def gravar_nome_em_arquivo():
    nome = input("Digite seu nome: ")
    with open("nome.txt", "w") as arquivo:
        arquivo.write(nome)
        
def imprimir_conteudo_arquivo():
    nome_arquivo = input("Digite o nome do arquivo: ")
    with open(nome_arquivo, "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
        
def copiar_conteudo_arquivo():
    with open("arquivo_original.txt", "r") as arquivo_original:
        conteudo = arquivo_original.read()
        with open("novo_arquivo.txt", "w") as novo_arquivo:
            novo_arquivo.write(conteudo)
            
def imprimir_nome_correspondente(numero):
    with open("arquivo_exemplo.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        if len(linhas) >= numero:
            print(linhas[numero - 1].strip())