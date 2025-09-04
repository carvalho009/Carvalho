N = int(input("Coloque um número de 1 a 1000: "))
while N <1 or N >1000:
    N = int(input("Coloque um número de 1 a 1000: "))
for i in range(1, N + 1):
    print(i, i**2, i**3)
    print(i, i**2 + 1, i**3 + 1)
