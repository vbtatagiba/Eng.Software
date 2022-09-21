# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do
# atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa
# que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe
# o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado
# o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
# 6. Atleta: Rodrigo Curvêllo
# 7.
# 8. Primeiro Salto: 6.5 m
# 9. Segundo Salto: 6.1 m
# 10. Terceiro Salto: 6.2 m
# 11. Quarto Salto: 5.4 m
# 12. Quinto Salto: 5.3 m
# 13.
# 14. Resultado final:
# 15. Atleta: Rodrigo Curvêllo
# 16. Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5.9 m

cont = 0
names = []
saltos = []

while True:
    nome = input('Digite o nome do atleta: ')
    names.append(nome)
    if nome == "":
        print('Digite um nome válido!!! ')
    else:
        break

while True:
    salto = float(input('Digite a distância dos saltos em ordem: '))
    saltos.append(salto)
    cont += 1
    if cont == 5:
        break

media = sum(saltos)/5
print('Resultado:', names[0])
print( 'Salto 1:',  saltos[0],'m')
print('Salto 2:', saltos[1],'m')
print('Salto 3:', saltos[2],'m')
print('Salto 4:', saltos[3],'m')
print('Salto 5:', saltos[4],'m')
print('Média final do atleta;',round(media, 2))


