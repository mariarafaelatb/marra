# Função para calcular a soma e a média de uma lista de números
def calcular_soma_e_media(lista):
    soma = sum(lista)
    media = soma / len(lista)
    return soma, media

# Função para substituir as ocorrências de uma palavra por outra em uma lista de palavras
def substituir_palavra(lista, palavra_antiga, palavra_nova):
    for i in range(len(lista)):
        if lista[i] == palavra_antiga:
            lista[i] = palavra_nova
    return lista

# Função para gerar um triângulo de asteriscos para o número de linhas informado
def gerar_triangulo(num_linhas):
    for i in range(1, num_linhas + 1):
        print('*' * i)

# Testando as funções
lista_numeros = [1, 2, 3, 4]
soma, media = calcular_soma_e_media(lista_numeros)
print("Soma:", soma)
print("Média:", media)

lista_palavras = ["banana", "morango", "limão"]
palavra_antiga = "limão"
palavra_nova = "laranja"
nova_lista = substituir_palavra(lista_palavras, palavra_antiga, palavra_nova)
print("Lista alterada:", nova_lista)

num_linhas = 4
gerar_triangulo(num_linhas)

