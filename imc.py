#!/usr/bin/python3

height = float(input("Digite sua altura em metros: "))
weight = float(input("Digite seu peso em Kg: "))
imc = weight / height**2
print("Seu IMC é: %.4f" % imc)
