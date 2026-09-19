# 💧 Sistema de Classificação de Consumo de Água

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github&logoColor=white)
![Ambiente](https://img.shields.io/badge/Foco-Conscientiza%C3%A3o%20Ambiental-green?style=for-the-badge)

## 📋 Sobre o Projeto
Este sistema foi desenvolvido em **Python** para atender à campanha de conscientização ambiental de uma companhia de saneamento fictícia. O objetivo principal é analisar o perfil de consumo de água de diferentes tipos de imóveis (casas, apartamentos e estabelecimentos comerciais) e emitir alertas educativos personalizados para os moradores.

O programa utiliza a estrutura moderna de controle de fluxo **`match-case`** (Structural Pattern Matching) introduzida no Python 3.10, otimizando a coleta de dados de acordo com a regra de negócio de cada imóvel.

---

## 🛠️ Tecnologias Utilizadas
* **Python 3.10+**
* Estrutura de decisão condicional (`if-elif-else`)
* Correspondência de padrões estruturais (`match-case`)

---

## ⚙️ Regras de Negócio Implementadas
* **Imóvel Comercial:** Exibe diretamente a mensagem de tarifa corporativa, sem necessidade de coletar dados de consumo.
* **Imóvel Residencial (Casa/Apartamento):**
  * **Consumo < 10 m³:** Alerta de consumo econômico.
  * **Consumo entre 10 m³ e 25 m³:** Alerta de consumo moderado (padrão residencial).
  * **Consumo > 25 m³:** Alerta de consumo excessivo com recomendação de checagem de vazamentos.

---

## 🚀 Como Executar o Programa

### Pré-requisitos
Certifique-se de ter o **Python 3.10 ou superior** instalado em sua máquina. Você pode verificar a versão rodando:
```bash
python --version
```

### Passo a Passo
1. Copie o código do script Python para um arquivo chamado `main.py`.
2. Abra o terminal ou prompt de comando na pasta onde salvou o arquivo.
3. Execute o comando abaixo:
   ```bash
   python main.py
   ```
4. Interaja com o terminal inserindo o tipo de imóvel e o consumo de água conforme solicitado.

---
Desenvolvido com foco em eficiência e boas práticas de lógica de programação. 🌱
