# Importa a biblioteca tkinter com o apelido tk.
# Ela permite criar janelas e componentes de interface gráfica.
import tkinter as tk

# Importa messagebox para exibir caixas de diálogo,
# como alertas e mensagens de informação.
from tkinter import messagebox

# Armazena os clientes cadastrados durante a execução.
clientes = []

# ---------------- FUNÇÃO LIMPAR ----------------
# Define a função que limpa os campos do formulário.
def limpar():
    # Apaga todo o conteúdo de cada campo.
    # 0 indica o início do texto e tk.END indica o final.
    entrada_nome.delete(0, tk.END)
    entrada_cpf.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_cidade.delete(0, tk.END)

    # Coloca o cursor no campo nome para iniciar um novo preenchimento.
    entrada_nome.focus()


# ---------------- FUNÇÃO SALVAR ----------------
# Define a função que será executada ao clicar no botão Salvar.
def salvar():
    # Obtém os textos digitados em cada campo.
    nome = entrada_nome.get()
    cpf = entrada_cpf.get()
    telefone = entrada_telefone.get()
    email = entrada_email.get()
    cidade = entrada_cidade.get()

    # Verifica se o nome está vazio.
    if nome == "":
        # Exibe um alerta solicitando o nome.
        messagebox.showwarning(
            "Atenção",           # Título da mensagem.
            "Informe o nome."    # Texto da mensagem.
        )
        # Encerra a função, impedindo as próximas verificações.
        return

    # Verifica se o CPF está vazio.
    if cpf == "":
        # Exibe um alerta solicitando o CPF.
        messagebox.showwarning(
            "Atenção",           # Título da mensagem.
            "Informe o CPF."     # Texto da mensagem.
        )
        # Encerra a função.
        return

    # Cria um dicionário para representar o cliente.
    cliente = {
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone,
        "email": email,
        "cidade": cidade
    }

    # Adiciona o dicionário do cliente à lista de clientes.
    clientes.append(cliente)

    # Insere o nome do cliente cadastrado no final da Listbox na interface.
    lista_clientes.insert(
        tk.END,
        nome
    )

    # Exibe a mensagem de confirmação após o cadastro.
    messagebox.showinfo(
        "Sucesso",
        "Cliente cadastrado com sucesso!"
    )

    # Limpa os campos do formulário após salvar.
    limpar()


# ---------------- JANELA PRINCIPAL ----------------
# Cria a janela principal do programa.
janela = tk.Tk()

# Define o texto exibido na barra de título da janela.
janela.title("Cadastro de Clientes")

# Define a largura de 550 pixels e a altura de 500 pixels.
janela.geometry("550x500")


# ---------------- TÍTULO ----------------
# Cria um Label: componente que exibe um texto na interface.
titulo = tk.Label(
    janela,                      # Janela à qual o componente pertence.
    text="CADASTRO DE CLIENTES", # Texto exibido no componente.
    font=("Arial", 16, "bold")   # Fonte Arial, tamanho 16, em negrito.
)

# Posiciona o título usando uma grade de linhas e colunas.
# A contagem das linhas e colunas começa em zero.
titulo.grid(
    row=0,          # Posiciona na primeira linha.
    column=0,       # Começa na primeira coluna.
    columnspan=2,   # Faz o título ocupar o espaço de duas colunas.
    pady=20         # Adiciona 20 pixels de espaço acima e abaixo.
)


# ---------------- CAMPOS ----------------

# --- NOME ---
# Cria o rótulo "Nome:" e o posiciona na grade.
tk.Label(
    janela,         # Janela à qual o rótulo pertence.
    text="Nome:"    # Texto exibido no rótulo.
).grid(
    row=1,          # Segunda linha.
    column=0,       # Primeira coluna.
    padx=10,        # Espaço de 10 pixels à esquerda e à direita.
    pady=5          # Espaço de 5 pixels acima e abaixo.
)

# Cria um Entry: campo para o usuário digitar uma linha de texto.
entrada_nome = tk.Entry(
    janela,         # Janela à qual o campo pertence.
    width=40        # Largura aproximada em caracteres, não em pixels.
)

# Posiciona o campo de nome ao lado do rótulo.
entrada_nome.grid(
    row=1,          # Mesma linha do rótulo "Nome:".
    column=1,       # Segunda coluna.
    padx=10,        # Espaçamento horizontal externo.
    pady=5          # Espaçamento vertical externo.
)

# --- CPF ---
# Cria e posiciona o rótulo "CPF:".
tk.Label(
    janela,         # Janela à qual o rótulo pertence.
    text="CPF:"     # Texto exibido no rótulo.
).grid(
    row=2,          # Terceira linha.
    column=0,       # Primeira coluna.
    padx=10,        # Espaçamento horizontal externo.
    pady=5          # Espaçamento vertical externo.
)

# Cria o campo de digitação do CPF.
# Neste código, o campo aceita texto sem validar o formato do CPF.
entrada_cpf = tk.Entry(
    janela,         # Janela à qual o campo pertence.
    width=40        # Largura aproximada em caracteres.
)

# Posiciona o campo de CPF ao lado do rótulo.
entrada_cpf.grid(
    row=2,          # Mesma linha do rótulo "CPF:".
    column=1,       # Segunda coluna.
    padx=10,        # Espaçamento horizontal externo.
    pady=5          # Espaçamento vertical externo.
)

