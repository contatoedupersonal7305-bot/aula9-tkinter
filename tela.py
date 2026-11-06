import tkinter as tk
from tkinter import messagebox

# --- BANCO DE DADOS TEMPORÁRIO ---
email_salvo = ""
senha_salva = ""
linha_selecionada_index = None  # Guarda o índice da consulta em edição

# --- DADOS INICIAIS DE CONSULTAS ---
dados_consultas = [
    ["João Silva", "Dr. Carlos Santos", "12/09", "83145 Maggie Plaza Suite 204"],
    ["Maria Oliveira", "Dr. Carlos Santos", "14/09", "Av. Paulista 1000 - Cj 42"],
    ["Pedro Alves", "Dra. Ana Costa", "18/09", "Rua das Flores 123"],
    ["Ana Souza", "Dr. Carlos Santos", "20/09", "83145 Maggie Plaza Suite 204"],
    ["Lucas Lima", "Dra. Ana Costa", "22/09", "Rua das Flores 123"],
    ["Fernanda Rocha", "Dr. Carlos Santos", "25/09", "Av. Paulista 1000 - Cj 42"],
    ["Gabriel Melo", "Dra. Ana Costa", "28/09", "83145 Maggie Plaza Suite 204"],
    ["Beatriz Luz", "Dr. Carlos Santos", "30/09", "Rua das Flores 123"]
]

# --- FUNÇÃO PARA TROCAR DE TELA ---
def mostrar_tela(tela_para_mostrar):
    tela_para_mostrar.tkraise()
    janela.focus_set()

# --- FUNÇÕES DE PLACEHOLDER ---
def on_focus_in(entry, texto_padrao, eh_senha=False):
    if entry.get() == texto_padrao:
        entry.delete(0, tk.END)
        entry.config(fg="#333333")
        if eh_senha:
            entry.config(show="*")

def on_focus_out(entry, texto_padrao, eh_senha=False):
    if entry.get().strip() == "":
        if eh_senha:
            entry.config(show="")
        entry.delete(0, tk.END)
        entry.insert(0, texto_padrao)
        entry.config(fg="#888888")

# --- LÓGICA DE CADASTRO E LOGIN ---
def salvar_cadastro():
    global email_salvo, senha_salva
    novo_email = entrada_novo_email.get().strip()
    nova_senha = entrada_nova_senha.get().strip()

    if novo_email in ["", " e-mail"] or nova_senha in ["", " senha"]:
        messagebox.showwarning("Aviso", "Preencha todos os campos para cadastrar!")
        return

    email_salvo = novo_email
    senha_salva = nova_senha
    messagebox.showinfo("Sucesso", "Acesso criado com sucesso! Faça o login.")
    mostrar_tela(tela_login)

def fazer_login():
    email = entrada_email.get().strip()
    senha = entrada_senha.get().strip()
    
    if email == email_salvo and senha == senha_salva and email_salvo != "":
        mostrar_tela(tela_dashboard)
    else:
        messagebox.showerror("Erro", "E-mail ou senha incorretos (ou conta não criada)!")

# --- JANELA PRINCIPAL ---
janela = tk.Tk()
janela.geometry("1920x1080")
janela.configure(bg="white")

janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)

# --- DEFININDO AS TELAS (FRAMES) ---
tela_login = tk.Frame(janela, bg="white")
tela_cadastro = tk.Frame(janela, bg="white")
tela_dashboard = tk.Frame(janela, bg="white")
tela_pacientes = tk.Frame(janela, bg="white")
tela_palestras = tk.Frame(janela, bg="white")
tela_consultas = tk.Frame(janela, bg="white")
tela_editar_consulta = tk.Frame(janela, bg="white")

todas_as_telas = [
    tela_login, tela_cadastro, tela_dashboard, 
    tela_pacientes, tela_palestras, tela_consultas, tela_editar_consulta
]

for t in todas_as_telas:
    t.grid(row=0, column=0, sticky="nsew")

