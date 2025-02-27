#Escreva um programa que solicite ao usuário um número e verifique se ele é positivo, negativo, ou zero. 
numero_str = input(("digite um número:"))
numero = int(numero_str)
if numero  >=1:
    print('Este número é positivo!') 
elif numero <0:
    print('Este número é negativo!')
else: 
    print('O número é igual a zero!') 
