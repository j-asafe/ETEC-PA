from tkinter import *
from tkinter import ttk
import random


# Criando a janela principal
root = Tk()
root.title("Gerador de Senhas")

def embaralhar(palavra):
    lista = list(palavra)
    random.shuffle(lista)
    return ''.join(lista)

def resultado():
    palavra1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%¨&*_+£¢¬§'
    palavra_embaralhada = embaralhar(palavra1) 
    senha = (random.sample(palavra_embaralhada, 9))
    finalResult = ''.join(senha)
    textResult.set(finalResult)

# Container
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


#Resultado da senha
textResult = StringVar()
ttk.Label(mainframe, textvariable=textResult).grid(column=2, row=1, sticky=(W, E))

# Botão pra senha
ttk.Button(mainframe, text="Gerar Senha", command=resultado).grid(column=2, row=2, sticky=W)

# para interface
ttk.Label(mainframe, text="Senha Gerada:").grid(column=0, row=1, sticky=E)

# espaçamento entre os widgets
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

#loop principal
root.mainloop()
