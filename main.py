#############################################################
###       ANALISADOR DE VENDAS DE UMA EMPRESA             ###
#############################################################
# NOME DA EMPRESA: GALO ELETRONICS LTDA                     #
#                                                           #
# FUNÇÃO DO PROGRAMA: ANALISAR VENDAS DE PRODUTOS           #
#                                                           #
# DESCRIÇÃO: O PROGRAMA DEVE REALIZAR AS SEGUINTES FUNCOES: # 
# 1. LER UM ARQUIVO CSV COM OS DADOS DE VENDAS DE PRODUTOS; #
# 2. CALCULAR O FATURAMENTO TOTAL DE CADA PRODUTO;          #
# 3. CALCULAR O FATURAMENTO TOTAL DE TODOS OS PRODUTOS;     #
# 4. IDENTIFICAR O PRODUTO MAIS VENDIDO;                    #
# 5. ANALISAR AS CATEGORIAS E O FATURAMENTO POR CATEGORIA;  #
#############################################################

import csv # importa a biblioteca CSV para ler arquivos CSV

arquivo = open('dados/vendas.csv') # abre o arquivo CSV com os dados de vendas
leitor = csv.reader(arquivo) # permite a leitura do arquivo CSV

next (leitor)     # Pular o cabeçalho para leitura de dados em numeros inteiros
total = 0   # inicializa a variável total para armazenar a quantidade total de produtos vendidos
total_faturamento = 0    # inicializa a variável total_faturamento para armazenar o faturamento total
faturamento_produtos = {} # cria um dicionário para armazenar o faturamento por produto
maior_quantidade = 0 # inicializa a variável para armazenar a maior quantidade vendida
produto_mais_vendido = "" # inicializa a variável para armazenar o nome do produto mais vendido
quantidade_produtos = {} # cria um dicionário para armazenar a quantidade de produtos vendidos
faturamento_categorias = {} # cria um dicionário para armazenar o faturamento por categoria
maior_faturamento_categorias = 0 # inicializa variável para saber o maior faturamento por categoria
categoria_mais_faturada = "" # inicializa variável para saber qual categoria teve o maior faturamento


for linha in leitor:
    quantidade = int(linha [3])
    #print(quantidade)
    total = total + quantidade    # Esta etapa do "for" soma a quantidade de produtos vendidos

    preco = float(linha [4])
    faturamento = quantidade * preco
    total_faturamento = total_faturamento + faturamento # Esta etapa do "for" soma o faturamento total

    

    produto = linha[1] # obtém o nome do produto da linha atual
    categoria = linha[2] # obtém o nome da categoria da linha atual

    if produto in faturamento_produtos: # verifica se o produto já está no dicionário
        faturamento_produtos[produto] = faturamento_produtos[produto] + faturamento 
        # L> se o produto já estiver no dicionário, soma o faturamento atual ao faturamento existente
    else:
        faturamento_produtos[produto] = faturamento 
         # L> se o produto não estiver no dicionário, adiciona o produto com o faturamento atual

    if categoria in faturamento_categorias:
        faturamento_categorias[categoria] = faturamento_categorias[categoria] + faturamento
        # L> se a categoria já estiver no dicionário, soma o faturamento atual ao existente
    else:
        faturamento_categorias[categoria] = faturamento
        # L> se não estiver no dicionário, adiciona a categoria com o faturamento atual

    if produto in quantidade_produtos:
        quantidade_produtos[produto] = quantidade_produtos[produto] + quantidade
        # L> se o produto já estiver no dicionário, soma a quantidade atual à existente
    else:
        quantidade_produtos[produto] = quantidade
        # L> se não estiver no dicionário, adiciona o produto com a quantidade atual

for produto in quantidade_produtos:
    if quantidade_produtos[produto] > maior_quantidade:
        maior_quantidade = quantidade_produtos[produto]
        produto_mais_vendido = produto 
    # L> se a quantidade atual for maior que a maior quantidade, 
    # atualiza a maior quantidade e o produto mais vendido
    

for categoria in faturamento_categorias:
    if faturamento_categorias[categoria] > maior_faturamento_categorias:
        maior_faturamento_categorias = faturamento_categorias[categoria]
        categoria_mais_faturada = categoria 
        # L> Se o faturamento atual for maior que o maior faturamento,
        # atualiza o maior faturamento e a categoria mais faturada


print("================================================")
print("=========== FATURAMENTO POR PRODUTO ============")
print("================================================")
for produto in faturamento_produtos:
    print(f"= > {produto} : R$ {faturamento_produtos[produto]:.2f}") 
    # L> Imprime o faturamento por produto

print("================================================")
print("========== FATURAMENTO POR CATEGORIA ===========")
print("================================================")
for categoria in faturamento_categorias:
    print(f"= > {categoria} : R$ {faturamento_categorias[categoria]:.2f}")
    # L> Imprime o faturamento por categoria    

print("================================================")
print("============== FATURAMENTO TOTAL ===============")
print("================================================")
print(f"= > Total do faturamento: R$ {total_faturamento:.2f}") # Imprime o faturamento total

print("================================================")
print("============= PRODUTO MAIS VENDIDO =============")
print("================================================")
print(f"= > Produto mais vendido: {produto_mais_vendido}") # Imprime o produto mais vendido
print(f"= > Quantidade: {maior_quantidade}") # Imprime a quantidade do produto mais vendido
print(f"= > Faturamento: R$ {faturamento_produtos[produto_mais_vendido]:.2f}")
        # L>Imprime o faturamento do produto mais vendido

print("================================================")
print("=========== CATEGORIA MAIS FATURADA ============")
print("================================================")
print(f"= > Categoria mais faturada: {categoria_mais_faturada}") # Imprime a categoria mais faturada
print(f"= > Faturamento: R$ {maior_faturamento_categorias:.2f}") 
# L> Imprime o faturamento da categoria mais faturada

print("================================================")
