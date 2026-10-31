"""Garante que o exemplo de saída do README é a saída real do programa.

Se o relatório mudar e o README não, este teste falha e mostra a diferença.
"""

import re
from pathlib import Path

from main import CSV_PADRAO, gerar_relatorio
from vendas import carregar_csv

README = Path(__file__).resolve().parent.parent / "readme.md"


def _exemplo_de_saida_do_readme() -> str:
    """Devolve o conteúdo do bloco ```text da seção "Exemplo de saída"."""
    texto = README.read_text(encoding="utf-8")
    secao = texto.split("## Exemplo de saída", maxsplit=1)[1]
    bloco = re.search(r"```text\n(.*?)\n```", secao, flags=re.DOTALL)
    assert bloco is not None, "README sem bloco ```text em 'Exemplo de saída'"
    return bloco.group(1)


def test_exemplo_do_readme_igual_a_saida_do_csv_de_exemplo():
    saida_real = gerar_relatorio(carregar_csv(CSV_PADRAO))
    assert _exemplo_de_saida_do_readme() == saida_real
