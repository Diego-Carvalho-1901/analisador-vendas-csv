# Analisador de Vendas em CSV

[![CI](https://github.com/Diego-Carvalho-1901/analisador-vendas-csv/actions/workflows/ci.yml/badge.svg)](https://github.com/Diego-Carvalho-1901/analisador-vendas-csv/actions/workflows/ci.yml)

## Sobre o projeto

Este projeto consiste em um analisador de vendas desenvolvido em Python, que processa dados armazenados em um arquivo CSV contendo informações como produtos, categorias, quantidade de unidades vendidas e preços unitários. A aplicação realiza diferentes análises, como faturamento por produto, produto mais vendido, faturamento por categoria, categoria com maior faturamento e faturamento total. Os resultados são apresentados no terminal, permitindo uma visualização mais clara do desempenho das vendas e dos produtos comercializados.

## Tecnologias utilizadas

- Python 3.12 (biblioteca padrão: `csv`, `decimal`, `argparse`, `pathlib`)
- [pytest](https://docs.pytest.org/) para os testes
- [ruff](https://docs.astral.sh/ruff/) como linter e formatador
- GitHub Actions para integração contínua

## Funcionalidades

- Cálculo do faturamento total
- Cálculo do faturamento por produto
- Cálculo do faturamento por categoria
- Cálculo do faturamento por mês (a partir da coluna de data)
- Identificação do produto mais vendido
- Identificação da categoria com maior faturamento
- Mensagens de erro claras, com o número da linha, para arquivos inválidos

## Estrutura do projeto

```text
analisador-vendas-csv/
├── main.py              # ponto de entrada: argumentos, relatório e mensagens de erro
├── vendas.py            # modelo Venda, leitura do CSV e cálculos (funções puras)
├── dados/
│   └── vendas.csv       # dados de exemplo (empresa fictícia)
├── tests/               # testes com pytest
├── requirements.txt     # dependências do programa (hoje, só a biblioteca padrão)
└── requirements-dev.txt # dependências de desenvolvimento (pytest e ruff)
```

## Como executar

### Pré-requisitos

- Python 3.12 ou mais recente
- Visual Studio Code (opcional, mas recomendado)

### Execução

1. Clone este repositório:

   ```bash
   git clone https://github.com/Diego-Carvalho-1901/analisador-vendas-csv.git
   ```

2. Acesse a pasta do projeto:

   ```bash
   cd analisador-vendas-csv
   ```

3. Execute o programa:

   ```bash
   python main.py                        # usa dados/vendas.csv
   python main.py caminho/para/outro.csv # analisa outro arquivo
   ```

O CSV precisa ter as colunas `data da venda, produto, categoria, quantidade vendida, preco unitario`,
com datas no formato `AAAA-MM-DD` e preços com ponto decimal (`3500.00`).
Se o arquivo não existir ou alguma linha estiver inválida, o programa mostra uma
mensagem dizendo qual linha corrigir e termina com código de saída 1.

## Como rodar os testes

Recomenda-se um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate        # no Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt

pytest                # roda todos os testes da pasta tests/
ruff check .          # procura erros e más práticas no código
ruff format --check . # confere a formatação (use "ruff format ." para corrigir)
```

Os mesmos comandos rodam automaticamente no GitHub Actions a cada push na `main`
e em todo pull request (arquivo `.github/workflows/ci.yml`). O selo no topo deste
README mostra se a última execução passou.

## Exemplo de saída

Saída para o arquivo de exemplo `dados/vendas.csv`:

```text
================================================
=========== FATURAMENTO POR PRODUTO ============
================================================
= > Notebook : R$ 52.500,00
= > Smartphone : R$ 67.500,00
= > Memoria RAM : R$ 2.250,00
= > SSD : R$ 3.900,00
= > CPU : R$ 3.850,00
= > Monitor : R$ 4.560,00
= > Teclado : R$ 1.440,00
= > Mouse : R$ 1.200,00
= > Mousepad : R$ 450,00
= > Headset : R$ 1.500,00
= > PC : R$ 28.000,00
================================================
========== FATURAMENTO POR CATEGORIA ===========
================================================
= > Eletronicos : R$ 162.560,00
= > Perifericos : R$ 4.590,00
================================================
============= FATURAMENTO POR MÊS ==============
================================================
= > 2024-01 : R$ 167.150,00
================================================
============== FATURAMENTO TOTAL ===============
================================================
= > Total do faturamento: R$ 167.150,00
================================================
============= PRODUTO MAIS VENDIDO =============
================================================
= > Produto mais vendido: Smartphone
= > Quantidade: 45
= > Faturamento: R$ 67.500,00
================================================
=========== CATEGORIA MAIS FATURADA ============
================================================
= > Categoria mais faturada: Eletronicos
= > Faturamento: R$ 162.560,00
================================================
```
