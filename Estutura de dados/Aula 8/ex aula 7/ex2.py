'''Escreva uma função que calcule o número de dias necessários para concluir um projeto, sabendo que o projeto tem n tarefas e cada tarefa leva d dias para ser concluída.'''
tempotarefa=float(input('Insira quanto dias leva para realizar uma tarefa? '))
quantastarefas=int(input('Quantas tarefas irão realizar? '))

total=tempotarefa*quantastarefas
print(f'Serão necessarios {total} dias para realizar todas as tarefas')