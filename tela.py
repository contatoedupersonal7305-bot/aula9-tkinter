import tkinter as tk

janela = tk.Tk()
janela.geometry("1920x1080") 
minha_imagem = tk.PhotoImage(file="image 1.png") 
label_imagem = tk.Label(janela, image=minha_imagem)
label_imagem.image = minha_imagem 

label_imagem.pack(pady=(100, 0)) 

entrada_email = tk.Entry(janela, font=("Arial", 16), bg="#cecdcd", relief="flat", justify="center", width=30)
entrada_email.insert(0, "e-mail")
entrada_email.pack(pady=10, ipady=12)

entrada_senha = tk.Entry(janela, font=("Arial", 16), bg="#cecdcd", relief="flat", justify="center", width=30)
entrada_senha.insert(0, "senha")
entrada_senha.pack(pady=10, ipady=12)


janela.mainloop()