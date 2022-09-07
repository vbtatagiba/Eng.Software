""" 7.	A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo."""
n=int(input('Digite o a posição do termo: '))
enersimotermo = 1
penultimo = 1
contador = 1
print(enersimotermo)
print(penultimo)
while contador <= n:
        termo = enersimotermo + penultimo
        penultimo = enersimotermo
        enersimotermo = termo
        contador += 1
        print(termo)