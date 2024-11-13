# ChatBot 0.2 - Atualização
# Sub-ChatBots criados com sucesso, a próxima versão deverá atribuir o tema deles.

import tkinter as tk
from tkinter import PhotoImage
from PIL import ImageTk
from PIL import Image

# Função para enviar a mensagem do usuário
def enviar_mensagem(event=None):
    mensagem_usuario = entrada_texto.get()
    if mensagem_usuario.strip():
        exibir_mensagem_usuario(mensagem_usuario)
        entrada_texto.delete(0, tk.END)

# Função para exibir a mensagem do usuário no campo de chat
def exibir_mensagem_usuario(mensagem):
    frame_usuario = tk.Frame(frame_chatbot, bg="white")

    label_imagem_usuario = tk.Label(frame_usuario, image=imagem_usuario)
    label_imagem_usuario.pack(side=tk.LEFT, padx=5)

    label_mensagem = tk.Label(frame_usuario, text=mensagem, bg="#dff0d8", fg="black", font=("Arial", 10), wraplength=250)
    label_mensagem.pack(side=tk.LEFT, padx=5)

    frame_usuario.pack(anchor='e', padx=10, pady=5)
    atualizar_scroll()

# Função para exibir a mensagem do chatbot no campo de chat
def exibir_mensagem_chatbot(mensagem):
    frame_bot = tk.Frame(frame_chatbot, bg="white")

    label_imagem_bot = tk.Label(frame_bot, image=imagem_bot)
    label_imagem_bot.pack(side=tk.LEFT, padx=5)

    label_mensagem = tk.Label(frame_bot, text=mensagem, bg="#f5f5f5", fg="black", font=("Arial", 10), wraplength=250)
    label_mensagem.pack(side=tk.LEFT, padx=5)

    frame_bot.pack(anchor='w', padx=10, pady=5)
    atualizar_scroll()

# Função para exibir as opções do chatbot principal
def exibir_opcoes_principal():
    global imagem_bot
    imagem_bot = imagem_principal  # Restabelece a imagem do chatbot principal
    exibir_mensagem_chatbot("Bem vindo. Sobre qual assunto você gostaria de falar?")
    opcoes = [
        "Consultar CPF",
        "Consultar FGTS",
        "Seguro desemprego",
        "Bolsa Família",
        "Micro Empreendedor Individual",
        "Falar com outro especialista"
    ]
    for opcao in opcoes:
        botao_opcao = tk.Button(frame_chatbot, text=opcao, bg="#b3cde0", fg="white", font=("Arial", 10),
                                command=lambda o=opcao: tratar_opcao_principal(o))
        botao_opcao.pack(anchor='w', padx=10, pady=5)

    atualizar_scroll()  # Garantir que o chat role até o final

# Função para tratar a escolha no chatbot principal
def tratar_opcao_principal(opcao):
    if opcao == "Falar com outro especialista":
        exibir_opcoes_sub_chatbot("Outro Especialista", imagem_sub_chatbot)
    elif opcao == "Micro Empreendedor Individual":
        exibir_opcoes_sub_chatbot("MEI", imagem_mei)
    elif opcao == "Bolsa Família":
        exibir_opcoes_sub_chatbot("Bolsa Família", imagem_bolsa_familia)
    else:
        exibir_mensagem_usuario(opcao)

# Função para exibir as opções de sub-chatbots (Especialista, MEI, Bolsa Família)
def exibir_opcoes_sub_chatbot(nome_chatbot, imagem_sub):
    global imagem_bot
    imagem_bot = imagem_sub  # Muda a imagem do chatbot para a do sub-chatbot correspondente
    exibir_mensagem_chatbot(f"Você está falando com o especialista de {nome_chatbot}. Sobre qual assunto você gostaria de falar?")
    opcoes = [
        "Consultar CPF",
        "Consultar FGTS",
        "Seguro desemprego",
        "Bolsa Família" if nome_chatbot != "Bolsa Família" else "MEI",  # Substituir a opção para evitar repetição
        "Voltar ao chatbot principal"
    ]
    for opcao in opcoes:
        if opcao == "Voltar ao chatbot principal":
            botao_opcao = tk.Button(frame_chatbot, text=opcao, bg="#f08080", fg="white", font=("Arial", 10),
                                    command=exibir_opcoes_principal)
        else:
            botao_opcao = tk.Button(frame_chatbot, text=opcao, bg="#b3cde0", fg="white", font=("Arial", 10),
                                    command=lambda o=opcao: exibir_mensagem_usuario(o))
        botao_opcao.pack(anchor='w', padx=10, pady=5)

    atualizar_scroll()  # Garantir que o chat role até o final

# Função para garantir que o chat role até o final
def atualizar_scroll():
    canvas.update_idletasks()
    canvas.yview_moveto(1)

# Configuração da janela principal
janela = tk.Tk()
janela.title("Atendimento Online")

# Carregando as imagens
imagem_principal = ImageTk.PhotoImage(Image.open("C:/Users/Thiago/Desktop/Tutor GOV/A.png"))  # Caminho da imagem do chatbot principal
imagem_sub_chatbot = ImageTk.PhotoImage(Image.open("C:/Users/Thiago/Desktop/Tutor GOV/T.png"))  # Caminho da imagem do sub-chatbot "Outro Especialista"
imagem_mei = ImageTk.PhotoImage(Image.open("C:/Users/Thiago/Desktop/Tutor GOV/F.png"))  # Caminho da imagem do sub-chatbot MEI
imagem_bolsa_familia = ImageTk.PhotoImage(Image.open("C:/Users/Thiago/Desktop/Tutor GOV/W.png"))  # Caminho da imagem do sub-chatbot Bolsa Família
imagem_usuario = ImageTk.PhotoImage(Image.open("C:/Users/Thiago/Desktop/Tutor GOV/E.png"))  # Imagem do usuário

# Definindo a imagem inicial como a do chatbot principal
imagem_bot = imagem_principal

# Configurando o frame principal de chat
frame_principal = tk.Frame(janela)
frame_principal.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Campo de rolagem do chat
canvas = tk.Canvas(frame_principal)
frame_chatbot = tk.Frame(canvas, bg="white")
scrollbar = tk.Scrollbar(frame_principal, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
canvas.create_window((0, 0), window=frame_chatbot, anchor='nw')

frame_chatbot.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Exibe as opções iniciais do ChatBot
exibir_opcoes_principal()

# Campo de entrada de texto para o usuário
entrada_texto = tk.Entry(janela, font=("Arial", 12))
entrada_texto.pack(fill=tk.X, padx=10, pady=10)
entrada_texto.bind("<Return>", enviar_mensagem)

janela.mainloop()
