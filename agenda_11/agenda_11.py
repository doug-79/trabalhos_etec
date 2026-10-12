#importação da biblioteca colorama, estou usando o mint, não é necessário importar o init e nem chamar
from colorama import Fore, Style

#função com os sinais de alertas com retorno
def aviso(nivel):
    lista_sinais = [ Fore.RED + "Nível 1 - Muito baixo (CRITICO!)", Fore.YELLOW + "Nível 2 - Baixo", 
                    Fore.GREEN + "Nível 3 - Médio", Fore.CYAN + "Nível 4 - Alto", Fore.BLUE + "Nível 5 - Muito Alto(ALERTA!)"  ]
    return lista_sinais[nivel]

#mostrar cada aviso
print(aviso(0))
print(aviso(1))
print(aviso(2))
print(aviso(3))
print(aviso(4))
print("Atenção")

#desativando as cores do terminal
print(Style.RESET_ALL+"Fim do aviso")


    

