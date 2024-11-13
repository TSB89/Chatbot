# ChatBot 0.23 - Atualização
# Implementado a saída de áudio com a biblioteca pyttsx3.

import tkinter as tk
from tkinter import PhotoImage
from PIL import ImageTk, Image
import pyttsx3

# Inicializando o engine de síntese de fala
engine = pyttsx3.init()

# Função para sintetizar o texto em fala
def sintetizar_fala(texto):
    engine.say(texto)
    engine.runAndWait()

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

    label_mensagem = tk.Label(frame_usuario, text=mensagem, bg="#dff0d8", fg="black", font=("Arial", 10), wraplength=200)
    label_mensagem.pack(side=tk.LEFT, padx=5)

    frame_usuario.pack(anchor='e', padx=10, pady=5)
    atualizar_scroll()

# Função para exibir a mensagem do chatbot no campo de chat
def exibir_mensagem_chatbot(mensagem):
    frame_bot = tk.Frame(frame_chatbot, bg="white")

    label_imagem_bot = tk.Label(frame_bot, image=imagem_bot)
    label_imagem_bot.pack(side=tk.LEFT, padx=5)

    label_mensagem = tk.Label(frame_bot, text=mensagem, bg="#f5f5f5", fg="black", font=("Arial", 10), wraplength=200)
    label_mensagem.pack(side=tk.LEFT, padx=5)

    frame_bot.pack(anchor='w', padx=10, pady=5)
    atualizar_scroll()

    # Chama a função para sintetizar a fala
    sintetizar_fala(mensagem)

# Função para exibir as opções do chatbot principal
def exibir_opcoes_principal():
    global imagem_bot
    imagem_bot = imagem_principal  # Restabelece a imagem do chatbot principal
    exibir_mensagem_chatbot("Sobre qual assunto você gostaria de falar?")
    opcoes = [
        "Consultar CPF",
        "Consultar FGTS",
        "Seguro desemprego",
        "Especialista Agricultor",
        "Especialista MEI",
        "Especialista Turismo"
    ]
    for opcao in opcoes:
        botao_opcao = tk.Button(frame_chatbot, text=opcao, bg="#b3cde0", fg="white", font=("Arial", 10),
                                command=lambda o=opcao: tratar_opcao_principal(o))
        botao_opcao.pack(anchor='w', padx=10, pady=5)

    atualizar_scroll()

# Função para tratar a escolha no chatbot principal
def tratar_opcao_principal(opcao):
    if opcao == "Especialista Turismo":
        exibir_opcoes_sub_chatbot("Especialista Turismo", imagem_sub_chatbot, respostas_turismo, opcoes_turismo)
    elif opcao == "Especialista MEI":
        exibir_opcoes_sub_chatbot("Especialista MEI", imagem_mei, respostas_mei, opcoes_mei)
    elif opcao == "Especialista Agricultor":
        exibir_opcoes_sub_chatbot("Especialista Agricultor", imagem_especialista_agricultor, respostas_agricultor, opcoes_agricultor)
    else:
        exibir_resposta(opcao, respostas_principal)

# Função para exibir as opções de sub-chatbots
def exibir_opcoes_sub_chatbot(nome_chatbot, imagem_sub, respostas_sub, opcoes_sub):
    global imagem_bot, respostas_atuais
    imagem_bot = imagem_sub  # Muda a imagem do chatbot para a do sub-chatbot correspondente
    respostas_atuais = respostas_sub  # Define as respostas atuais para o sub-chatbot
    exibir_mensagem_chatbot(f"Você está falando com o atendente {nome_chatbot}. Sobre qual assunto você gostaria de falar?")
    for opcao in opcoes_sub:
        if opcao == "Voltar ao chatbot principal":
            botao_opcao = tk.Button(frame_chatbot, text=opcao, bg="#f08080", fg="white", font=("Arial", 10),
                                    command=exibir_opcoes_principal)
        else:
            botao_opcao = tk.Button(frame_chatbot, text=opcao, bg="#b3cde0", fg="white", font=("Arial", 10),
                                    command=lambda o=opcao: exibir_resposta(o, respostas_atuais))
        botao_opcao.pack(anchor='w', padx=10, pady=5)

    atualizar_scroll()

