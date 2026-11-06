import tkinter as tk

janela = tk.Tk()
janela.geometry("1920x1080") 

minha_imagem = tk.PhotoImage(file="image 1.png") 
label_imagem = tk.Label(janela, image=minha_imagem)
label_imagem.image = minha_imagem 

label_imagem.pack(pady=(100, 0)) 


janela.mainloop()