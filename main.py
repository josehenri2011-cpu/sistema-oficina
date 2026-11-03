import persistencia
import cadastros


cadastros_clientes = persistencia.carregar_json_clientes()
cadastros_veiculos = persistencia.carregar_json_veiculos()
catalago = persistencia.carregar_json_catalogo()
Solicitaçoes_serviço=persistencia.carregar_Json_Solicitaçoes_serviço()

id = 0
id_ordens=0
while True:
    opçao = int(input("Digite: "))

    if opçao == 1:
        id = cadastros.criar_cliente(cadastros_clientes, id)
        print(cadastros_clientes)
    elif opçao == 2:
        cadastros.registro_serviços(catalago)
        
    elif opçao == 3:
        cadastros.registro_serviços(catalago)
        

    # Demais opções do menu serão trabalhadas depois