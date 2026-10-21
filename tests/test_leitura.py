from datetime import date
from decimal import Decimal

import pytest

from vendas import ErroLeitura, Venda, carregar_csv, ler_vendas

CABECALHO = [
    "data da venda",
    "produto",
    "categoria",
    "quantidade vendida",
    "preco unitario",
]


def test_le_uma_venda_com_decimal():
    vendas = ler_vendas(
        [CABECALHO, ["2024-01-15", "Notebook", "Eletronicos", "5", "3500.00"]]
    )
    assert vendas == [
        Venda(date(2024, 1, 15), "Notebook", "Eletronicos", 5, Decimal("3500.00"))
    ]
    assert vendas[0].faturamento == Decimal("17500.00")


def test_carregar_csv_remove_espaco_depois_da_virgula(tmp_path):
    arquivo = tmp_path / "vendas.csv"
    arquivo.write_text(
        "data da venda, produto, categoria, quantidade vendida, preco unitario\n"
        "2024-01-15, Notebook, Eletronicos, 5, 3500.00\n",
        encoding="utf-8",
    )
    [venda] = carregar_csv(arquivo)
    assert venda.produto == "Notebook"
    assert venda.categoria == "Eletronicos"


def test_ignora_linhas_em_branco():
    linhas = [CABECALHO, [], ["2024-01-15", "Mouse", "Perifericos", "2", "80.00"], []]
    assert len(ler_vendas(linhas)) == 1


def test_arquivo_inexistente_vira_erro_de_leitura(tmp_path):
    with pytest.raises(ErroLeitura, match="Arquivo não encontrado"):
        carregar_csv(tmp_path / "nao_existe.csv")


def test_csv_vazio():
    with pytest.raises(ErroLeitura, match="vazio"):
        ler_vendas([])


def test_csv_so_com_cabecalho():
    with pytest.raises(ErroLeitura, match="nenhuma venda"):
        ler_vendas([CABECALHO])


@pytest.mark.parametrize(
    ("linha", "mensagem"),
    [
        (["2024-01-15", "Mouse", "Perifericos", "2"], "Linha 2: esperadas 5 colunas"),
        (
            ["15/01/2024", "Mouse", "Perifericos", "2", "80.00"],
            "Linha 2: data inválida",
        ),
        (
            ["2024-01-15", "Mouse", "Perifericos", "dois", "80.00"],
            "Linha 2: quantidade inválida",
        ),
        (
            ["2024-01-15", "Mouse", "Perifericos", "0", "80.00"],
            "Linha 2: quantidade inválida",
        ),
        (["2024-01-15", "Mouse", "Perifericos", "2", "abc"], "Linha 2: preço inválido"),
        (["2024-01-15", "Mouse", "Perifericos", "2", "NaN"], "Linha 2: preço inválido"),
        (["2024-01-15", "Mouse", "Perifericos", "2", "-1"], "Linha 2: preço inválido"),
    ],
)
def test_linhas_invalidas_indicam_o_numero_da_linha(linha, mensagem):
    with pytest.raises(ErroLeitura, match=mensagem):
        ler_vendas([CABECALHO, linha])
