import tkinter as tk
from tkinter import messagebox

email_salvo = ""
senha_salva = ""

modo_formulario = ""
linha_edicao_index = None

dados_pacientes = [
    ["João Silva", "123.456.789-00", "Masculino", "30", "12/09/2026"],
    ["Maria Oliveira", "987.654.321-11", "Feminino", "42", "15/09/2026"],
    ["Carlos Eduardo", "456.789.123-22", "Masculino", "25", "18/09/2026"],
    ["Ana Beatriz", "321.654.987-33", "Feminino", "38", "20/09/2026"],
    ["Lucas Mendes", "654.987.321-44", "Masculino", "50", "22/09/2026"],
    ["Fernanda Lima", "789.123.456-55", "Feminino", "29", "25/09/2026"]
]

dados_palestras = [
    ["Nutrição Esportiva", "15/10/2026", "Auditório A", "R$ 150", "2h"],
    ["Saúde Mental no Trabalho", "20/10/2026", "Sala 3", "Gratuito", "1h 30m"],
    ["Primeiros Socorros", "05/11/2026", "Auditório Principal", "R$ 80", "4h"],
    ["Ergonomia e Postura", "12/11/2026", "Online (Zoom)", "R$ 50", "1h"],
    ["Alimentação Saudável", "01/12/2026", "Auditório B", "R$ 100", "2h"]
]

dados_consultas = [
    ["João Silva", "Dr. Carlos Santos", "12/09/2026", "Maggie Plaza, Suite 204"],
    ["Maria Oliveira", "Dr. Carlos Santos", "14/09/2026", "Av. Paulista, 1000"],
    ["Carlos Eduardo", "Dra. Ana Costa", "18/09/2026", "Rua das Flores, 123"],
    ["Ana Beatriz", "Dr. Carlos Santos", "20/09/2026", "Maggie Plaza, Suite 204"],
    ["Lucas Mendes", "Dra. Ana Costa", "22/09/2026", "Rua das Flores, 123"]
]

def mostrar_tela(tela_para_mostrar):
    tela_para_mostrar.tkraise()
    janela.focus_set()

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

janela = tk.Tk()
janela.geometry("1920x1080")
janela.configure(bg="white")

janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)

tela_login = tk.Frame(janela, bg="white")
tela_cadastro = tk.Frame(janela, bg="white")
tela_dashboard = tk.Frame(janela, bg="white")
tela_pacientes = tk.Frame(janela, bg="white")
tela_palestras = tk.Frame(janela, bg="white")
tela_consultas = tk.Frame(janela, bg="white")
tela_formulario_generico = tk.Frame(janela, bg="white")

todas_as_telas = [
    tela_login, tela_cadastro, tela_dashboard, 
    tela_pacientes, tela_palestras, tela_consultas, tela_formulario_generico
]

for t in todas_as_telas:
    t.grid(row=0, column=0, sticky="nsew")

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

def abrir_formulario(tipo, index=None):
    global modo_formulario, linha_edicao_index
    modo_formulario = tipo
    linha_edicao_index = index

    acao_txt = "EDITAR" if index is not None else "ADICIONAR"
    lbl_tit_form.config(text=f"{acao_txt} {tipo}")

    for f in [frame_campo1, frame_campo2, frame_campo3, frame_campo4, frame_campo5]:
        f.pack_forget()

    for e in [ent1, ent2, ent3, ent4, ent5]:
        e.delete(0, tk.END)

    if tipo == "PACIENTE":
        lbl_c1.config(text="Nome:")
        lbl_c2.config(text="Documento (CPF):")
        lbl_c3.config(text="Sexo:")
        lbl_c4.config(text="Idade:")
        lbl_c5.config(text="Última Consulta:")

        frame_campo1.pack(pady=4)
        frame_campo2.pack(pady=4)
        frame_campo3.pack(pady=4)
        frame_campo4.pack(pady=4)
        frame_campo5.pack(pady=4)

        if index is not None:
            dados = dados_pacientes[index]
            ent1.insert(0, dados[0]); ent2.insert(0, dados[1]); ent3.insert(0, dados[2]); ent4.insert(0, dados[3]); ent5.insert(0, dados[4])

    elif tipo == "PALESTRA":
        lbl_c1.config(text="Título da Palestra:")
        lbl_c2.config(text="Data:")
        lbl_c3.config(text="Local:")
        lbl_c4.config(text="Valor:")
        lbl_c5.config(text="Duração:")

        frame_campo1.pack(pady=4)
        frame_campo2.pack(pady=4)
        frame_campo3.pack(pady=4)
        frame_campo4.pack(pady=4)
        frame_campo5.pack(pady=4)

        if index is not None:
            dados = dados_palestras[index]
            ent1.insert(0, dados[0]); ent2.insert(0, dados[1]); ent3.insert(0, dados[2]); ent4.insert(0, dados[3]); ent5.insert(0, dados[4])

    elif tipo == "CONSULTA":
        lbl_c1.config(text="Paciente:")
        lbl_c2.config(text="Médico:")
        lbl_c3.config(text="Data:")
        lbl_c4.config(text="Local:")

        frame_campo1.pack(pady=4)
        frame_campo2.pack(pady=4)
        frame_campo3.pack(pady=4)
        frame_campo4.pack(pady=4)

        if index is not None:
            dados = dados_consultas[index]
            ent1.insert(0, dados[0]); ent2.insert(0, dados[1]); ent3.insert(0, dados[2]); ent4.insert(0, dados[3])

    mostrar_tela(tela_formulario_generico)
    ent1.focus_set()

