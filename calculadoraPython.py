#calculadora Python

import math



def soma(num1, num2):
	return num1+num2

def subtracao(num1, num2):
	return num1-num2

def multiplicacao(num1, num2):
	return num1*num2

def divisao(num1, num2):
	return num1/num2


print("\n -------CALCULADORA PYTHON----------- \n")

print("\n Escolha um Opção: \n")
print("1 - SOMA")
print("2 - SUBTRAÇÃO")
print("3 - MULTIPLICAÇÃO")
print("4 - DIVISÃO")

escolha = input("\nEscolha sua opção, digite (1,2,3 ou 4): ")

num1 = int(input("\nDigite o primeiro numero: "))
num2 = int(input("\nDigite o segundo numero: "))

if escolha == '1':
	print("\n")
	print(num1, "+" , num2, "=",soma(num1,num2))
	print("\n")

elif escolha == '2':
	print("\n")
	print(num1, "-" , num2, "=",subtracao(num1,num2))
	print("\n")

elif escolha == '3':
	print("\n")
	print(num1, "*" , num2, "=",multiplicacao(num1,num2))
	print("\n")

elif escolha == '4':
	print("\n")
	print(num1, "/" , num2, "=",divisao(num1,num2))
	print("\n")

else:
	print("\n Opção inválida!")
