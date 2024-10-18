from tkinter import * #importando tudo TK. O "*" significa 'all', então, de tk ele está importando tudo;
from tkinter import ttk #Atualização visual

inicio = Tk() #Criando janela. Sendo root um nome qualquer e 'Tk()' a fução pra chamar o Tkinter;
inicio.title("Calculadora de IMC") #Configurando o título do app;

imc_resultas = StringVar()
def calculate(*args): #A função para fazer a conta de pés para metros.
    try:
        alturas = float(altura.get()) #Aqui ele está puxando as informações do feet com o get ('pegar') e definindo o resultado como float;
        pesos = float(peso.get())
        imc=(float(pesos/alturas**2))
        imc_resultas.set('{:.2f}'.format(imc))
    except ValueError:
        pass #Esse 'pass' é para ignorar quando a conversão não der certo;

#Criando o nosso container <div>
mainframe = ttk.Frame(inicio, padding = "5 5 12 12") #Defininido os parâmetros do contâiner, sendo 3 em cima e em baixo e 12 dos lados;
mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) # O sticky está expandindo nas direções apresentadas;
inicio.columnconfigure(0, weight=2) # Permitindo que a coluna 0 do root se expanda.
inicio.rowconfigure(0, weight=2) # Permitindo que a linha 0 do root se expanda.

altura = StringVar() #Criação de uma variável para armazenar o dados pés (como uma string variável);

altura_entry = ttk.Entry(mainframe, width=7, textvariable=altura)  # Definindo um Entry com largura de 7 e ligando à variável 'feet';
altura_entry.grid(column=2, row=1, sticky=(W,E)) #Colocando o entry na coluna 2 linha 1;

peso = StringVar() #Criação de uma variável para guardar os metros;
peso_entry = ttk.Entry(mainframe, width=7, textvariable=peso)
peso_entry.grid(column=2, row=2, sticky=(W,E))

#ttk.Label(mainframe, textvariable=peso).grid(column=1, row=2, sticky=(W,E)) #Cria um espaço para mostrar o resultado metros;

ttk.Button(mainframe, text="Calcular", command=calculate).grid(column=4, row=2, sticky=W) #Cria um botão com o nome calcular que executa a função (calculate);
ttk.Label(mainframe, textvariable=imc_resultas).grid(column=3, row=2, sticky=(W,E)) #Cria um espaço para mostrar o resultado metros;

#<p>
ttk.Label(mainframe, text="Altura:").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Peso:").grid(column=1, row=2, sticky=E)
#ttk.Label(mainframe, text="Metros").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
altura_entry.focus()

inicio.bind("<Return>", calculate) # Liga a tecla Enter à função de cálculo;


inicio.mainloop() #Gerando loop para rederização interminente