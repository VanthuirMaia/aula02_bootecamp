
# Atividades String

# Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
palavra = input("Digite uma palavra: ")
print(f"A palavra em letras Maiúsculas é: {palavra.upper()}")

# Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome = input("Digite seu nome completo: ")
print(f"Seu nome em letras minúsculas é: {nome.lower()}")

# Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input("Digite uma frase: ")
print(f"A frase sem espaços em branco no início e no final é: {frase.strip()}")

# Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input("Digite uma data no formato 'dd/mm/aaaa': ")
dia, mes, ano = data.split("/")
print(f"O dia é: {dia}")
print(f"O mês é: {mes}")
print(f"O ano é: {ano}")

# Escreva um programa que concatene duas strings fornecidas pelo usuário.
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
print("Seu nome completo é: ", nome + " " + sobrenome)

