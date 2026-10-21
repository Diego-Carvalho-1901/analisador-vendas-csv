"""Leitura do CSV de vendas e os cálculos do relatório.

As funções daqui não imprimem nada nem dependem de arquivo aberto, o que
permite testá-las com listas montadas à mão.
"""

import csv
from collections.abc import Iterable
from dataclasses import dataclass
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path

COLUNAS = (
    "data da venda",
    "produto",
    "categoria",
    "quantidade vendida",
    "preco unitario",
)


class ErroLeitura(Exception):
    """Problema no CSV, com uma mensagem pronta para mostrar ao usuário."""


@dataclass(frozen=True)
class Venda:
    """Uma linha do CSV de vendas."""

    data: date
    produto: str
    categoria: str
    quantidade: int
    preco_unitario: Decimal

    @property
    def faturamento(self) -> Decimal:
        """Valor total da venda (quantidade x preço unitário)."""
        return self.quantidade * self.preco_unitario


def carregar_csv(caminho: Path) -> list[Venda]:
    """Abre o CSV em `caminho` e devolve as vendas.

    Lança ErroLeitura se o arquivo não existir ou se o conteúdo for inválido.
    """
    try:
        # skipinitialspace=True descarta o espaço depois de cada vírgula
        # ("2024-01-15, Notebook" vira "Notebook", e não " Notebook").
        with open(caminho, encoding="utf-8", newline="") as arquivo:
            return ler_vendas(csv.reader(arquivo, skipinitialspace=True))
    except FileNotFoundError:
        raise ErroLeitura(f"Arquivo não encontrado: {caminho}") from None


def ler_vendas(linhas: Iterable[list[str]]) -> list[Venda]:
    """Converte as linhas do CSV (a primeira é o cabeçalho) em vendas.

    Linhas em branco são ignoradas. Lança ErroLeitura, com o número da linha,
    quando o CSV está vazio ou quando alguma linha é inválida.
    """
    linhas = iter(linhas)
    if next(linhas, None) is None:
        raise ErroLeitura("O arquivo CSV está vazio.")

    vendas = []
    # O cabeçalho é a linha 1, então os dados começam na linha 2.
    for numero_linha, linha in enumerate(linhas, start=2):
        if not linha:
            continue
        vendas.append(_converter_linha(linha, numero_linha))

    if not vendas:
        raise ErroLeitura("O arquivo CSV não contém nenhuma venda.")
    return vendas


def _converter_linha(linha: list[str], numero_linha: int) -> Venda:
    """Valida uma linha do CSV e a transforma em Venda."""
    if len(linha) != len(COLUNAS):
        raise ErroLeitura(
            f"Linha {numero_linha}: esperadas {len(COLUNAS)} colunas "
            f"({', '.join(COLUNAS)}), mas foram encontradas {len(linha)}."
        )

    data_texto, produto, categoria, quantidade_texto, preco_texto = linha
    try:
        data = date.fromisoformat(data_texto)
    except ValueError:
        raise ErroLeitura(
            f"Linha {numero_linha}: data inválida '{data_texto}'. Use o formato AAAA-MM-DD."
        ) from None

    try:
        quantidade = int(quantidade_texto)
    except ValueError:
        quantidade = -1
    if quantidade <= 0:
        raise ErroLeitura(
            f"Linha {numero_linha}: quantidade inválida '{quantidade_texto}'. "
            "Use um número inteiro maior que zero."
        )

    try:
        # Decimal a partir do texto guarda exatamente "3500.00", sem o erro
        # de arredondamento que um float teria.
        preco = Decimal(preco_texto)
    except InvalidOperation:
        preco = None
    # Decimal aceita "NaN" e "Infinity", que não são preços.
    if preco is None or not preco.is_finite() or preco < 0:
        raise ErroLeitura(f"Linha {numero_linha}: preço inválido '{preco_texto}'.")

    return Venda(data, produto, categoria, quantidade, preco)