# --- TELEFONE ---
# Cria e posiciona o rótulo "Telefone:".
tk.Label(
    janela,          # Janela à qual o rótulo pertence.
    text="Telefone:" # Texto exibido no rótulo.
).grid(
    row=3,           # Quarta linha.
    column=0,        # Primeira coluna.
    padx=10,         # Espaçamento horizontal externo.
    pady=5           # Espaçamento vertical externo.
)

# Cria o campo de digitação do telefone.
entrada_telefone = tk.Entry(
    janela,          # Janela à qual o campo pertence.
    width=40         # Largura aproximada em caracteres.
)

# Posiciona o campo de telefone ao lado do rótulo.
entrada_telefone.grid(
    row=3,           # Mesma linha do rótulo "Telefone:".
    column=1,        # Segunda coluna.
    padx=10,         # Espaçamento horizontal externo.
    pady=5           # Espaçamento vertical externo.
)

# --- E-MAIL ---
# Cria e posiciona o rótulo "E-mail:".
tk.Label(
    janela,          # Janela à qual o rótulo pertence.
    text="E-mail:"   # Texto exibido no rótulo.
).grid(
    row=4,           # Quinta linha.
    column=0,        # Primeira coluna.
    padx=10,         # Espaçamento horizontal externo.
    pady=5           # Espaçamento vertical externo.
)

# Cria o campo de digitação do e-mail.
entrada_email = tk.Entry(
    janela,          # Janela à qual o campo pertence.
    width=40         # Largura aproximada em caracteres.
)

# Posiciona o campo de e-mail ao lado do rótulo.
entrada_email.grid(
    row=4,           # Mesma linha do rótulo "E-mail:".
    column=1,        # Segunda coluna.
    padx=10,         # Espaçamento horizontal externo.
    pady=5           # Espaçamento vertical externo.
)

# --- CIDADE ---
# Cria e posiciona o rótulo "Cidade:".
tk.Label(
    janela,          # Janela à qual o rótulo pertence.
    text="Cidade:"   # Texto exibido no rótulo.
).grid(
    row=5,           # Sexta linha.
    column=0,        # Primeira coluna.
    padx=10,         # Espaçamento horizontal externo.
    pady=5           # Espaçamento vertical externo.
)

# Cria o campo de digitação da cidade.
entrada_cidade = tk.Entry(
    janela,          # Janela à qual o campo pertence.
    width=40         # Largura aproximada em caracteres.
)

# Posiciona o campo de cidade ao lado do rótulo.
entrada_cidade.grid(
    row=5,           # Mesma linha do rótulo "Cidade:".
    column=1,        # Segunda coluna.
    padx=10,         # Espaçamento horizontal externo.
    pady=5           # Espaçamento vertical externo.
)


# ---------------- BOTÕES ----------------
# Cria o botão "Limpar" dentro da janela.
botao_limpar = tk.Button(
    janela,          # Janela à qual o botão pertence.
    text="Limpar",   # Texto exibido no botão.
    width=12,        # Largura do botão.
    command=limpar   # Executa a função limpar quando o botão é clicado.
)

# Posiciona o botão Limpar usando o gerenciador de layout grid.
botao_limpar.grid(
    row=6,           # Posiciona na linha de índice 6 (sétima linha).
    column=0,        # Posiciona na coluna de índice 0 (primeira coluna).
    pady=15          # Adiciona 15 pixels de espaço externo acima e abaixo.
)

# Cria o botão "Salvar" dentro da janela.
botao_salvar = tk.Button(
    janela,          # Janela à qual o botão pertence.
    text="Salvar",   # Texto exibido no botão.
    width=12,        # Largura do botão.
    command=salvar   # Função executada quando o botão é clicado.
)

# Posiciona o botão Salvar abaixo dos campos.
botao_salvar.grid(
    row=6,           # Sétima linha.
    column=1,        # Segunda coluna.
    pady=15          # Espaço acima e abaixo do botão.
)


# ---------------- LISTA (LISTBOX) ----------------
# Cria e posiciona o rótulo acima da lista de clientes.
tk.Label(
    janela,                      # Janela à qual o rótulo pertence.
    text="Clientes cadastrados:" # Texto exibido no rótulo.
).grid(
    row=7,                       # Oitava linha.
    column=0,                    # Primeira coluna.
    columnspan=2                 # Ocupa o espaço de duas colunas.
)

# Cria o componente Listbox para apresentar os clientes na interface.
lista_clientes = tk.Listbox(
    janela,          # Janela à qual a lista pertence.
    width=60,        # Largura em caracteres.
    height=8         # Altura em número de linhas visíveis.
)

# Posiciona a Listbox na grade da janela.
lista_clientes.grid(
    row=8,           # Nona linha.
    column=0,        # Primeira coluna.
    columnspan=2,    # Ocupa duas colunas.
    padx=10,         # Espaçamento horizontal externo.
    pady=10          # Espaçamento vertical externo.
)


# ---------------- EXECUÇÃO ----------------
# Coloca o cursor inicialmente no campo nome ao abrir o programa.
entrada_nome.focus()

# Inicia o ciclo de eventos da interface.
# Mantém a janela aberta e processa ações como cliques e digitação.
janela.mainloop()