def salvar_formulario():
    v1, v2, v3, v4, v5 = ent1.get().strip(), ent2.get().strip(), ent3.get().strip(), ent4.get().strip(), ent5.get().strip()

    if modo_formulario == "PACIENTE":
        novo_registro = [v1, v2, v3, v4, v5]
        if linha_edicao_index is not None:
            dados_pacientes[linha_edicao_index] = novo_registro
        else:
            dados_pacientes.append(novo_registro)
        construir_tabela(tela_pacientes, "PACIENTES", ["Nome", "Documento", "Sexo", "Idade", "Última Consulta", "Ações"], dados_pacientes, "PACIENTE")
        mostrar_tela(tela_pacientes)

    elif modo_formulario == "PALESTRA":
        novo_registro = [v1, v2, v3, v4, v5]
        if linha_edicao_index is not None:
            dados_palestras[linha_edicao_index] = novo_registro
        else:
            dados_palestras.append(novo_registro)
        construir_tabela(tela_palestras, "PALESTRAS", ["Palestra", "Data", "Local", "Valor", "Duração", "Ações"], dados_palestras, "PALESTRA")
        mostrar_tela(tela_palestras)

    elif modo_formulario == "CONSULTA":
        novo_registro = [v1, v2, v3, v4]
        if linha_edicao_index is not None:
            dados_consultas[linha_edicao_index] = novo_registro
        else:
            dados_consultas.append(novo_registro)
        construir_tabela(tela_consultas, "CONSULTAS", ["Paciente", "Médico", "Data", "Local", "Ações"], dados_consultas, "CONSULTA")
        mostrar_tela(tela_consultas)

    messagebox.showinfo("Sucesso", f"{modo_formulario.capitalize()} salvo com sucesso!")

