
#A empresa de marketing TudoWeb precisa realizar uma pesquisa de opinião com seus clientes para saber o grau de satisfação no atendimento. Sua tarefa é:

#Desenvolver um programa em Python utilizando a estrutura de repetição para coletar e exibir o retorno de uma pesquisa de atendimento ao cliente.
#O programa deve solicitar a digitação do nome, idade e opinião do entrevistado sobre o atendimento prestado, sendo:
#1: EXCELENTE
#2: BOM
#3: RUIM
#A pesquisa deve ser feita com 50 entrevistados.
#Ao final, o programa deverá exibir na tela:
#a) Quantidade de respostas “EXCELENTE”
#b) Quantidade de respostas “RUIM”
#Utilize estruturas de decisão para verificar a opinião do entrevistado.
#Realize testes com 10 entrevistados para validar o funcionamento do programa.
#Compartilhe o projeto completo junto com os prints de tela do código e da execução no seu repositório Github, informe o link do repositório no ambiente virtual.

#variáveis zeradas
excelente = 0
bom = 0
ruim = 0
#laço de repetição    
for i in range (50):
   
    print(i+1,  " - Solicitamos aos usuários que respondam a seguinte pesquisa: \n") 
    nome = str(input("Digite seu nome: "))
    idade = int(input("digite sua idade: "))
    atendimento = int(input("Digite (1) para o atendimento foi EXCELENTE - (2) para BOM - (3) para RUIM: " ))
    
    if atendimento == 1:
        excelente += 1
    elif atendimento == 2:
        bom += 1
    elif atendimento == 3:
        ruim += 1
           
    print("\n\n") #pular linhas

#Resultado da pesquisa
print("Segundo a pesquisa, os usuários relataram os seguinte paramentros:\n ")
print(f"EXCELENTE = {excelente}\n")     

print(f"BOM = {bom}\n")     
    
print(f"RUIM = {ruim}\n")     