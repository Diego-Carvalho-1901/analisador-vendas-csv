# Analisador de Vendas em CSV

## Sobre o projeto

Este projeto consiste em um analisador de vendas desenvolvido em Python, que processa dados armazenados em um arquivo CSV contendo informações como produtos, categorias, quantidade de unidades vendidas e preços unitários. A aplicação realiza diferentes análises, como faturamento por produto, produto mais vendido, faturamento por categoria, categoria com maior faturamento e faturamento total. Os resultados são apresentados no terminal, permitindo uma visualização mais clara do desempenho das vendas e dos produtos comercializados.

## Tecnologias utilizadas

- Python
- Biblioteca `csv`
- Arquivos no formato CSV

## Funcionalidades

- Cálculo do faturamento total
- Cálculo do faturamento por produto
- Identificação do produto mais vendido
- Cálculo do faturamento por categoria
- Identificação da categoria com maior faturamento


## Como executar

### Pré-requisitos

- Python 3 instalado
- Visual Studio Code (opcional, mas recomendado)

### Execução

1. Clone este repositório:
   ```bash
   git clone https://github.com/Diego-Carvalho-1901/analisador-vendas-csv.git

2. Acesse a pasta do projeto:
    cd analisador-vendas-csv

3. Execute o programa:
    python main.py

## Exemplo de Saída

```text
================================================
=========== FATURAMENTO POR PRODUTO ============
================================================
= >  Notebook : R$ 52500.00
= >  Smartphone : R$ 67500.00
= >  Memoria RAM : R$ 2250.00
= >  SSD : R$ 3900.00
= >  CPU : R$ 3850.00
= >  Monitor : R$ 4560.00
= >  Teclado : R$ 1440.00
= >  Mouse : R$ 1200.00
= >  Mousepad : R$ 450.00
= >  Headset : R$ 1500.00
= >  PC : R$ 28000.00
================================================
========== FATURAMENTO POR CATEGORIA ===========
================================================
= >  Eletronicos : R$ 162560.00
= >  Perifericos : R$ 4590.00
================================================
============== FATURAMENTO TOTAL ===============
================================================
= > Total do faturamento: R$ 167150.00
================================================
============= PRODUTO MAIS VENDIDO =============
================================================
= > Produto mais vendido:  Smartphone
= > Quantidade: 45
= > Faturamento: R$ 67500.00
================================================
=========== CATEGORIA MAIS FATURADA ============
================================================
= > Categoria mais faturada:  Eletronicos
= > Faturamento: R$ 162560.00
================================================


