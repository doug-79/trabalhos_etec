aparelho = input("Digite o nome do aparelho: ") 
potencia = float(input("Digite a potência do aparelho em watts (W): "))
tempo_uso = float(input("Digite o tempo de uso diário do aparelho em horas: "))
consumoMensal = (potencia * tempo_uso * 30) / 1000
print(f"O consumo mensal estimado do aparelho {aparelho} é de: {consumoMensal} kWh/mês")