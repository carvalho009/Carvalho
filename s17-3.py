participantes = int(input("Digite o número de participantes: "))
tipo_reuniao = input("Digite o tipo de reunião (normal ou executiva): ").strip().lower()

if tipo_reuniao == "executiva" or participantes >= 16:
    print("Sala Grande")
elif participantes >= 16 and tipo_reuniao == 'normal':
        print("Sala Média")
elif participantes >= 6 and participantes <= 15 and tipo_reuniao == 'normal':
    print("Sala Média")
elif participantes <= 5:
    print("Sala Pequena")
