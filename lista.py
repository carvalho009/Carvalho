while True:
    try:
        fruta = int(input("Coloque um número de 0 a 4: "))
        frutas = ['Banana', 'Maça', 'Uva', 'Manga', 'Abacaxi']
        print(frutas[fruta])
        continua = input("Deseja continuar?[sim, nao]: ").lower()
        if continua == 'nao':
            break
    except IndexError:
        print("Erro de indice")
