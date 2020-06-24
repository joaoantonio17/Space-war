import random
# Maneira que eu encontrei de eliminar lasers e aliens após sairem da tela
# Detecta quais estão fora do jogo, encontra a posição dele na lisa
# e depois deleta
A = [12, 12, 13, 150]
print(A)
Contador = -1
for i in A:
    Contador += 1
    if i > 100:
        del A[Contador]
print(A)