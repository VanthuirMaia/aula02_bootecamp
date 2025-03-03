# 1) Solicita ao usuário que digite seu nome
nome_usuario = input("Digite seu nome: ")
if nome_usuario.isdigit():
    print("Digite um nome válido!")
    exit()
elif len(nome_usuario) == 0:
    print("Você não digitou nada")
    exit()






    
# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario = float(input("Digite o valor do seu salário: "))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus = float(input("Digite o valor do bônus recebido: "))

# 4) Calcule o valor do bônus final
bonus_final = salario + bonus

# 5) Imprima cálculo do KPI para o usuário
print(f"O KPI do usuário {nome_usuario} é de {bonus_final}")

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"O usuário {nome_usuario} tem um salário de R$ {salario} e recebeu um bônus de R$ {bonus}")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?