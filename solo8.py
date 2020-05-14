#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
horas = int(input('Quantas horas você trabalha por mês?'))
salario = int(input('Quanto você ganha por hora?'))
total = (horas*salario)
print('Você ganha {} por mês' .format(total))