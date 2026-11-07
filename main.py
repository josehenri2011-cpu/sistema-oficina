import persistencia
import cadastros


cadastros_clientes = persistencia.carregar_json_clientes()
cadastros_veiculos = persistencia.carregar_json_veiculos()
catalago = persistencia.carregar_json_catalogo()
Solicitaçoes_serviço=persistencia.carregar_Json_Solicitaçoes_serviço()
id = 0
id_ordens=0
while True:
    print(cadastros_clientes)
    print("""
    ===== SISTEMA DE GESTÃO DE OFICINA =====

    1 - Cadastrar cliente
    2 - Cadastrar serviço
    3 - Cadastrar serviço

    ========================================
    """)

    opçao = int(input("Escolha uma opção: "))


    if opçao == 1:
        id = cadastros.criar_cliente(cadastros_clientes, id)
        persistencia.salvar_json(cadastros_clientes,cadastros_veiculos,catalago,Solicitaçoes_serviço)
    elif opçao == 2:
        cadastros.registro_serviços(catalago)
        
    elif opçao == 3:
        cadastros.registro_serviços(catalago)
        

    # Demais opções do menu serão trabalhadas depois