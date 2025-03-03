"""
# Atividades Try-Except

# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

try:
    Temperatura = float(input("Digite a temperatura em Celsius: "))
    Fahrenheit = (Temperatura * 1.8) + 32
    print(f"A temperatura em Fahrenheit é {Fahrenheit} °F")
except ValueError:
    print("Por favor, digite um número válido.")

# Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.
try:
    frase = input("Digite uma palavra ou frase: ").lower()
    if not isinstance(frase, str) or not all(e.isalnum() or e.isspace() for e in frase):
        raise ValueError("A entrada deve conter apenas letras.")
    frase = ''.join(e for e in frase if e.isalnum())
    if frase == frase[::-1]:
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo!")
except ValueError as e:
    print(f"Erro: {e}")

# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. Use try-except para lidar com divisões por zero e entradas não numéricas. Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.
try:
    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")
    operador = input("Digite o operador (+, -, *, /): ")
    if not num1.isnumeric() or not num2.isnumeric():
        raise ValueError("Os números devem ser inteiros.")
    num1 = int(num1)
    num2 = int(num2)
    if operador not in ['+', '-', '*', '/']:
        raise ValueError("Operador inválido.")
    if operador == '/' and num2 == 0:
        raise ZeroDivisionError("Divisão por zero.")
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        resultado = num1 / num2
    print(f"O resultado é {resultado}")
except ValueError as e:
    print(f"Erro: {e}")
except ZeroDivisionError as e:
    print(f"Erro: {e}")

# Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".
try:
    numero = int(input("Digite um número: "))
    if numero > 0:
        sinal = "positivo"
    elif numero < 0:
        sinal = "negativo"
    else:
        sinal = "zero"
    if numero % 2 == 0:
        paridade = "par"
    else:
        paridade = "ímpar"
    print(f"O número é {sinal} e {paridade}.")
except ValueError:
    print("Por favor, digite um número inteiro válido.")    

# Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a string de entrada em uma lista de números inteiros. Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.
try:
    numeros = input("Digite uma lista de números separados por vírgula: ").split(',')
    numeros = [int(numero) for numero in numeros]
    print(f" A lista de números é: {numeros}")
except ValueError:
    print("Erro: A lista deve conter apenas números inteiros.")

"""


