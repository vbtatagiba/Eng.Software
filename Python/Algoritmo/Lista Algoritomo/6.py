'''6. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área
para o usuário.'''
lado=float(input('Insira o tamanho do lado:'))
area=lado**2
dobro=area*2
print ('A Área do quadro é:',area)

perg=str(input('''Deseja ver o dobro dessa área Digite 'Y' para sim e 'N' para não:'''))

if perg=='Y' or perg=='y':
    print('O dobro da área do quadrado é',dobro)
else:
    print('Obrigado Simulação encerrada')