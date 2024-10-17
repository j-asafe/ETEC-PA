from tkinter import *  # Importando tudo do módulo tkinter
from tkinter import ttk  # Importando ttk para widgets com melhor aparência

root = Tk()  # Criando a janela principal
root.title("Cálculo de IMC")  # Configurando o título da janela

def calculate(*args):  # Definindo a função para calcular o IMC
    try:
        weight = float(weight_entry.get())  # Obtendo o peso como float
        height = float(height_entry.get())  # Obtendo a altura como float

        # Calculando o IMC (peso / altura^2)
        imc = weight / (height ** 2)
        imc_result.set(f"{imc:.2f}")  # Armazenando o resultado formatado com 2 casas decimais
    except ValueError:  # Tratando caso o valor não seja um número válido
        imc_result.set("")  # Limpa o resultado se houver erro

# Criando o container principal (frame)
mainframe = ttk.Frame(root, padding="3 3 12 12")  # Adicionando padding ao frame
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))  # Posicionando o frame na janela

root.columnconfigure(0, weight=1)  # Configurando a coluna para expandir
root.rowconfigure(0, weight=1)  # Configurando a linha para expandir

# Variáveis para armazenar a entrada de peso e altura
weight_entry = StringVar()
height_entry = StringVar()
imc_result = StringVar()

# Criando campos de entrada para peso e altura
ttk.Label(mainframe, text="Altura (m)").grid(column=1, row=1, sticky=W)  # Rótulo para 'Altura'
height_entry_widget = ttk.Entry(mainframe, width=10, textvariable=height_entry)
height_entry_widget.grid(column=1, row=2, sticky=(W, E))  # Campo de entrada para altura

ttk.Label(mainframe, text="Peso (kg)").grid(column=1, row=3, sticky=W)  # Rótulo para 'Peso'
weight_entry_widget = ttk.Entry(mainframe, width=10, textvariable=weight_entry)
weight_entry_widget.grid(column=1, row=4, sticky=(W, E))  # Campo de entrada para peso

# Exibindo o resultado do IMC
ttk.Label(mainframe, text="Resultado").grid(column=2, row=2, sticky=W)  # Rótulo para 'Resultado'
ttk.Label(mainframe, textvariable=imc_result).grid(column=2, row=3, sticky=(W, E))  # Resultado do IMC

# Botão para calcular o IMC
ttk.Button(mainframe, text="Calcular", command=calculate).grid(column=3, row=2, rowspan=2, sticky=(W, E))

# Configurando padding para todos os widgets dentro do mainframe
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)  # Adicionando padding aos widgets

weight_entry_widget.focus()  # Colocando o foco no campo de entrada de peso
root.bind("<Return>", calculate)  # Ligando a tecla Enter à função de cálculo

root.mainloop()  # Iniciando o loop principal da interface gráfica