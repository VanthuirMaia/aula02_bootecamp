# Atividades Booleanas

# Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
expressao1 = input("Digite a primeira expressão booleana (True ou False): ")
expressao2 = input("Digite a segunda expressão booleana (True ou False): ")
resultado = expressao1 and expressao2
print(f"O resultado da operação AND entre as expressões é: {resultado}")

#Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
expressao1 = input("Digite a primeira expressão booleana (True ou False): ")
expressao2 = input("Digite a segunda expressão booleana (True ou False): ")
resultado = expressao1 or expressao2
print(f"O resultado da operação OR entre as expressões é: {resultado}")

# Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
valor = input("Digite um valor booleano (True ou False): ")
valor = not valor
print(f"O valor invertido é: {valor}")

# Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
resultado = numero1 == numero2
if resultado:
    print("Os números são iguais.")
else:
    print("Os números são diferentes.")



