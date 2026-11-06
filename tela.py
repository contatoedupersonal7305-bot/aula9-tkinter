import tkinter as tk
from tkinter import messagebox  # Importação necessária para exibir o pop-up de erro

# Funções para o campo de E-mail
def on_click_email(event):
    if entrada_email.get() == "e-mail":
        entrada_email.delete(0, tk.END)
        entrada_email.config(fg="black")

def on_leave_email(event):
    if entrada_email.get() == "":
        entrada_email.insert(0, "e-mail")
        entrada_email.config(fg="gray")

# Funções para o campo de Senha
def on_click_senha(event):
    if entrada_senha.get() == "senha":
        entrada_senha.delete(0, tk.END)
        entrada_senha.config(fg="black", show="*")

def on_leave_senha(event):
    if entrada_senha.get() == "":
        entrada_senha.config(show="")
        entrada_senha.insert(0, "senha")
        entrada_senha.config(fg="gray")

# Função do Botão ACESSAR com Validação
def abrir_proxima_pagina():
    # 1. Pega os valores digitados nos campos
    email_digitado = entrada_email.get()
    senha_digitada = entrada_senha.get()
    
    # 2. Define qual é o e-mail e senha corretos (Altere aqui se precisar)
    email_correto = "teste@email.com"
    senha_correta = "1234"
    
    # 3. Verifica se bate com os dados corretos
    if email_digitado == email_correto and senha_digitada == senha_correta:
        
        # Reseta os campos após o sucesso
        entrada_email.delete(0, tk.END)
        entrada_email.insert(0, "e-mail")
        entrada_email.config(fg="gray")
        
        entrada_senha.delete(0, tk.END)
        entrada_senha.config(show="")
        entrada_senha.insert(0, "senha")
        entrada_senha.config(fg="gray")
        
        janela.focus()

        # Abre a "Próxima Página"
        nova_janela = tk.Toplevel(janela)
        nova_janela.geometry("600x400")
        nova_janela.title("Nova Página")
        nova_janela.configure(bg="white")
        
        tk.Label(nova_janela, text="Bem-vindo ao sistema!", font=("Arial", 20, "bold"), bg="white", fg="green").pack(pady=150)
        
    else:
        # 4. Se errar a senha, mostra um aviso na tela e não avança
        messagebox.showerror("Erro de Login", "E-mail ou senha incorretos. Tente novamente.")


janela = tk.Tk()
janela.geometry("1920x1080")
janela.configure(bg="white")

# 1. Imagem
minha_imagem = tk.PhotoImage(file="image 1.png")  
label_imagem = tk.Label(janela, image=minha_imagem, bg="white")
label_imagem.image = minha_imagem  
label_imagem.pack(pady=(100, 40))

# 2. Campo de E-mail
entrada_email = tk.Entry(janela, font=("Arial", 16), bg="#f0f0f0", fg="gray", relief="flat", justify="center", width=30)
entrada_email.insert(0, "e-mail")
entrada_email.pack(pady=10, ipady=12)
entrada_email.bind("<FocusIn>", on_click_email)
entrada_email.bind("<FocusOut>", on_leave_email)

# 3. Campo de Senha
entrada_senha = tk.Entry(janela, font=("Arial", 16), bg="#f0f0f0", fg="gray", relief="flat", justify="center", width=30)
entrada_senha.insert(0, "senha")
entrada_senha.pack(pady=10, ipady=12)
entrada_senha.bind("<FocusIn>", on_click_senha)
entrada_senha.bind("<FocusOut>", on_leave_senha)

# 4. Botão ACESSAR
botao_acessar = tk.Button(janela, text="ACESSAR", font=("Arial", 14, "bold"), bg="#3b96c8", fg="white", relief="flat", width=33, command=abrir_proxima_pagina)
botao_acessar.pack(pady=20, ipady=8)

janela.focus()
janela.mainloop()