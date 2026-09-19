#A companhia de saneamento da sua cidade lançou uma campanha de conscientização ambiental e precisa de um script em Python para classificar o perfil de consumo dos imóveis e emitir alertas educativos aos moradores.

#Solicite ao usuário o tipo de imóvel (opções esperadas: "comercial", "casa" ou "apartamento").
#Solicite o consumo mensal de água em metros cúbicos (𝑚3 ) (número decimal).
#Implemente a classificação de acordo com as seguintes regras de negócio: o Se o tipo for "comercial", exibir:
#"Tarifa comercial aplicada – consulte o plano corporativo."
#Se o tipo for "apartamento" e o consumo for menor que 10 𝑚3 , exibir: "Consumo econômico – excelente controle de água!"
#Se o tipo for "apartamento" ou for "casa" com consumo de até 25 𝑚3 , exibir: "Consumo moderado – dentro do padrão residencial."
#Em qualquer outro caso (consumo acima do limite residencial), exibir: "Consumo excessivo – adote medidas de economia e verifique vazamentos.

# o usuario vai digitar qual o tipo de imovel
imovel = int(input("Digite o tipo de imóvel (1) - casa (2) - apartamento (3) comercial:  "))
             
match imovel:
    case 1 | 2: #como casa e partamento sao resirenciais, ficaram no mesmo case
       consumo = float(input("Digite o consumo de água: "))
       if consumo < 10:
           print("Consumo econômico – excelente controle de água!")
       
       elif consumo == 10 or consumo <= 25:
           print("Consumo moderado – dentro do padrão residencial ")
           
       else:
          print("Consumo excessivo – adote medidas de economia e verifique vazamentos!")
                      
    case 3: #como não foi pedido os paramentros de consumo vai aparecer somente a mensagem
        print("Tarifa comercial aplicada – consulte o plano corporativo.")
             
    case _: #se caso o usuario digitar outra coisa vai parar aqui
        print("Opção inválida! Escolha apenas 1, 2 ou 3.")
            
             
             
             