# ==========================================
# COMPONENTE REUTILIZÁVEL: CABEÇALHO PADRÃO
# ==========================================
def criar_cabecalho(parent, mostrar_voltar=False, comando_voltar=None):
    header = tk.Frame(parent, bg="white")
    header.pack(fill="x", padx=40, pady=20)

    header_left = tk.Frame(header, bg="white")
    header_left.pack(side="left")

    avatar_label = tk.Label(header_left, text="👤", font=("Arial", 28), fg="#4fa8e8", bg="#d6efff", width=2, height=1)
    avatar_label.pack(side="left", padx=(0, 15))

    lbl_bemvindo = tk.Label(header_left, text="BEM VINDO JUAN", font=("Arial", 11, "bold"), fg="#3a8ebd", bg="#e1f3fd", padx=20, pady=8)
    lbl_bemvindo.pack(side="left", padx=(0, 15))

    lbl_notif = tk.Label(header_left, text="🔔", font=("Arial", 18), fg="#4fa8e8", bg="white", cursor="hand2")
    lbl_notif.pack(side="left")

    header_right = tk.Frame(header, bg="white")
    header_right.pack(side="right")
    lbl_logo = tk.Label(header_right, text="a+", font=("Arial", 28, "bold italic"), fg="#2b8bbb", bg="white")
    lbl_logo.pack(side="right")

    if mostrar_voltar:
        sub_header = tk.Frame(parent, bg="white")
        sub_header.pack(fill="x", padx=60, pady=(0, 10))
        btn_voltar = tk.Label(sub_header, text="⇐ Voltar", font=("Arial", 12, "bold"), fg="#3a8ebd", bg="white", cursor="hand2")
        btn_voltar.pack(side="left")
        if comando_voltar:
            btn_voltar.bind("<Button-1>", lambda e: comando_voltar())

# ==========================================
# FUNÇÕES DE EDICÃO E ATUALIZAÇÃO DA CONSULTA
# ==========================================
def carregar_dados_edicao(index, paciente, medico, data, local):
    global linha_selecionada_index
    linha_selecionada_index = index

    # Limpa e preenche os campos com os valores atuais da linha
    e_paciente.delete(0, tk.END)
    e_paciente.insert(0, paciente)

    e_data.delete(0, tk.END)
    e_data.insert(0, data)

    e_endereco.delete(0, tk.END)
    e_endereco.insert(0, local)

    e_medico.delete(0, tk.END)
    e_medico.insert(0, medico)

    mostrar_tela(tela_editar_consulta)
    
    # Coloca o cursor piscando automaticamente na caixa de texto "Paciente"
    e_paciente.focus_set()

def salvar_edicao_consulta():
    global linha_selecionada_index
    
    if linha_selecionada_index is not None:
        # Atualiza a lista principal com os novos valores digitados
        dados_consultas[linha_selecionada_index][0] = e_paciente.get().strip()
        dados_consultas[linha_selecionada_index][1] = e_medico.get().strip()
        dados_consultas[linha_selecionada_index][2] = e_data.get().strip()
        dados_consultas[linha_selecionada_index][3] = e_endereco.get().strip()

        # Reconstruir a tabela de consultas para mostrar as alterações na tela
        construir_tabela(tela_consultas, "CONSULTAS", ["Paciente", "Médico", "Data", "Local", "Ações"], dados_consultas)
        
        messagebox.showinfo("Sucesso", "Consulta atualizada com sucesso!")
        mostrar_tela(tela_consultas)

