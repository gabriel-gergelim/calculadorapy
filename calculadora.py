import tkinter as tk

#Funções
def limpar():
    visor.delete(0, tk.END)
def backspace():
    visor.delete(len(visor.get())-1, tk.END)
def divisao():
    num = visor.get()
    
def somar():
    n1 = 8
def decimal():
    if "." not in visor.get():
        visor.insert(tk.END, ".")

#Numeros

def digitar_0():
    visor.insert(tk.END, "0")
def digitar_1():
    visor.insert(tk.END, "1")
def digitar_2():
    visor.insert(tk.END, "2")
def digitar_3():
    visor.insert(tk.END, "3")
def digitar_4():
    visor.insert(tk.END, "4")
def digitar_5():
    visor.insert(tk.END, "5")
def digitar_6():
    visor.insert(tk.END, "6")
def digitar_7():
    visor.insert(tk.END, "7")
def digitar_8():
    visor.insert(tk.END, "8")
def digitar_9():
    visor.insert(tk.END, "9")

#Janela principal

janela = tk.Tk()
janela.title("Calculadora de aura")
janela.resizable(False, False)


visor = tk.Entry(janela, width=15, justify="center", font=("Arial", 18))
visor.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="we")

#primeira linha de botões

botao_c = tk.Button(janela, text="C", width=6, command=limpar)
botao_c.grid(row=1, column=0, padx=2, pady=2)

botao_backspace = tk.Button(janela, text="⌫", width=6, command=backspace)
botao_backspace.grid(row=1, column=1, padx=2, pady=2)

botao_divisao = tk.Button(janela, text="÷", width=6)
botao_divisao.grid(row=1, column=2, padx=2, pady=2)

botao_multiplicacao = tk.Button(janela, text="X", width=6)
botao_multiplicacao.grid(row=1, column=3, padx=2, pady=2)

#segunda linha de botões

botao_7 = tk.Button(janela, text="7", width=6, command=digitar_7)
botao_7.grid(row=2, column=0, padx=2, pady=2)

botao_8 = tk.Button(janela, text="8", width=6, command=digitar_8)
botao_8.grid(row=2, column=1, padx=2, pady=2)

botao_9 = tk.Button(janela, text="9", width=6, command=digitar_9)
botao_9.grid(row=2, column=2, padx=2, pady=2)

botao_subtracao = tk.Button(janela, text="-", width=6)
botao_subtracao.grid(row=2, column=3, padx=2, pady=2)

#terceira linha de botões

botao_4 = tk.Button(janela, text="4", width=6, command=digitar_4)
botao_4.grid(row=3, column=0, padx=2, pady=2)

botao_5 = tk.Button(janela, text="5", width=6, command=digitar_5)
botao_5.grid(row=3, column=1, padx=2, pady=2)

botao_6 = tk.Button(janela, text="6", width=6, command= digitar_6)
botao_6.grid(row=3, column=2, padx=2, pady=2)

botao_soma = tk.Button(janela, text="+", width=6)
botao_soma.grid(row=3, column=3, padx=2, pady=2)

botao_1 = tk.Button(janela, text="1", width=6, command=digitar_1)
botao_1.grid(row=4, column=0, padx=2, pady=2)

botao_2 = tk.Button(janela, text="2", width=6, command=digitar_2)
botao_2.grid(row=4, column=1, padx=2, pady=2)

botao_3 = tk.Button(janela, text="3", width=6, command=digitar_3)
botao_3.grid(row=4, column=2, padx=2, pady=2)

botao_0 = tk.Button(janela, text="0", width=6, command=digitar_0)
botao_0.grid(row=5, column=0, padx=2, pady=2, columnspan=2, sticky="we")

botao_calcular = tk.Button(janela, text="=", width=6)
botao_calcular.grid(row=4, column=3, padx=2, pady=2, rowspan=2, sticky="ns")

botao_decimal = tk.Button(janela, text=".", width=6)
botao_decimal.grid(row=5, column=2, padx=2, pady=2)








janela.mainloop()