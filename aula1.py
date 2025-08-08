cargo = input("Digite o seu cargo: ")
dia_da_semana = input("Digite o dia da semana: ")

if cargo == 'Gerente':
        print("Acesso Liberado todos os dias")
elif cargo == 'Analista' or cargo == "Estagiário":
    if dia_da_semana in ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]:
        print(f"Acesso Liberado no dia {dia_da_semana}")
    else:
        ("Acesso Negado, Você só pode acessar de Segunda a Sexta")
else:
    print("Acesso Negado. Cargo não reconhecido.")