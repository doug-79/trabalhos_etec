# ⚡ Calculadora de Consumo Energético em Python

> Projeto desenvolvido para as aulas de programação da ETEC, aplicando lógica de programação, manipulação de variáveis e cálculos matemáticos em Python. 🐍

---

## 📋 Sobre o Projeto
Este sistema em Python tem como objetivo calcular o consumo mensal de energia (em kWh/mês) de qualquer aparelho elétrico. O usuário informa o nome do aparelho, a sua potência em Watts e o tempo médio de uso diário, e o programa faz o cálculo considerando um mês de 30 dias.

---

## 🛠️ Tecnologias Utilizadas
O projeto foi desenvolvido utilizando as seguintes tecnologias e ferramentas:

<p>
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  <img src="https://img.shields.io/badge/Linux_Mint-87CEEB?style=for-the-badge&logo=linuxmint&logoColor=white" alt="Linux Mint">
</p>

---

## 🧮 Fórmula Utilizada
O cálculo do consumo mensal em Quilowatts-hora (kWh/mês) é feito através da seguinte lógica:

$$\text{Consumo Mensal (kWh)} = \frac{\text{Potência (W)} \times \text{Tempo Diário (horas)} \times 30}{1000}$$

* **Aparelho:** Nome do dispositivo inserido pelo usuário.
* **Potência (W):** Potência do aparelho em Watts.
* **Tempo de uso:** Horas que o aparelho fica ligado por dia.
* **30:** Quantidade de dias do mês considerada no cálculo.
* **1000:** Fator de conversão de Watts para Quilowatts.

---

## 💻 Código Fonte (`app.py`)
```python
aparelho = input("Digite o nome do aparelho: ") 
potencia = float(input("Digite a potência do aparelho em watts (W): "))
tempo_uso = float(input("Digite o tempo de uso diário do aparelho em horas: "))
consumoMensal = (potencia * tempo_uso * 30) / 1000
print(f"O consumo mensal estimado do aparelho {aparelho} é de: {consumoMensal} kWh/mês")