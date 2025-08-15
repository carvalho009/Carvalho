valor_do_pedido = float(input("Digite o valor do pedido: "))
dias_para_entrega = int(input("Digite o dia para entrega: "))

def classificar_pedidos(valor_do_pedido, dias_para_entrega):
    if valor_do_pedido <= 100 or dias_para_entrega > 7:
        print("Entrega Normal")
    elif valor_do_pedido > 100 and valor_do_pedido <= 500 or dias_para_entrega >= 4 and dias_para_entrega <= 7:
        print("Entrega Prioritário")
    elif valor_do_pedido > 500 or dias_para_entrega < 4:
        print("Entrega Urgente")
    else:
        print("Pedido não classificado")

classificar_pedidos(valor_do_pedido, dias_para_entrega)