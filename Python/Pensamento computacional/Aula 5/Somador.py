#somador
contador=0
somador=0
while contador < 5 :
    contador= contador+1
    valor= float(input('Digite o '+str(contador)+ ' valor:'))
    somador=somador+ valor
    print('Soma=',somador)