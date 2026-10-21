from datetime import date
from decimal import Decimal

from vendas import (
    Venda,
    categoria_mais_faturada,
    faturamento_por_categoria,
    faturamento_por_mes,
    faturamento_por_produto,
    faturamento_total,
    produto_mais_vendido,
    quantidade_por_produto,
)


def venda(dia: str, produto: str, categoria: str, qtd: int, preco: str) -> Venda:
    return Venda(date.fromisoformat(dia), produto, categoria, qtd, Decimal(preco))


VENDAS = [
    venda("2024-02-10", "Mouse", "Perifericos", 3, "80.10"),
    venda("2024-01-15", "Notebook", "Eletronicos", 1, "3500.00"),
    venda("2024-01-20", "Mouse", "Perifericos", 2, "80.10"),
]


def test_faturamento_total():
    assert faturamento_total(VENDAS) == Decimal("3900.50")


def test_faturamento_total_de_lista_vazia_e_zero():
    assert faturamento_total([]) == Decimal(0)


def test_faturamento_por_produto():
    assert faturamento_por_produto(VENDAS) == {
        "Mouse": Decimal("400.50"),
        "Notebook": Decimal("3500.00"),
    }


def test_faturamento_por_categoria():
    assert faturamento_por_categoria(VENDAS) == {
        "Perifericos": Decimal("400.50"),
        "Eletronicos": Decimal("3500.00"),
    }


def test_faturamento_por_mes_em_ordem_cronologica():
    resultado = faturamento_por_mes(VENDAS)
    assert list(resultado) == ["2024-01", "2024-02"]
    assert resultado["2024-01"] == Decimal("3660.20")
    # Com float, 3 * 80.10 daria 240.29999999999998.
    assert resultado["2024-02"] == Decimal("240.30")


def test_quantidade_por_produto():
    assert quantidade_por_produto(VENDAS) == {"Mouse": 5, "Notebook": 1}


def test_produto_mais_vendido_conta_unidades_e_nao_faturamento():
    assert produto_mais_vendido(VENDAS) == ("Mouse", 5)


def test_produto_mais_vendido_em_empate_fica_com_o_primeiro():
    vendas = [
        venda("2024-01-01", "A", "X", 2, "1"),
        venda("2024-01-01", "B", "X", 2, "1"),
    ]
    assert produto_mais_vendido(vendas) == ("A", 2)


def test_categoria_mais_faturada():
    assert categoria_mais_faturada(VENDAS) == ("Eletronicos", Decimal("3500.00"))
