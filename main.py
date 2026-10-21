"""Analisador de vendas em CSV — ponto de entrada pela linha de comando.

Lê um CSV de vendas e imprime faturamento por produto, por categoria e por
mês, o faturamento total, o produto mais vendido e a categoria mais faturada.
Os dados de exemplo são da empresa fictícia Galo Eletronics Ltda.

Uso:
    python main.py                      # usa dados/vendas.csv
    python main.py caminho/para/arquivo.csv
"""

import argparse
import sys
from decimal import Decimal
from pathlib import Path

from vendas import (
    ErroLeitura,
    Venda,
    carregar_csv,
    categoria_mais_faturada,
    faturamento_por_categoria,
    faturamento_por_mes,
    faturamento_por_produto,
    faturamento_total,
    produto_mais_vendido,
)

# Resolvido a partir deste arquivo, e não do diretório atual, para o programa
# funcionar mesmo quando é chamado de outra pasta.
CSV_PADRAO = Path(__file__).resolve().parent / "dados" / "vendas.csv"
LARGURA = 48


def gerar_relatorio(vendas: list[Venda]) -> str:
    """Monta o texto do relatório a partir das vendas."""
    linhas: list[str] = []

    linhas += _cabecalho("FATURAMENTO POR PRODUTO")
    linhas += _listar(faturamento_por_produto(vendas))

    linhas += _cabecalho("FATURAMENTO POR CATEGORIA")
    linhas += _listar(faturamento_por_categoria(vendas))

    linhas += _cabecalho("FATURAMENTO POR MÊS")
    linhas += _listar(faturamento_por_mes(vendas))

    linhas += _cabecalho("FATURAMENTO TOTAL")
    linhas.append(f"= > Total do faturamento: {_reais(faturamento_total(vendas))}")

    produto, quantidade = produto_mais_vendido(vendas)
    linhas += _cabecalho("PRODUTO MAIS VENDIDO")
    linhas.append(f"= > Produto mais vendido: {produto}")
    linhas.append(f"= > Quantidade: {quantidade}")
    linhas.append(
        f"= > Faturamento: {_reais(faturamento_por_produto(vendas)[produto])}"
    )

    categoria, valor = categoria_mais_faturada(vendas)
    linhas += _cabecalho("CATEGORIA MAIS FATURADA")
    linhas.append(f"= > Categoria mais faturada: {categoria}")
    linhas.append(f"= > Faturamento: {_reais(valor)}")

    linhas.append("=" * LARGURA)
    return "\n".join(linhas)


def _cabecalho(titulo: str) -> list[str]:
    """Título centralizado entre duas linhas de '='."""
    return ["=" * LARGURA, f" {titulo} ".center(LARGURA, "="), "=" * LARGURA]


def _listar(totais: dict[str, Decimal]) -> list[str]:
    """Uma linha "= > nome : R$ valor" para cada item."""
    return [f"= > {nome} : {_reais(valor)}" for nome, valor in totais.items()]


def _reais(valor: Decimal) -> str:
    """Formata no padrão brasileiro: R$ 1.234,56."""
    texto = f"{valor:,.2f}"  # 1,234.56
    return "R$ " + texto.replace(",", "_").replace(".", ",").replace("_", ".")


def criar_parser() -> argparse.ArgumentParser:
    """Define os argumentos aceitos na linha de comando."""
    parser = argparse.ArgumentParser(
        description="Analisa um CSV de vendas e imprime o faturamento."
    )
    parser.add_argument(
        "csv",
        nargs="?",
        type=Path,
        default=CSV_PADRAO,
        help="CSV com as colunas data da venda, produto, categoria, "
        "quantidade vendida, preco unitario (padrão: dados/vendas.csv)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Lê o CSV, imprime o relatório e devolve o código de saída do programa."""
    argumentos = criar_parser().parse_args(argv)
    try:
        vendas = carregar_csv(argumentos.csv)
    except ErroLeitura as erro:
        print(f"Erro: {erro}", file=sys.stderr)
        return 1

    print(gerar_relatorio(vendas))
    return 0


if __name__ == "__main__":
    sys.exit(main())