# ==========================================
# COMPONENTE REUTILIZÁVEL: TABELA DE DADOS
# ==========================================
def construir_tabela(parent, titulo, colunas, lista_dados=None):
    # Limpa widgets anteriores da tela para reconstruir
    for widget in parent.winfo_children():
        widget.destroy()

    criar_cabecalho(parent, mostrar_voltar=True, comando_voltar=lambda: mostrar_tela(tela_dashboard))

    lbl_titulo = tk.Label(parent, text=titulo, font=("Arial", 22, "bold"), fg="#2b8bbb", bg="white")
    lbl_titulo.pack(pady=(0, 20))

    table_frame = tk.Frame(parent, bg="white")
    table_frame.pack(expand=True, fill="both", padx=100)

    for col_idx in range(len(colunas)):
        table_frame.grid_columnconfigure(col_idx, weight=1)

    for col_idx, col_nome in enumerate(colunas):
        lbl_col = tk.Label(table_frame, text=col_nome, font=("Arial", 12, "bold"), fg="#2b8bbb", bg="white", pady=10)
        lbl_col.grid(row=0, column=col_idx, sticky="ew")

    if lista_dados:
        for row_idx, item in enumerate(lista_dados, start=1):
            bg_cor = "#f7fafc" if row_idx % 2 == 0 else "white"
            
            for col_idx, valor in enumerate(item):
                lbl_dado = tk.Label(table_frame, text=valor, font=("Arial", 11), fg="#3a8ebd", bg=bg_cor, pady=8)
                lbl_dado.grid(row=row_idx, column=col_idx, sticky="ew")
            
            if "Ações" in colunas:
                btn_acao = tk.Label(table_frame, text="Editar", font=("Arial", 11), fg="#2b8bbb", bg=bg_cor, cursor="hand2", pady=8)
                btn_acao.grid(row=row_idx, column=len(colunas)-1, sticky="ew")
                
                # Passa o índice da linha e os dados para preenchimento
                p_nome, p_medico, p_data, p_local = item[0], item[1], item[2], item[3]
                idx_atual = row_idx - 1
                btn_acao.bind("<Button-1>", lambda e, idx=idx_atual, p=p_nome, m=p_medico, d=p_data, l=p_local: carregar_dados_edicao(idx, p, m, d, l))

    pagi_frame = tk.Frame(parent, bg="white")
    pagi_frame.pack(pady=20)
    
    paginas = ["1", "2", "3", "4", "5", "6"]
    for p in paginas:
        if p == "2":
            btn_p = tk.Label(pagi_frame, text=p, font=("Arial", 10, "bold"), fg="white", bg="#2b8bbb", width=3, height=1)
        else:
            btn_p = tk.Label(pagi_frame, text=p, font=("Arial", 10), fg="#2b8bbb", bg="white", width=3, height=1)
        btn_p.pack(side="left", padx=2)

# ==========================================
# 1. TELA DE LOGIN
# ==========================================
minha_imagem = tk.PhotoImage(file="image 1.png")  
label_imagem = tk.Label(tela_login, image=minha_imagem, bg="white")
label_imagem.image = minha_imagem  
label_imagem.pack(pady=(80, 30))

entrada_email = tk.Entry(tela_login, font=("Arial", 14), bg="#eaeaea", fg="#888888", bd=0, relief="flat", justify="left", width=32, highlightthickness=1, highlightbackground="#eaeaea", highlightcolor="#a020f0")
entrada_email.insert(0, " e-mail")
entrada_email.pack(pady=8, ipady=10)
entrada_email.bind("<FocusIn>", lambda e: on_focus_in(entrada_email, " e-mail"))
entrada_email.bind("<FocusOut>", lambda e: on_focus_out(entrada_email, " e-mail"))

entrada_senha = tk.Entry(tela_login, font=("Arial", 14), bg="#eaeaea", fg="#888888", bd=0, relief="flat", justify="left", width=32, highlightthickness=1, highlightbackground="#eaeaea", highlightcolor="#a020f0")
entrada_senha.insert(0, " senha")
entrada_senha.pack(pady=8, ipady=10)
entrada_senha.bind("<FocusIn>", lambda e: on_focus_in(entrada_senha, " senha", eh_senha=True))
entrada_senha.bind("<FocusOut>", lambda e: on_focus_out(entrada_senha, " senha", eh_senha=True))

botao_acessar = tk.Button(tela_login, text="ACESSAR", font=("Arial", 11, "bold"), bg="#2b8bbb", fg="white", highlightbackground="#2b8bbb", activebackground="#206b93", activeforeground="white", bd=0, relief="flat", width=32, command=fazer_login)
botao_acessar.pack(pady=20, ipady=10)

