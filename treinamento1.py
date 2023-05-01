nome = input("Qual o seu nome?")
nascimento = int(input("Em que ano você nasceu?"))
idade = (2023 - nascimento)
peso = float(input("informe seu peso atual: "))
altura = float(input("informe seu altura atual: "))

massa_corporal = (peso / (altura ** 2))


print("\nSeja bem vindo", nome, "\nsua idade é: ", idade, "\nSua massa corporal é: ", round(massa_corporal,2))

