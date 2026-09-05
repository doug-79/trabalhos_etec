
""" Você foi contratado para desenvolver um programa que implemente um sistema de desconto progressivo para uma loja online. Este sistema deve aplicar descontos de acordo com o valor total da compra. As regras de desconto são as seguintes:

Se o valor total da compra for menor do que R$ 200,00, o cliente recebe um desconto de 5%.
Se o valor total da compra for maior ou igual a R$ 200,00 e menor que R$ 300,00, o cliente recebe um desconto de 10%.
Se o valor total da compra for maior ou igual a R$ 300,00, o cliente recebe um desconto de 15%."""


compra = float(input("Digite o valor da compra: ")) #digita o valor da compra
      
#condições para compra usando if/ elif/else e printando o resultado formatado
if compra < 200:
    print(f"Valor total com desconto de 5% {compra * 0.95 :.2f}")
elif compra < 300:
    print(f"Valor total com desconto de 10% {compra * 0.9 :.2f}")
else:
    print(f"Valor total com desconto de 15% {compra * 0.85 :.2f}")
                


                
        

        
    
