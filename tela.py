import tkinter as tk

janela = tk.Tk()
janela.geometry("1920x1080") # Define o tamanho da janela (LarguraxAltura)

# 1. Cria a função que será acionada pelo evento do botão
minha_imagem = tk.PhotoImage(file="image 1.png")  # Substitua pelo caminho da sua imagem
label_imagem = tk.Label(janela, image=minha_imagem)
label_imagem.image = minha_imagem  # Mantém uma referência à imagem para evitar que ela seja coletada pelo garbage collector
label_imagem.pack()

# 5. Inicia o loop de eventos, mantendo a aplicação viva
janela.mainloop()