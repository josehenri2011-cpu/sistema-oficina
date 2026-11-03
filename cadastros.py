

class Clientes():
    def __init__(self,nome,cpf, telefone):
        self.nome=nome
        self.cpf=cpf
        self.telefone=telefone
        

class Veiculo:
    def __init__(self, placa: str, modelo: str, proprietario: str):
        self.placa = placa
        self.modelo = modelo
        self.proprietario = proprietario





def validar_placa():
    """Valida se a placa tem o formato básico correto (ex: 7 caracteres)."""
    while True:
        placa=input("Insira a placa do veículo (ex: ABC1234 ou ABC1D23): ").strip()
        placa = placa.strip()
        
        if len(placa) != 7:
            print("❌ Erro: A placa deve ter exatamente 7 caracteres (ex: ABC1234 ou ABC1D23).")
        
        else:
            return placa
            



def placa_ja_cadastrada(placa,cadastros_veiculos):
    """Verifica se a placa já existe no dicionário."""
    if placa in cadastros_veiculos:
        return True
    return False


# --- FUNÇÃO DE CADASTRO (Focada apenas no fluxo) ---
def criar_veiculo(cadastros_veiculos):
    print("\n--- NOVO CADASTRO DE VEÍCULO ---")
    
    # Validações aplicadas de forma limpa
    while True:
        placa=validar_placa()
        
        if placa_ja_cadastrada(placa):
            print(f"❌ Erro: Já existe um veículo cadastrado com a placa {placa}.")
        else:
            break
            

    
    modelo = input("Digite o modelo do veículo: ")
    if not modelo:
        print("❌ Erro: O modelo não pode ficar vazio.")
        return

    proprietario = input("Digite o nome do proprietário: ").strip()
    if not proprietario:
        print("❌ Erro: O proprietário não pode ficar vazio.")
        return

    # Se passou por tudo, cria o objeto
    novo_veiculo = Veiculo(placa=placa, modelo=modelo, proprietario=proprietario)
    cadastros_veiculos[placa] = novo_veiculo
    print(f"✅ Veículo '{modelo}' cadastrado com sucesso!")


def criar_cliente(cadastros_clientes,id):
    id +=1
    nome=input("Digite o nome do cliente: ")
    while True:
       cpf=input("Digite o CPF do cliente: ")
       cpf = cpf.strip()

    
       if not validar_cpf(cpf):
           continue
        
       if cpf in cadastros_clientes:
           print("❌ Erro: CPF já cadastrado. Tente novamente.")
           continue
       break
    
    telefone=input("Digite o telefone do cliente: ")
    
    cliente= Clientes(nome,cpf,telefone)
    cadastros_clientes[cpf]={
        "ID":id,
        "cliente":cliente
    }
    return id
    

def validar_cpf(cpf):
    """Valida se o CPF tem o formato básico correto (ex: 11 dígitos)."""
    if len(cpf) != 11 or not cpf.isdigit():
        print("❌ Erro: O CPF deve ter exatamente 11 dígitos numéricos.")
        return False
    return True


def registro_serviços(catalago):
    serviço=input("Digite o serviço: ")
    preço=float(input("Digite o preço do serviço: "))
    novo_serviço={
        "serviço":serviço,
        "preço":preço
        }
    catalago.append(novo_serviço)    
    
 
def ordem_serviço(id_ordens,Solicitaçoes_serviço):
    id_ordens+=1
    placa=input("insira a placa do veiculo")
    serviço=input("quais serviço deseja solicitar? ")   
    
            
    Solicitaçoes_serviço[id_ordens]={
                "placa":placa,
                "serviço":[serviço]
            }
    
    
    while True:
        resposta=input("Deseja solicitar outro serviço? (s/n): ").strip().lower()
        if resposta=="sim":
            pass
        elif resposta=="nao":
           return id_ordens



