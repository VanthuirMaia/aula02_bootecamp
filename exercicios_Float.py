
# Atividades Float

# Escreva um programa que receba dois números flutuantes e realize sua adição.
Num1 = float(input("Digite o primeiro número: "))
Num2 = float(input("Digite o segundo número: "))
Soma = Num1 + Num2
print(f"A soma dos dois números é {Soma}")


# Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
Num1 = float(input("Digite o primeiro número: "))
Num2 = float(input("Digite o segundo número: "))
Media = (Num1 + Num2) / 2
print(f"A média dos dois números é {Media}")

# Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
Num = float(input("Digite o número: "))
Expoente = float(input("Digite o expoente: "))
Potencia = Num ** Expoente
print(f"O número {Num} elevado a {Expoente} é igual a {Potencia}")

# Faça um programa que converta a temperatura de Celsius para Fahrenheit.
Temperatura = float(input("Digite a temperatura em Celsius: "))
Fahrenheit = (Temperatura * 1.8) + 32
print(f"A temperatura em Fahrenheit é {Fahrenheit} °F")


# Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
Raio = float(input("Digite o raio do círculo: "))
Area = 3.14 * (Raio ** 2)
print(f"A área do círculo é {Area}")