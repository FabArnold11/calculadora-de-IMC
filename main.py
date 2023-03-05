print("Seja bem-vindo ao sistema de cálculo para IMC!!")
print("###############################################")
print("Por favor digite os seguintes dados: ")

peso = float(input("Peso em quilogramas: "))

altura = float(input("Altura em metros: "))

imc = peso/(altura * altura)

if 0 <= imc <= 18.49:
    print("Você está abaixo do peso ideal!")
elif 18.5 <= imc <= 24.99:
    print("Você está no peso idea!l")
elif 25 <= imc <= 29.99:
    print("Você está acima do peso ideal!")
else:
    print("Você está em nível de obesidade!")
