xhat_list = [1, 2, 3, 4, 5] # Esta é uma lista atual de números ocultos no hat.

numero = int(input("informe o novo numero: "))
hat_list[1] = numero
del hat_list[2]

print ("Comprimento da nova lista:", len (hat_list))

print (hat_list) 
