import sqlite3
from contextlib import closing
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, askyesno
from PIL import Image, ImageTk

# Constantes
DB_NAME = "ListaBanco.db"

###########################################################
################ FUNÇÕES ##################################
###########################################################

def conectar_banco():
    return sqlite3.connect(DB_NAME)

def executar_comando(sql, params=()):
    try:
        with conectar_banco() as conexão:
            with closing(conexão.cursor()) as cursor:
                cursor.execute(sql, params)
                conexão.commit()
                return cursor.fetchall()
    except sqlite3.Error as e:
        showinfo(title='Erro', message=f'Erro ao acessar o banco de dados: {e}')
        return []

def My_Select():  # seleciona registros do banco e alimenta a TreeView
    tree.delete(*tree.get_children())  # Apaga registros da Treeview
    reorganizar_tela()
    resultado = executar_comando('''SELECT * FROM Clientes''')
    for i in resultado:
        tree.insert('', END, values=i)  # insere resultado do Select na TreeView

def reorganizar_tela():
    tree.place(x=180, y=25)
    label1.place_forget()
    label2.place_forget()
    label5.place_forget()
    label6.place_forget()
    Matr.place_forget()
    Nome.place_forget()
    Cod.place_forget()
    Sal.place_forget()
    Botao_Save.place_forget()
    Botao_Retornar.place_forget()
    Botao_Alterar.place_forget()
    Botao_Exc['state'] = NORMAL
    Botao_Inc['state'] = NORMAL
    Botao_Alt['state'] = NORMAL
    tree.place(x=180, y=25)
    label3.place(x=180, y=260)
    label4.place(x=180, y=280)
    lbl_NN.place_forget()
    lbl_Sal.place_forget()
    Pesq_Nome.place_forget()
    Pesq_Label.place_forget()
    Botao_Pesquisar.place_forget()
    Botao_Voltar_Geral.place_forget()

def My_Inc():  # prepara tela para inclusão dos dados
    Matr.delete(0, END)  # apaga dados da caixa Entry
    Nome.delete(0, END)
    Cod.delete(0, END)
    Sal.delete(0, END)
    esconder_elementos()
    Botao_Exc['state'] = DISABLED
    Botao_Alt['state'] = DISABLED
    mostrar_elementos_inclusao()

def mostrar_elementos_inclusao():
    label1.place(x=180, y=25)
    label2.place(x=180, y=50)
    label5.place(x=180, y=75)
    label6.place(x=180, y=100)
    Matr.place(x=300, y=25)
    Nome.place(x=285, y=50)
    Cod.place(x=360, y=75)
    Sal.place(x=290, y=100)
    Botao_Save.place(x=180, y=150)
    Botao_Retornar.place(x=300, y=150)

def esconder_elementos():
    tree.place_forget()
    label3.place_forget()
    label4.place_forget()

def Salvar():  # salva no banco dados digitados
    my_cpf = Matr.get()
    my_name = Nome.get()
    my_cod = Cod.get()
    my_sal = Sal.get()
    if my_cpf and my_name and my_cod and my_sal:
        if not executar_comando('''INSERT INTO Clientes (Mátricula, Nome, Cód_Seg, Salário) VALUES (?, ?, ?, ?)''', (my_cpf, my_name, my_cod, my_sal)):
            showinfo(title='Atenção', message='Registro Incluído')
        else:
            showinfo(title='Atenção', message='Matrícula Já Existente')
    else:
        showinfo(title='Erro', message='Preencha todos os campos')
    My_Select()

def My_Exc():  # exclui registro selecionado da TreeView e do banco de dados
    Botao_Inc['state'] = DISABLED
    Botao_Alt['state'] = DISABLED
    if not tree.focus():
        showinfo(title='ERRO', message='Selecione um item para Exclusão')
    else:
        item_selecionado = tree.focus()
        rowid = tree.item(item_selecionado)
        Matr_Exc = (rowid["values"][0])
        answer = askyesno(title='Confirmação', message='Certeza que deseja excluir este item?')
        if answer:
            executar_comando('''DELETE FROM Clientes WHERE Mátricula = ?''', (Matr_Exc,))
            tree.delete(item_selecionado)
    My_Select()

def My_Alt():  # prepara tela para alteração e verifica se há registro selecionado
    Botao_Exc['state'] = DISABLED
    Botao_Inc['state'] = DISABLED
    global Matr_Alt
    global Nome_Alt
    global Cod_Alt
    global Sal_Alt
    Nome.delete(0, END)
    Cod.delete(0, END)
    Sal.delete(0, END)
    if not tree.focus():
        showinfo(title='ERRO', message='Selecione um item para Alteração')
    else:
        item_selecionado = tree.focus()
        rowid = tree.item(item_selecionado)
        Matr_Alt = (rowid["values"][0])
        Nome_Alt = (rowid["values"][1])
        Cod_Alt = (rowid["values"][2])
        Sal_Alt = (rowid["values"][3])
        label3.place_forget()
        label4.place_forget()
        lbl_NN.place(x=180, y=260)
        Nome.insert(0, Nome_Alt)
        Nome.place(x=180, y=285)
        lbl_Sal.place(x=180, y=310)
        Sal.insert(0, Sal_Alt)
        Sal.place(x=180, y=335)
        Botao_Alterar.place(x=180, y=370)
        Botao_Retornar.place(x=180, y=400)

