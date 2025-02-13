import os

os.system("clear")

idade=int(input('digite a idade: '))

if idade > 18:
 print('maior de idade')


elif idade == 18:
 print('começando a maior idade')

else:
 print('menor idade')

print(f'A idade {idade} é de fulano')