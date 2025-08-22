link_3 = int(input("Coloque um número de 1 a 1000: "))
while link_3 < 0 or link_3 > 1000:
    link_3 = int(input("Coloque um número de 1 a 1000: "))
link_2 = link_3 * 2
link_1 = link_2 * 2
soma = (link_1 * 2)
print(f"O número de cliques no terceiro link foi: {link_3}")
print(f"O número de cliques no segundo link foi: {link_2}")
print(f"O número de cliques no primeiro link foi: {link_1}")
print(f"A soma total de cliques é: {soma}")
    

