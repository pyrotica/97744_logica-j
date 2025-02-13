import os

#limpa o terminal
os.system("clear")

print("ola mundo")

#solicitar dados ao usuario

nome=input('digite o nome')
idade=int(input('digite a idade'))

#imprimir os dados

print(f'o nome do usuario é: {nome}')
print(f'a idade do usuario é: {idade}')