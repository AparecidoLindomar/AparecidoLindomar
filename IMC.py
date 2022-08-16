import os

nome = input('Qual seu nome:')
peso = float(input('Informe seu peso:'))
altura = float(input('Informe sua altura:'))

imc = peso / altura**2

print(f"Seu IMC é:{imc:.2f}") 

if imc < 18.5:
	print(f"{nome}está abaixo do peso normal para seu IMC.")
elif imc < 24.9:
	print(f"{nome}está com o peso Normla para seu IMC.")
elif imc < 29.9:
	print(f"{nome}está com excesso de peso para sua altura.")
elif imc < 34.9:
	print(f"{nome}está com obesidade classe I, cuidado!!.")
elif imc < 39.9:
	print(f"{nome}está com obesidade classeII, precisa se preocupar com sua saúde.")
elif imc > 40:
	print(f"{nome}está com obesidade classe III, procure seu médico urgente.")

 
