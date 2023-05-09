#list_1 = [1]
#list_2 = list_1
#list_1 [0] = 2
#print(list_2)


#fatia
#list_1 = [1]
#list_2 = list_1[:]
#list_1[0] = 2
#print(list_2)

#my_list[start:end] modelo de codigo para executar a fatia de listas

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)


#my_list[:end] equivale a my_list[0:end]

#my_list[start:] neste caso ele lé do final para o começo my_list[start:len(my_list)]


#utilizando Del nas listas
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

#Nota: nesse caso, a fatia não gera nenhuma nova lista!

#O resultado do snippet é: [10, 4, 2].


#in e not in na lista - verifica se um elemento esta ou não dentro da lista - retorna false ou true
my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)


# encontra o maior elemento da lista
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)

# aplicando o for no cidogo acima
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
 
for i in my_list:
    if i > largest:
        largest = i
 
print(largest)


#utilizando fatia no codigo acima
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
 
for i in my_list[1:]:
    if i > largest:
        largest = i
 
print(largest)

# mesmo codigo, mas reescrito para localizar a posição, e não o elemento
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False
 
for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break
 
if found:
    print("Elemento encontrado no índice", i)
else:
    print("ausente")


# localizando elementos de uma lista em outrra lista
a = [5, 11, 9, 42, 3, 49]
b = [3, 7, 11, 42, 34, 49]

 
for number in b:
    if number in a:
        hits += 1
 
print(hits)