link_primeiro_acesso = tk.Label(tela_login, text="PRIMEIRO ACESSO", font=("Arial", 11, "bold"), bg="white", fg="#2b8bbb", cursor="hand2")
link_primeiro_acesso.pack(pady=5)
link_primeiro_acesso.bind("<Button-1>", lambda e: mostrar_tela(tela_cadastro))

# ==========================================
# 2. TELA DE CADASTRO
# ==========================================
label_imagem_cad = tk.Label(tela_cadastro, image=minha_imagem, bg="white")
label_imagem_cad.image = minha_imagem
label_imagem_cad.pack(pady=(80, 30))

entrada_novo_email = tk.Entry(tela_cadastro, font=("Arial", 14), bg="#eaeaea", fg="#888888", bd=0, relief="flat", justify="left", width=32, highlightthickness=1, highlightbackground="#eaeaea", highlightcolor="#a020f0")
entrada_novo_email.insert(0, " e-mail")
entrada_novo_email.pack(pady=8, ipady=10)
entrada_novo_email.bind("<FocusIn>", lambda e: on_focus_in(entrada_novo_email, " e-mail"))
entrada_novo_email.bind("<FocusOut>", lambda e: on_focus_out(entrada_novo_email, " e-mail"))

entrada_nova_senha = tk.Entry(tela_cadastro, font=("Arial", 14), bg="#eaeaea", fg="#888888", bd=0, relief="flat", justify="left", width=32, highlightthickness=1, highlightbackground="#eaeaea", highlightcolor="#a020f0")
entrada_nova_senha.insert(0, " senha")
entrada_nova_senha.pack(pady=8, ipady=10)
entrada_nova_senha.bind("<FocusIn>", lambda e: on_focus_in(entrada_nova_senha, " senha", eh_senha=True))
entrada_nova_senha.bind("<FocusOut>", lambda e: on_focus_out(entrada_nova_senha, " senha", eh_senha=True))

botao_salvar = tk.Button(tela_cadastro, text="CADASTRAR E VOLTAR", font=("Arial", 11, "bold"), bg="#2b8bbb", fg="white", highlightbackground="#2b8bbb", activebackground="#206b93", activeforeground="white", bd=0, relief="flat", width=32, command=salvar_cadastro)
botao_salvar.pack(pady=20, ipady=10)

# ==========================================
# 3. TELA DASHBOARD
# ==========================================
criar_cabecalho(tela_dashboard)

body_frame = tk.Frame(tela_dashboard, bg="white")
body_frame.pack(expand=True)

lbl_perfil = tk.Label(body_frame, text="PERFIL: MÉDICO", font=("Arial", 10, "bold"), fg="#3a8ebd", bg="white")
lbl_perfil.grid(row=0, column=0, sticky="w", pady=(0, 5), padx=10)

cards_container = tk.Frame(body_frame, bg="white")
cards_container.grid(row=1, column=0)

def criar_card(parent, icone_texto, titulo, comando):
    card = tk.Frame(parent, bg="#95d6f8", width=190, height=200, cursor="hand2")
    card.pack_propagate(False)
    
    lbl_icon = tk.Label(card, text=icone_texto, font=("Arial", 42), fg="#3a8ebd", bg="#95d6f8")
    lbl_icon.pack(expand=True, pady=(20, 0))
    
    lbl_title = tk.Label(card, text=titulo, font=("Arial", 13, "bold"), fg="white", bg="#95d6f8")
    lbl_title.pack(pady=(0, 20))
    
    card.bind("<Button-1>", lambda e: comando())
    lbl_icon.bind("<Button-1>", lambda e: comando())
    lbl_title.bind("<Button-1>", lambda e: comando())
    
    return card

card1 = criar_card(cards_container, "👤", "PACIENTES", lambda: mostrar_tela(tela_pacientes))
card1.pack(side="left", padx=15)

card2 = criar_card(cards_container, "📅\n12", "PALESTRAS", lambda: mostrar_tela(tela_palestras))
card2.pack(side="left", padx=15)

card3 = criar_card(cards_container, "📅\n12", "CONSULTAS", lambda: mostrar_tela(tela_consultas))
card3.pack(side="left", padx=15)

