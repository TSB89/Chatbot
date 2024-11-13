# ChatBot 0.1 - Objetivo
# Fazer com que as opções apareçam e possam ser selecionadas através da aba de texto.

import tkinter as tk
from PIL import Image, ImageTk


# Função para carregar e exibir uma imagem no widget
def carregar_imagem(widget, caminho_imagem, frame):
    try:
        image = Image.open(caminho_imagem)
        image = image.resize((150, 150), Image.Resampling.LANCZOS)  # Alta qualidade
        image = ImageTk.PhotoImage(image)
        widget.config(image=image)
        widget.image = image
        frame.pack(pady=10)  # Garante que o frame seja visível
    except Exception as e:
        print(f"Erro ao carregar a imagem: {e}")


# Função para exibir a resposta na área de texto e trocar a imagem do bot
def exibir_resposta(opcao):
    text_area.insert(tk.END, f"Você: {opcao}\n")
    text_area.insert(tk.END, f"Chatbot: Você escolheu o sub-bot '{opcao}'\n")

    # Troca a imagem principal pela do sub-bot correspondente
    if opcao == "Agricultor":
        text_area.insert(tk.END, "Sub-bot Agricultor: Como posso te ajudar hoje?\n")
        carregar_imagem(imagem_label_principal, caminho_imagem_agricultor, frame_imagem_principal)
    elif opcao == "Turista":
        text_area.insert(tk.END, "Sub-bot Turista: Que lugar deseja explorar?\n")
        carregar_imagem(imagem_label_principal, caminho_imagem_turista, frame_imagem_principal)
    elif opcao == "Aposentado":
        text_area.insert(tk.END, "Sub-bot Aposentado: Como está sua aposentadoria?\n")
        carregar_imagem(imagem_label_principal, caminho_imagem_aposentado, frame_imagem_principal)
    elif opcao == "Estudante":
        text_area.insert(tk.END, "Sub-bot Estudante: Como estão seus estudos?\n")
        carregar_imagem(imagem_label_principal, caminho_imagem_estudante, frame_imagem_principal)

    text_area.see(tk.END)


# Função para exibir as opções de sub-bots na área de texto
def exibir_opcoes():
    text_area.insert(tk.END, "Chatbot: Escolha um dos sub-bots abaixo:\n")
    opcoes = [
        "1. Agricultor",
        "2. Turista",
        "3. Aposentado",
        "4. Estudante"
    ]
    for opcao in opcoes:
        text_area.insert(tk.END, f"{opcao}\n")


# Função chamada quando o usuário envia a mensagem
def enviar_mensagem(event=None):
    mensagem = entrada_texto.get()  # Captura o texto da entrada do usuário
    if mensagem.strip():
        text_area.insert(tk.END, f"Você: {mensagem}\n")
        resposta_do_chatbot(mensagem)
    entrada_texto.delete(0, tk.END)


# Simula a resposta do chatbot com base na mensagem do usuário
def resposta_do_chatbot(mensagem):
    if mensagem in ["1", "Agricultor"]:
        exibir_resposta("Agricultor")
    elif mensagem in ["2", "Turista"]:
        exibir_resposta("Turista")
    elif mensagem in ["3", "Aposentado"]:
        exibir_resposta("Aposentado")
    elif mensagem in ["4", "Estudante"]:
        exibir_resposta("Estudante")
    else:
        text_area.insert(tk.END, "Chatbot: Desculpe, não entendi. Por favor, escolha uma das opções.\n")
        text_area.see(tk.END)


# Função para criar botões de sub-bots
def criar_botoes_sub_bots():
    sub_bots = [
        ("1", "Agricultor"),
        ("2", "Turista"),
        ("3", "Aposentado"),
        ("4", "Estudante")
    ]
    for num, nome in sub_bots:
        botao = tk.Button(frame_botoes, text=f"{num}. {nome}", width=30,
                          command=lambda opcao=nome: exibir_resposta(opcao))
        botao.pack(pady=5)


# Configuração da janela principal
root = tk.Tk()
root.title("GiOVana - Atendente Virtual")
root.geometry("500x700")

# Definindo os caminhos das imagens (edite estas variáveis com os caminhos corretos)
caminho_imagem_principal = "C:/Users/Thiago/Pictures/Screenshots/marketing/B1.png"
caminho_imagem_agricultor = "C:/Users/Thiago/Pictures/Screenshots/marketing/B4.png"
caminho_imagem_turista = "C:/Users/Thiago/Pictures/Screenshots/marketing/B3.png"
caminho_imagem_aposentado = "C:/Users/Thiago/Pictures/Screenshots/marketing/B5.png"
caminho_imagem_estudante = "C:/Users/Thiago/Pictures/Screenshots/marketing/B2.png"

# Frame para a imagem do bot principal (ou sub-bot selecionado)
frame_imagem_principal = tk.Frame(root)
frame_imagem_principal.pack(pady=10)

# Label para exibir a imagem principal ou dos sub-bots
imagem_label_principal = tk.Label(frame_imagem_principal)
imagem_label_principal.pack()

# Carregar a imagem inicial do bot principal
carregar_imagem(imagem_label_principal, caminho_imagem_principal, frame_imagem_principal)

# Frame para a área de texto
frame_texto = tk.Frame(root)
frame_texto.pack(pady=10)

# Área de texto para exibir a conversa
text_area = tk.Text(frame_texto, height=20, width=60)
text_area.pack()

# Frame para a entrada de texto do usuário
frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=10)

# Caixa de entrada de texto do usuário
entrada_texto = tk.Entry(frame_entrada, width=40)
entrada_texto.pack(side=tk.LEFT, padx=10)

# Botão de enviar
botao_enviar = tk.Button(frame_entrada, text="Enviar", command=enviar_mensagem)
botao_enviar.pack(side=tk.RIGHT)

# Frame para os botões das opções
frame_botoes = tk.Frame(root)
frame_botoes.pack(pady=20)

# Atalho para enviar mensagem usando a tecla Enter
root.bind('<Return>', enviar_mensagem)

# Exibe as opções ao iniciar o chatbot
text_area.insert(tk.END, "Chatbot: Olá! Escolha um dos sub-bots abaixo ou clique em uma opção:\n")
exibir_opcoes()
criar_botoes_sub_bots()

# Iniciar o loop principal
root.mainloop()
