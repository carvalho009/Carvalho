while True:
    fruta = int(input("Coloque um número de 0 a 5: "))
    frutas = ['Banana', 'Maça', 'Uva', 'Manga', 'Abacaxi']
    print(frutas[fruta])
    continua = input("Deseja continuar?[sim, nao]: ").lower()
    if continua == 'nao':
        break
