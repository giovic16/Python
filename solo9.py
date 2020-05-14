#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
fahrenheit = int(input('Entre com a temperatura:'))
celsius = (fahrenheit-32)//1.8
print('A temperatura transofrmada é {}' .format(celsius))