# Função para exibir a resposta quando uma opção é selecionada
def exibir_resposta(opcao, respostas):
    resposta = respostas.get(opcao, "Opção não reconhecida.")
    exibir_mensagem_chatbot(resposta)

# Função para garantir que o chat role até o final
def atualizar_scroll():
    canvas.update_idletasks()
    canvas.yview_moveto(1)

# Dicionários de respostas para cada sub-chatbot
respostas_principal = {
    "Consultar CPF": "A consulta do CPF pode ser feita no site da Receita Federal www.teste.com.br",
    "Consultar FGTS": "Para consultar o FGTS, acesse o site da Caixa Econômica www.teste.com.br",
    "Seguro desemprego": "O seguro desemprego pode ser solicitado no portal gov.br.",
    "Bolsa Família": "Informações sobre o Bolsa Família estão disponíveis no site oficial do programa."
}

respostas_turismo = {
    "Guia de Turismo": "Informações sobre guias de turismo estão disponíveis no site do Ministério do Turismo.",
    "Obter Visto": "Para obter um visto, consulte as embaixadas ou consulados.",
    "Criar sua conta GOV.BR": "Acesse o portal gov.br para criar sua conta.",
    "Serviços financeiros": "Diversos bancos oferecem serviços para turistas.",
}

respostas_mei = {
    "Consultar CNPJ": "Você pode consultar o CNPJ no site da Receita Federal.",
    "Emitir Guia DAS": "Acesse o Portal do Empreendedor para emitir sua guia DAS.",
    "Atualizar dados MEI": "A atualização dos dados pode ser feita no Portal do Empreendedor.",
    "Consultoria Sebrae": "O Sebrae oferece consultoria especializada para MEIs.",
}

respostas_agricultor = {
    "Consultar CAFIR e CNIR": "Você pode consultar os dados de CAFIR e CNIR no site do Incra.",
    "Consultar o Pronaf": "O Pronaf oferece crédito rural para pequenos agricultores.",
    "Consultar o Garantia Safra": "O programa Garantia Safra está disponível no portal do governo.",
    "Cadastrar Viticultor": "Para cadastrar-se como viticultor, acesse o portal do Ministério da Agricultura."
}

# Definir opções específicas para cada sub-chatbot
opcoes_turismo = [
    "Guia de Turismo",
    "Obter Visto",
    "Criar sua conta GOV.BR",
    "Serviços financeiros",
    "Voltar ao chatbot principal"
]

opcoes_mei = [
    "Consultar CNPJ",
    "Emitir Guia DAS",
    "Atualizar dados MEI",
    "Consultoria Sebrae",
    "Voltar ao chatbot principal"
]

opcoes_agricultor = [
    "Consultar CAFIR e CNIR",
    "Consultar o Pronaf",
    "Consultar o Garantia Safra ",
    "Cadastrar Viticultor",
    "Voltar ao chatbot principal"
]

# Configuração da janela principal
janela = tk.Tk()
janela.title("ChatBot versão 0.23")

# Definindo a largura e altura da janela
largura = 350  # Defina a largura desejada
altura = 400   # Defina a altura desejada
janela.geometry(f"{largura}x{altura}")

# Carregando as imagens
imagem_principal = ImageTk.PhotoImage(Image.open("C:/Users/Thiago/Desktop/Tutor GOV/A.png"))  # Caminho da imagem do chatbot principal
imagem_sub_chatbot = ImageTk.PhotoImage(Image.open("C:/Users/Thiago/Desktop/Tutor GOV/T.png"))  # Caminho da imagem do sub-chatbot "Especialista Turismo"
imagem_mei = ImageTk.PhotoImage(Image.open("C:/Users/Thiago/Desktop/Tutor GOV/M.png"))  # Caminho da imagem do sub-chatbot MEI
imagem_especialista_agricultor = ImageTk.PhotoImage(Image.open("C:/Users/Thiago/Desktop/Tutor GOV/F.png"))  # Caminho da imagem do sub-chatbot Especialista Agricultor
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

# Inicia a janela principal do chatbot
janela.mainloop()
