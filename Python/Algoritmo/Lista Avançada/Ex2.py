'''2. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As
perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a
participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela
deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
"Assassino". Caso contrário, ele será classificado como "Inocente".'''

perg1=str(input('Telefonou para a vítima?:'))
perg2=str(input('Esteve no local do crime?: '))
perg3=str(input('Mora perto da vítima?: '))
perg4=str(input('Devia para a vítima?: '))
perg5=str(input('Já trabalhou com a vítima?: '))
susp=5


if perg1=="N" or perg1=="Não" or perg1=="n":
    susp-=1
elif perg2=="N" or perg2=="Não" or perg2=="n":
    susp-=1
elif perg3=="N" or perg3=="Não" or perg3=="n":
    susp-=1
elif perg4=="N" or perg4=="Não" or perg4=="n":
    susp-=1
elif perg5=="N" or perg5=="Não" or perg5=="n":
    susp-=1

if susp==2:
    print('Suspeita')
elif  susp==3 or susp==4:
    print('Cúmplice')
elif susp==5:
    print('Assasino')
if susp==1 or susp==0:
    print('Inocente')