footer_frame = tk.Frame(tela_dashboard, bg="white")
footer_frame.pack(side="bottom", pady=40)

lbl_ajuda = tk.Label(footer_frame, text="PRECISA DE AJUDA? 💬", font=("Arial", 16, "bold"), fg="#2b8bbb", bg="white", cursor="hand2")
lbl_ajuda.pack()

# ==========================================
# 4. TELA PACIENTES
# ==========================================
dados_pacientes = [["João Silva", "123.456.789-00", "Masculino", "30", "12/09/2026"] for _ in range(8)]
construir_tabela(tela_pacientes, "PACIENTES", ["Nome", "Documento", "Sexo", "Idade", "Última Consulta"], dados_pacientes)

# ==========================================
# 5. TELA PALESTRAS
# ==========================================
dados_palestras = [["Nutrição Esportiva", "15/10/2026", "Auditório A", "R$ 150", "2h"] for _ in range(8)]
construir_tabela(tela_palestras, "PALESTRAS", ["Palestra", "Data", "Local", "Valor", "Duração"], dados_palestras)

# ==========================================
# 6. TELA CONSULTAS
# ==========================================
construir_tabela(tela_consultas, "CONSULTAS", ["Paciente", "Médico", "Data", "Local", "Ações"], dados_consultas)

# ==========================================
# 7. TELA EDITAR CONSULTA
# ==========================================
criar_cabecalho(tela_editar_consulta, mostrar_voltar=True, comando_voltar=lambda: mostrar_tela(tela_consultas))

lbl_tit_editar = tk.Label(tela_editar_consulta, text="EDITAR CONSULTA", font=("Arial", 22, "bold"), fg="#2b8bbb", bg="white")
lbl_tit_editar.pack(pady=(0, 20))

form_frame = tk.Frame(tela_editar_consulta, bg="white")
form_frame.pack(expand=True)

# Linha 1: Paciente + Data
f_linha1 = tk.Frame(form_frame, bg="white")
f_linha1.pack(pady=6)

e_paciente = tk.Entry(f_linha1, font=("Arial", 11), bg="#f0f7fc", fg="#333333", bd=1, relief="solid", width=32)
e_paciente.pack(side="left", padx=5, ipady=8)

e_data = tk.Entry(f_linha1, font=("Arial", 11), bg="#f0f7fc", fg="#333333", bd=1, relief="solid", width=12, justify="center")
e_data.pack(side="left", padx=5, ipady=8)

# Linha 2: Endereço
e_endereco = tk.Entry(form_frame, font=("Arial", 11), bg="#f0f7fc", fg="#333333", bd=1, relief="solid", width=47)
e_endereco.pack(pady=6, ipady=8)

# Linha 3: Recomendações
e_jejum = tk.Entry(form_frame, font=("Arial", 11), bg="#f0f7fc", fg="#333333", bd=1, relief="solid", width=47)
e_jejum.insert(0, "Jejum de 12 horas")
e_jejum.pack(pady=6, ipady=8)

# Linha 4: Médico
e_medico = tk.Entry(form_frame, font=("Arial", 11), bg="#f0f7fc", fg="#333333", bd=1, relief="solid", width=47)
e_medico.pack(pady=6, ipady=8)

# Linha 5: Anexo
e_anexo = tk.Entry(form_frame, font=("Arial", 11), bg="#f0f7fc", fg="#3a8ebd", bd=1, relief="solid", width=47, justify="center")
e_anexo.insert(0, "Anexo ☁️")
e_anexo.pack(pady=6, ipady=8)

# Botão Salvar Edição
btn_salvar_edit = tk.Button(
    form_frame, text="EDITAR", font=("Arial", 11, "bold"), 
    bg="#d6efff", fg="#2b8bbb", highlightbackground="#d6efff",
    activebackground="#2b8bbb", activeforeground="white", 
    bd=0, relief="flat", width=42, command=salvar_edicao_consulta
)
btn_salvar_edit.pack(pady=20, ipady=10)

# INICIAR APLICAÇÃO NA TELA DE LOGIN
mostrar_tela(tela_login)
janela.mainloop()