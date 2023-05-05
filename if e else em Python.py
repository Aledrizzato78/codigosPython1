#Ler dois números codigo simples
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
 
# Escolha o número maior
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2
 
# Imprimir o resultado
print("O maior número é:", larger_number)


#Ler dois números codigo complexo
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
 
# Escolha o número maior
if number1 > number2: larger_number = number1
else: larger_number = number2
 
# Imprimir o resultado
print("O maior número é:", larger_number)


# Leia três números
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))
 
# Assumimos temporariamente que o primeiro número
# é o maior deles.
# Em breve verificaremos isso.
largest_number = number1
 
# Nós verificamos se o segundo número é maior que o maior_número atual
# e atualize o maior_número, se necessário.
if number2 > largest_number:
    largest_number = number2
 
# Nós verificamos se o terceiro número é maior que o maior_número atual
# e atualize o maior_número, se necessário.
if number3 > largest_number:
    largest_number = number3
 
# Imprimir o resultado
print("O maior número é:", largest_number)

# Leia três números função max e min:
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
 
# Verifique qual dos números é o maior
# e passe-o para a variável de número_maior.
 
largest_number = max(a, b, c)
menor_numero = min(a, b, c)
 
# Imprimir o resultado.
print("O maior número é:", largest_number, "o menor numero é: ", menor_numero)