def Alterar():  # realiza a alteração no banco de dados
    Nome_Alt = Nome.get()
    Sal_Alt = Sal.get()
    if Nome_Alt and Sal_Alt:
        executar_comando('''UPDATE Clientes SET Nome = ?, Salário = ? WHERE Mátricula = ?''', (Nome_Alt, Sal_Alt, Matr_Alt))
        selected_item = tree.selection()[0]
        tree.item(selected_item, values=(Matr_Alt, Nome_Alt, Cod_Alt, Sal_Alt))
        showinfo(title='Atenção', message='Registro Alterado')
    else:
        showinfo(title='Erro', message='Preencha todos os campos')
    My_Select()

def My_Pesquisa():  # prepara tela para pesquisa por nome
    esconder_elementos()
    label3.place_forget()
    label4.place_forget()
    Pesq_Label.place(x=180, y=25)
    Pesq_Nome.place(x=180, y=50)
    Botao_Pesquisar.place(x=180, y=75)
    Botao_Retornar.place(x=180, y=100)

def Pesquisar():  # realiza a pesquisa por nome
    nome_pesq = Pesq_Nome.get()
    if nome_pesq:
        resultado = executar_comando('''SELECT * FROM Clientes WHERE Nome LIKE ?''', ('%' + nome_pesq + '%',))
        tree.delete(*tree.get_children())
        for i in resultado:
            tree.insert('', END, values=i)
        tree.place(x=180, y=125)
        # Adiciona botão para voltar ao relatório geral
        Botao_Voltar_Geral.place(x=180, y=300)
    else:
        showinfo(title='Erro', message='Digite um nome para pesquisa')

def Voltar_Geral():  # volta ao relatório geral após pesquisa
    Botao_Voltar_Geral.place_forget()
    My_Select()

###########################################################
############################ Programa Principal############
###########################################################
Janela = Tk()
Janela.title("Sistema de Cadastro de Clientes")  # Titulo da Janela
Janela.geometry('1000x500')  # dimensiona a janela

Tit = Label(Janela, text="Selecione uma das opções abaixo")
Tit.place(x=0, y=0)
Tit["font"] = ("Verdana", 10, "italic", "bold")
Tit["fg"] = "blue"
Tit["bg"] = "white"

Botao_Sel = Button(Janela, text="Relatório Geral", width=15, command=My_Select)
Botao_Sel.place(x=0, y=25)

Botao_Inc = Button(Janela, text="Incluir Funcionário", width=15, command=My_Inc)
Botao_Inc.place(x=0, y=50)

label1 = Label(Janela, text="Entre com a matrícula")
Matr = Entry(Janela, width=10)
label2 = Label(Janela, text="Entre com o nome")
Nome = Entry(Janela, width=30)
label5 = Label(Janela, text="Entre com Código de segurança")
Cod = Entry(Janela, width=10)
label6 = Label(Janela, text="Entre com o Salário")
Sal = Entry(Janela, width=30)

Botao_Save = Button(Janela, text="Salvar Funcionário", width=15, command=Salvar)
Botao_Retornar = Button(Janela, text="Retornar", width=15, command=reorganizar_tela)

Botao_Exc = Button(Janela, text="Excluir Funcionário", width=15, command=My_Exc)
Botao_Exc.place(x=0, y=75)

Botao_Alt = Button(Janela, text="Alterar Informações", width=15, command=My_Alt)
Botao_Alt.place(x=0, y=100)

lbl_NN = Label(Janela, text="Entre com o novo nome")
lbl_Sal = Label(Janela, text="Entre com o novo salário")
Botao_Alterar = Button(Janela, text="Salvar Alterações", width=15, command=Alterar)

Sair = Button(Janela, text="Sair da Aplicação", command=Janela.destroy, width=15)
Sair.place(x=0, y=175)

columns = ('Matricula', 'Nome', 'Cód_Seg', 'Salário')
tree = ttk.Treeview(Janela, columns=columns, show='headings')
tree.heading('Matricula', text='Matrícula do Cliente')
tree.heading('Nome', text='Nome do Cliente')
tree.heading('Cód_Seg', text='Código de segurança do Cliente')
tree.heading('Salário', text='Salário do Cliente')

label3 = Label(Janela, text="Role a tela para baixo com o Mouse")
label3.place(x=180, y=260)
label3["font"] = ("Arial", 8, "bold")
label3["fg"] = "blue"
label3["bg"] = "white"
label4 = Label(Janela, text="Selecione o registro para Alterar/Excluir")
label4.place(x=180, y=280)
label4["font"] = ("Arial", 8, "bold")
label4["fg"] = "red"
label4["bg"] = "white"

Pesq_Label = Label(Janela, text="Digite o nome para pesquisa")
Pesq_Nome = Entry(Janela, width=30)
Botao_Pesquisar = Button(Janela, text="Pesquisar", width=15, command=Pesquisar)

Botao_Pesq = Button(Janela, text="Pesquisar por Nome", width=15, command=My_Pesquisa)
Botao_Pesq.place(x=0, y=150)

Botao_Voltar_Geral = Button(Janela, text="Voltar ao Relatório Geral", width=20, command=Voltar_Geral)

My_Select()  # Executa a função inicial

# Logotipo
image = Image.open("Logo MY.BANK.bmp")
resize_image = image.resize((200, 100))
img = ImageTk.PhotoImage(resize_image)
Logo = Label(Janela, image=img)
Logo.image = img
Logo.place(x=750, y=400)

Janela.mainloop()
