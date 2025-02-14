import os

os.system("clear")

num=int(input('digite o numero: '))

if num > 10:
 print(f'{num} é maior que 10')

elif num == 10:
 print(f'{num} é iqual a 10')

else:
 print(f'{num} é menor que 10')