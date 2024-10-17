from tkinter import *  # Importando tudo do módulo tkinter
from tkinter import ttk  # Importando ttk para widgets com melhor aparência

root = Tk()  # Criando a janela principal
root.title("Milhas para KM")  # Configurando o título da janela

def calculate(*args):  # Definindo a função para calcular a conversão
    try:
        value = float(miles.get())  # Obtendo o valor em milhas como float
        # Calculando a conversão de milhas para quilômetros (1 milha = 1.60934 km)
        kilometers.set(int(value * 1.60934 * 10000.0 + 0.5) / 10000.0)
    except ValueError:  # Tratando caso o valor não seja um número válido
        pass

# Criando o container principal (frame)
mainframe = ttk.Frame(root, padding="3 3 12 12")  # Adicionando padding ao frame
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))  # Posicionando o frame na janela

root.columnconfigure(0, weight=1)  # Configurando a coluna para expandir
root.rowconfigure(0, weight=1)  # Configurando a linha para expandir

miles = StringVar()  # Variável para armazenar a entrada de milhas
miles_entry = ttk.Entry(mainframe, width=7, textvariable=miles)  # Criando campo de entrada para milhas
miles_entry.grid(column=2, row=1, sticky=(W, E))  # Posicionando o campo de entrada

kilometers = StringVar()  # Variável para armazenar a conversão em quilômetros
ttk.Label(mainframe, textvariable=kilometers).grid(column=2, row=2, sticky=(W, E))  # Exibindo o resultado em km

ttk.Button(mainframe, text="Calcular", command=calculate).grid(column=3, row=3, sticky=W)  # Botão para calcular

# Criando rótulos de texto
ttk.Label(mainframe, text="Milhas").grid(column=3, row=1, sticky=W)  # Rótulo para 'Milhas'
ttk.Label(mainframe, text="é equivalente a").grid(column=1, row=2, sticky=E)  # Rótulo de texto
ttk.Label(mainframe, text="Quilômetros").grid(column=3, row=2, sticky=W)  # Rótulo para 'Quilômetros'

# Configurando padding para todos os widgets dentro do mainframe
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)  # Adicionando padding aos widgets

miles_entry.focus()  # Colocando o foco no campo de entrada de milhas
root.bind("<Return>", calculate)  # Ligando a tecla Enter à função de cálculo

root.mainloop()  # Iniciando o loop principal da interface gráfica