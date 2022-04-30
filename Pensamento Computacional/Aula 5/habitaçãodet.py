"""5.	Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação"""
a =int(input('Insira sua população1: '))
b =int (input('Insira sua população2: '))
cres1=float(input('Insira seu crescimento1: '))
cres2=float(input('Insira seu crescimento2: '))
ano = 0

while a <= b:
	a += a * cres1
	b += b * cres2
	ano += 1

print ( "A ultrapassa ou iguala a B em %d anos" %ano )