from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Milhas Para Quilômetros")

def calculate(*args):
    try:
        value = float(milhas.get())
        quilometros.set(value * 1.60934)  # Conversão de milhas para quilômetros
    except ValueError:
        pass

# Criando o container
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Variáveis
milhas = StringVar()  # Variável para armazenar os dados em milhas
quilometros = StringVar()  # Variável para guardar os quilômetros

# <input>
milhas_entry = ttk.Entry(mainframe, width=7, textvariable=milhas)
milhas_entry.grid(column=2, row=1, sticky=(W, E))

# Label para mostrar o resultado em quilômetros
ttk.Label(mainframe, textvariable=quilometros).grid(column=2, row=2, sticky=(W, E))

# Botão calcular
ttk.Button(mainframe, text="Calcular", command=calculate).grid(column=3, row=3, sticky=W)

# <p>
ttk.Label(mainframe, text="milhas").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="é equivalente a").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="quilômetros").grid(column=3, row=2, sticky=W)

# Configuração de padding
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
milhas_entry.focus()

# Liga a tecla Enter à função de cálculo
root.bind("<Return>", calculate)

root.mainloop()
