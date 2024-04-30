def imprimir_informacoes(nome, idade, cidade):
    print(f"Nome: {nome} - Idade: {idade} - Cidade: {cidade}!", sep='', end='')

# Exemplo de uso da função
imprimir_informacoes("Rafa", 23, "Rio de Janeiro")

def calcular_operacao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação desejada (+, -, *, /): ")

    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: divisão por zero!")
            return
    
    print("Resultado:", resultado)

# Exemplo de uso da função
calcular_operacao()

def lista_compras():
    itens = input("Digite os itens da lista de compras, separados por vírgula: ").split(',')
    for i, item in enumerate(itens, start=1):
        print(f"Item {i}: {item.strip()}")

# Testando a função
lista_compras()

def converter_celsius_para_fahrenheit():
    celsius = float(input("Digite a temperatura em graus Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Temperatura em Fahrenheit:", fahrenheit)

# Testando a função
converter_celsius_para_fahrenheit()

def pedir_nomes():
    nomes = []
    while True:
        nome = input("Digite um nome (digite 'sair' para finalizar): ")
        if nome.lower() == 'sair':
            break
        nomes.append(nome)
    
    print("Nomes digitados:")
    for nome in nomes:
        print(nome)

# Testando a função
pedir_nomes()
