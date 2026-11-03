import json

def salvar_json(cadastros_clientes,cadastros_veiculos,catalago,Solicitaçoes_serviço):
    with open("cadastros_clientes.json", "w") as arquivo:
        json.dump(cadastros_clientes, arquivo,ensure_ascii=False, indent=4)
    with open("cadastros_veiculos.json","w") as arquivo:
        json.dump(cadastros_veiculos, arquivo, ensure_ascii=False, indent=4)
    with open("catalogo.json","w") as arquivo:
        json.dump(catalago, arquivo, ensure_ascii=False, indent=4)
    with open("Solicitaçoes_serviço.json","w") as arquivo:
        json.dump(Solicitaçoes_serviço, arquivo, ensure_ascii=False, indent=4)

def carregar_json_clientes():
    try:
        with open("cadastros_clientes.json", "r") as arquivo:
            clientes=json.load(arquivo)
            return clientes
    except FileNotFoundError:
        return {}
def carregar_json_veiculos():
    try:
        with open("cadastros_veiculos.json", "r") as arquivo:
            veiculos=json.load(arquivo)
            return veiculos
    except FileNotFoundError:
        return []
def carregar_json_catalogo():
    try:
        with open("catalogo.json", "r") as arquivo:
            catalogo=json.load(arquivo)
            return catalogo
    except FileNotFoundError:
        return []
def carregar_Json_Solicitaçoes_serviço():
    try:
        with open("Solicitaçoes_serviço.json","r") as arquivo:
            solicitaçoes=json.load(arquivo)
            return solicitaçoes
        
    except FileNotFoundError:
        return {}