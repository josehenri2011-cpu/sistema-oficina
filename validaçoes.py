
                    
                
def validar_placa(cadastros):
    placa=input("insira a placa:")
    for dados in cadastros:
        if dados["placa"]==placa:
           print("placa ja registrada")
       
            
    