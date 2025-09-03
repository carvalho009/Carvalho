import random
quant_intervalos = int(input("Coloque a quantidade de intervalos de 1 a 1000: "))
while quant_intervalos < 1 or quant_intervalos > 1000:
    quant_intervalos = int(input("Coloque a quantidade de intervalos de 1 a 1000: "))
for i in range(1, quant_intervalos+1):
    tempo_t = random.randint(1, 100)
    velocidade_v = random.randint(1, 120)
    print(f"intervalo{i}| tempo_t {tempo_t} velocidade_v{velocidade_v} distancia{tempo_t*velocidade_v}")
distancia = tempo_t * velocidade_v
total_percorrido =+ distancia
print(f"O Km total percorrido é: {total_percorrido} ")