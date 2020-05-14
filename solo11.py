# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal
sexo = input('Digite seu sexo: (1)Para homem (2)Para mulher: ')

if sexo == 1:
    aH = input('Digite sua altura: ')
    vH = 72.7 * aH
    rH = vH - 58
    print('Seu peso ideal é quilos' .format(rH))
elif sexo == 2:
    aM = input('Digite sua altura: ')
    vM = 62.1 * aM
    rM = vM - 44.7
    print('Seu peso ideal é quilos' .format(rM))
