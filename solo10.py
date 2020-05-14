# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
celsius = int(input('Entre com a temperatura:'))
fahrenheit = (celsius*1.8+32)//1
print('A temperatura tranformada é {}' .format(fahrenheit))