def construir_tabela(parent, titulo, colunas, lista_dados, tipo_entidade):
    for widget in parent.winfo_children():
        widget.destroy()

    criar_cabecalho(parent, mostrar_voltar=True, comando_voltar=lambda: mostrar_tela(tela_dashboard))

    top_bar = tk.Frame(parent, bg="white")
    top_bar.pack(fill="x", padx=100, pady=(0, 15))

    lbl_titulo = tk.Label(top_bar, text=titulo, font=("Arial", 22, "bold"), fg="#2b8bbb", bg="white")
    lbl_titulo.pack(side="left")

    btn_add = tk.Button(
        top_bar, text=f"+ Adicionar {tipo_entidade.capitalize()}", font=("Arial", 10, "bold"),
        bg="#95d6f8", fg="#2b8bbb", highlightbackground="#95d6f8", bd=0, relief="flat", padx=15, pady=6,
        command=lambda: abrir_formulario(tipo_entidade)
    )
    btn_add.pack(side="right")

    table_frame = tk.Frame(parent, bg="white")
    table_frame.pack(expand=True, fill="both", padx=100)

    for col_idx in range(len(colunas)):
        table_frame.grid_columnconfigure(col_idx, weight=1)

    for col_idx, col_nome in enumerate(colunas):
        lbl_col = tk.Label(table_frame, text=col_nome, font=("Arial", 11, "bold"), fg="#2b8bbb", bg="white", pady=8)
        lbl_col.grid(row=0, column=col_idx, sticky="ew")

    if lista_dados:
        for row_idx, item in enumerate(lista_dados, start=1):
            bg_cor = "#f7fafc" if row_idx % 2 == 0 else "white"
            
            for col_idx, valor in enumerate(item):
                lbl_dado = tk.Label(table_frame, text=valor, font=("Arial", 10), fg="#3a8ebd", bg=bg_cor, pady=6)
                lbl_dado.grid(row=row_idx, column=col_idx, sticky="ew")
            
            btn_acao = tk.Label(table_frame, text="Editar", font=("Arial", 10, "bold"), fg="#2b8bbb", bg=bg_cor, cursor="hand2", pady=6)
            btn_acao.grid(row=row_idx, column=len(colunas)-1, sticky="ew")
            
            idx_linha = row_idx - 1
            btn_acao.bind("<Button-1>", lambda e, idx=idx_linha: abrir_formulario(tipo_entidade, idx))

    pagi_frame = tk.Frame(parent, bg="white")
    pagi_frame.pack(pady=15)
    
    for p in ["1", "2", "3", "4", "5", "6"]:
        bg_p = "#2b8bbb" if p == "1" else "white"
        fg_p = "white" if p == "1" else "#2b8bbb"
        btn_p = tk.Label(pagi_frame, text=p, font=("Arial", 9, "bold" if p == "1" else "normal"), fg=fg_p, bg=bg_p, width=3, height=1)
        btn_p.pack(side="left", padx=2)

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

construir_tabela(tela_pacientes, "PACIENTES", ["Nome", "Documento", "Sexo", "Idade", "Última Consulta", "Ações"], dados_pacientes, "PACIENTE")
construir_tabela(tela_palestras, "PALESTRAS", ["Palestra", "Data", "Local", "Valor", "Duração", "Ações"], dados_palestras, "PALESTRA")
construir_tabela(tela_consultas, "CONSULTAS", ["Paciente", "Médico", "Data", "Local", "Ações"], dados_consultas, "CONSULTA")

def voltar_do_formulario():
    if modo_formulario == "PACIENTE": mostrar_tela(tela_pacientes)
    elif modo_formulario == "PALESTRA": mostrar_tela(tela_palestras)
    elif modo_formulario == "CONSULTA": mostrar_tela(tela_consultas)

criar_cabecalho(tela_formulario_generico, mostrar_voltar=True, comando_voltar=voltar_do_formulario)

lbl_tit_form = tk.Label(tela_formulario_generico, text="FORMULÁRIO", font=("Arial", 22, "bold"), fg="#2b8bbb", bg="white")
lbl_tit_form.pack(pady=(0, 15))

form_container = tk.Frame(tela_formulario_generico, bg="white")
form_container.pack(expand=True)

def criar_bloco_campo(parent):
    frame = tk.Frame(parent, bg="white")
    lbl = tk.Label(frame, text="", font=("Arial", 10, "bold"), fg="#3a8ebd", bg="white", anchor="w")
    lbl.pack(fill="x")
    ent = tk.Entry(frame, font=("Arial", 11), bg="#f0f7fc", fg="#333333", bd=1, relief="solid", width=45)
    ent.pack(ipady=7)
    return frame, lbl, ent

frame_campo1, lbl_c1, ent1 = criar_bloco_campo(form_container)
frame_campo2, lbl_c2, ent2 = criar_bloco_campo(form_container)
frame_campo3, lbl_c3, ent3 = criar_bloco_campo(form_container)
frame_campo4, lbl_c4, ent4 = criar_bloco_campo(form_container)
frame_campo5, lbl_c5, ent5 = criar_bloco_campo(form_container)

btn_salvar_form = tk.Button(
    form_container, text="SALVAR", font=("Arial", 11, "bold"), 
    bg="#d6efff", fg="#2b8bbb", highlightbackground="#d6efff",
    activebackground="#2b8bbb", activeforeground="white", 
    bd=0, relief="flat", width=40, command=salvar_formulario
)
btn_salvar_form.pack(pady=20, ipady=8)

mostrar_tela(tela_login)
janela.mainloop()