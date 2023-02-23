frutas = ['manga', 'banana', 'laranja', 'uva', 'abacaxi']


fruta = input("Insira uma fruta: ")

if fruta.lower() in frutas:
    print('-='*30)
    print(f"A fruta {fruta} está na lista!")
    print('-='*30)
else:
    print('-='*30)
    print(f"A fruta {fruta} não está na lista.")
    print('-='*30)