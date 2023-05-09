#matrizes em Python

row = []
 
for i in range(8):
    row.append(WHITE_PAWN)
 
#resumido

row = [WHITE_PAWN for i in range(8)]


#lista de 10 elementos

squares = [x ** 2 for x in range(10)]
 
#8 elementos

twos = [2 ** i for i in range(8)]
#O fragmento cria uma matriz de oito elementos que contém as oito primeiras potências de dois (1, 2, 4, 8, 16, 32, 64, 128)
 

#apenas elementos impares da lista

odds = [x for x in squares if x % 2 != 0 ]


#3.7.2 Matrizes bidimensionais

board = []
 
for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)


#Nota:

#a parte interna do loop cria uma linha que consiste em oito elementos (cada um deles igual a EMPTY) e a anexa à lista ao board;
#a parte externa a repete oito vezes;
#no total, a lista board compõe-se de 64 elementos (todos iguais a EMPTY)
 


# mesmo codigo, mas aninhado
board = [[EMPTY for i in range(8)] for j in range(8)]


#criando a matriz

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK


#colocando elementos na matriz

board[4][2] = KNIGHT
board[3][4] = PAWN





#matriz tridimensional

rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
 


 





 


 
