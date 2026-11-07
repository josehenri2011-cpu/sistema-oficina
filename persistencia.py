import json
from cadastros import Clientes

def salvar_json(cadastros_clientes,cadastros_veiculos,catalago,Solicitaçoes_serviço):
   dados_para_salvar={}
   for cpf, dados in cadastros_clientes.items():
       
       dados_cliente=dados["cliente"].__dict__
       id=dados["ID"]

   
       dados_para_salvar[cpf]={
        "ID":id,
        "cliente": dados_cliente
         }
    
   with open("dados_para_salvar.json", "w") as arquivo:
        json.dump(dados_para_salvar,arquivo,ensure_ascii=False, indent=4)
        
   with open("cadastros_veiculos.json","w") as arquivo:
        json.dump(cadastros_veiculos, arquivo, ensure_ascii=False, indent=4)
   with open("catalogo.json","w") as arquivo:
        json.dump(catalago, arquivo, ensure_ascii=False, indent=4)
   with open("Solicitaçoes_serviço.json","w") as arquivo:
        json.dump(Solicitaçoes_serviço, arquivo, ensure_ascii=False, indent=4)

def carregar_json_clientes():
    dic_temp={
        
    }
    try:
        with open("dados_para_salvar.json", "r") as arquivo:
            clientes=json.load(arquivo)
            for cpf, dados in clientes.items():
               atributos = dados["cliente"]
               id = dados["ID"]
               
               
               cliente = Clientes(
               atributos["nome"],
               atributos["cpf"],
               atributos["telefone"]
                                     )
            
               dic_temp[cpf]={
                "cliente":cliente,
                "ID":id }
            
        
        return dic_temp
    
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