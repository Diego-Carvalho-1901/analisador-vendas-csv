"""Testes do ponto de entrada (main.py) e do texto do relatório."""

from datetime import date
from decimal import Decimal

from main import CSV_PADRAO, _reais, gerar_relatorio, main
from vendas import Venda


def test_csv_padrao_fica_na_pasta_dados_do_projeto():
    assert CSV_PADRAO.is_absolute()
    assert CSV_PADRAO.parts[-2:] == ("dados", "vendas.csv")
    assert CSV_PADRAO.exists()


def test_reais_no_padrao_brasileiro():
    assert _reais(Decimal(167150)) == "R$ 167.150,00"
    assert _reais(Decimal("0.5")) == "R$ 0,50"


def test_relatorio_traz_todas_as_secoes():
    vendas = [
        Venda(date(2024, 1, 15), "Notebook", "Eletronicos", 2, Decimal("3500.00")),
        Venda(date(2024, 2, 1), "Mouse", "Perifericos", 3, Decimal("80.00")),
    ]
    texto = gerar_relatorio(vendas)
    assert "= > Notebook : R$ 7.000,00" in texto
    assert "= > Perifericos : R$ 240,00" in texto
    assert "= > 2024-02 : R$ 240,00" in texto
    assert "= > Total do faturamento: R$ 7.240,00" in texto
    assert "= > Produto mais vendido: Mouse" in texto
    assert "= > Categoria mais faturada: Eletronicos" in texto


def test_main_com_csv_de_exemplo(capsys):
    assert main([]) == 0
    saida = capsys.readouterr().out
    # Os números do README: confere que a refatoração não mudou os resultados.
    assert "= > Total do faturamento: R$ 167.150,00" in saida
    assert "= > Produto mais vendido: Smartphone" in saida
    # Sem espaço sobrando antes do nome (bug do CSV com ", ").
    assert "= > Notebook : R$ 52.500,00" in saida


def test_main_com_arquivo_inexistente(tmp_path, capsys):
    assert main([str(tmp_path / "nao_existe.csv")]) == 1
    assert "Arquivo não encontrado" in capsys.readouterr().err


def test_main_com_csv_vazio(tmp_path, capsys):
    arquivo = tmp_path / "vazio.csv"
    arquivo.write_text("", encoding="utf-8")
    assert main([str(arquivo)]) == 1
    assert "Erro: O arquivo CSV está vazio." in capsys.readouterr().err
