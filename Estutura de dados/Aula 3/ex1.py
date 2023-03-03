linha=6
colunas=5
cont=0
matriz=["x",0,0,0,"x",0,"x",0,"x",0,0,0,"x",0,0,0,"x",0,"x",0,"x",0,"x",0,"x",0,"x",0,"x",0]
pos=[]

for i in range (len(matriz)):
    if matriz[i] == "x":
        cont += 1 
        pos.append(i)
    else:
        pass
print('O Numero de x são',cont)
print('As posição são',pos)