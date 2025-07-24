"""
    1- Calculadora Simples
    Crie um programa que simule uma calculadora básica com as seguintes funcionalidades:

    * Solicite ao usuário dois números reais.  
    * Peça a operação desejada (+, -, *, /).  
    * Realize a operação escolhida e exiba o resultado.  
    * Trate divisões por zero e operações inválidas com mensagens apropriadas.  

    O programa deve continuar solicitando entradas até que uma operação válida seja realizada com sucesso.
"""


while True:
    try:
        a = float(input("Digite o primeiro número real: "))
        b = float(input("Digite o segundo número real: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite números reais.")
        continue

    op = input("Escolha a operação (+, -, *, /): ")

    if op == '+':
        resultado = a + b
    elif op == '-':
        resultado = a - b
    elif op == '*':
        resultado = a * b
    elif op == '/':
        if b == 0:
            print("Erro: divisão por zero não é permitida. Tente novamente.")
            continue
        resultado = a / b
    else:
        print("Operação inválida. Use apenas +, -, * ou /.")
        continue

    print(f"Resultado: {resultado}")
    break
