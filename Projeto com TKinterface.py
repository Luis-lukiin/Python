import sqlite3
from contextlib import closing
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno
from PIL import Image, ImageTk 
###########################################################
################ FUNÇÕES ##################################
###########################################################
def My_Select(): # seleciona registros do banco e alimenta a TreeView
    tree.delete(*tree.get_children()) # Apaga registros da Treeview
    tree.place(x=180,y=25) 
    # reorganiza tela
    label1.place_forget()
    label2.place_forget()
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
    tree.place(x=180,y=25) 
    label3.place(x=180,y=260)
    label4.place(x=180,y=280) 
    #Acesso Banco
    with sqlite3.connect("ListaBanco.db") as conexão:
            with closing(conexão.cursor()) as cursor:
                cursor.execute('''select * from Clientes''')
                resultado=cursor.fetchall()
                for i in resultado:
                    tree.insert('', END, values=i)    # insere resultado do Select na TreeView
##########################################################################
def My_Inc(): # prepara tela para inclusão dos dados
     Matr.delete(0, END) # apaga dados da caixa Entry
     Nome.delete(0, END)
     Cod.delete(0, END)
     Sal.delete(0, END)
     tree.place_forget() # esconde widget da tela anterior
     label3.place_forget()
     label4.place_forget()
     Botao_Exc['state'] = DISABLED # desabilita botões desnecessários no modo inclusão
     Botao_Alt['state'] = DISABLED
     label1.place(x=180,y=25) # posiciona widgets de inclusão 
     label2.place(x=180,y=50) 
     label5.place(x=180,y=75)
     label6.place(x=180,y=100)
     Matr.place(x=300,y=25) 
     Nome.place(x=285,y=50)
     Cod.place(x=360,y=75)
     Sal.place(x=290,y=100) 
     Botao_Save.place(x=180,y=150)
     Botao_Retornar.place(x=300,y=150)
def Salvar(): # salva no banco dados digitados
    my_cpf=Matr.get()
    my_name=Nome.get()
    my_cod=Cod.get()
    my_sal=Sal.get()  
    try: 
        with sqlite3.connect("ListaBanco.db") as conexão:        
                with closing(conexão.cursor()) as cursor:
                    cursor.execute('''insert into Clientes (Mátricula, Nome, Cód_Seg, Salário) values (?,?,?,?)''',(my_cpf,my_name,my_cod,my_sal))
                    conexão.commit()
                showinfo(title='Atenção', message='Registro Incluído')
    except sqlite3.IntegrityError: # verificando se registro já existe no banco
         showinfo(title='Atenção', message='Matrícula Já Existente')
##########################################################################
def My_Exc(): # exclui registro selecionado da TreeView e do banco de dados
    Botao_Inc['state'] = DISABLED # desabilita botões desnecessários no modo exclusão
    Botao_Alt['state'] = DISABLED
    if not tree.focus(): # verifica se existe registro selecionado na Tree View
        showinfo(title='ERRO', message='Selecione um item para Exclusão')
        My_Select() # recarrega a TreeView
    else:
        # Coletando qual item está selecionado.
        item_selecionado = tree.focus()
        rowid = tree.item(item_selecionado)
        Matr_Exc = (rowid["values"][0])
        with sqlite3.connect("ListaBanco.db") as conexão:
            with closing(conexão.cursor()) as cursor:
                cursor.execute(f'delete from Clientes where Mátricula = "{Matr_Exc}"')
                answer = askyesno(title='confirmation', message='Certeza que deseja excluir este item?')
                if answer:
                    conexão.commit()
                    tree.delete(item_selecionado)
                    My_Select()
                else:
                    conexão.rollback()
                    My_Select()
##########################################################################
def My_Alt(): # prepara tela para alteração e verifica se há registro selecionado
     Botao_Exc['state'] = DISABLED
     Botao_Inc['state'] = DISABLED
     global Matr_Alt
     global Nome_Alt
     global Sal_alt
     Nome.delete(0, END)
     Sal.delete(0, END)
     if not tree.focus():
        showinfo(title='ERRO', message='Selecione um item para Alteração')
        My_Select()
     else:
        # esconde mensagens de rolagem de página e seleção de itens
        label3.place_forget()
        label4.place_forget()
        # Coletando qual item está selecionado.
        item_selecionado = tree.focus()
        rowid = tree.item(item_selecionado)
        Matr_Alt = (rowid["values"][0])
        Nome_Alt = (rowid["values"][1])
        Sal_alt = (rowid["values"][2])
        # prepara tela e coloca informações para alteração
        lbl_NN.place(x=180,y=260)
        Nome.insert(0, Nome_Alt)
        Nome.place(x=180,y=285)
        Botao_Alterar.place(x=180,y=320) # botões de alterar e retornar
        Botao_Retornar.place(x=180,y=350)
def Alterar(): # realiza a alteração no banco d dados
    Nome_Alt=Nome.get()
    with sqlite3.connect("ListaBanco.db") as conexão:
                with closing(conexão.cursor()) as cursor:
                    cursor.execute(f'update Clientes set Nome = "{Nome_Alt}" where Mátricula = "{Matr_Alt}"')
                    conexão.commit()
    selected_item = tree.selection()[0]
    tree.item(selected_item, text="blub", values=(Matr_Alt,Nome_Alt,Sal_alt))
    showinfo(title='Atenção', message='Registro Alterado')
##########################################################################
##########################################################################
############################ Programa Principal###########################
#### Instancia a classe TK
Janela = Tk()
#### Título e tamanho da janela
Janela.title("Sistema de Cadastro de Clientes") # Titulo da Janela
Janela.geometry('1000x500') # dimensiona a janela
#### Label com instruções iniciais
Tit = Label(Janela, text="Selecione uma das opções abaixo")
Tit.place(x=0,y=0)
Tit["font"] = ("Verdana", "10", "italic", "bold",)
Tit["fg"]=("blue")
Tit["bg"]=("white")
#### Botão Select
Botao_Sel = Button(Janela, text="Relatório Geral",width=15)
Botao_Sel.place(x=0,y=25)
Botao_Sel['command']= My_Select #roda quando o botão é acionado
###########################################################
################ ROTINAS PARA INCLUSÃO DE DADOS############
###########################################################
# Botão Inclusão
Botao_Inc = Button(Janela, text="Incluir funcionário",width=15)
Botao_Inc.place(x=0,y=50)
Botao_Inc['command']=My_Inc # Altera a tela para inclusão de dados
#### Cria caixas e labels para entrada de dados
label1 = Label (Janela, text = "Entre com a matricula")
Matr = Entry(Janela,width=10)
label2 = Label (Janela, text = "Entre com o nome")
Nome = Entry(Janela,width=30)
label5 = Label (Janela, text = "Entre com Código de segurança")
Cod = Entry(Janela,width=10)
label6 = Label (Janela, text = "Entre com o Salário")
Sal = Entry(Janela,width=30)
# Botão para e função para salvar dados digitados
Botao_Save = Button(Janela, text="Incluir funcionário",width=15)
Botao_Save['command']=Salvar # inclui no banco os dados digitados
#### Botão retornar
Botao_Retornar = Button(Janela, text="Retornar",width=15,command=My_Select)
##############################################################
################ ROTINAS PARA EXCLUSÃO DE DADOS##############
##############################################################
Botao_Exc = Button(Janela, text="Excluir Funcionário",width=15)
Botao_Exc.place(x=0,y=75)
Botao_Exc['command']=My_Exc # função para exclusão de dados
##############################################################
################ ROTINAS PARA ALTERAÇÃO DE DADOS##############
##############################################################
#### Botão Alterar
Botao_Alt = Button(Janela, text="Alterar Informações",width=15)
Botao_Alt.place(x=0,y=100)
lbl_NN = Label (Janela, text = "Entre com o novo nome")
Botao_Alt['command']=My_Alt
Botao_Alterar = Button(Janela, text="Salvar Alterações",width=15)
Botao_Alterar['command']=Alterar
##############################################################
########################## Botão Sair#########################
###########################################################
Sair= Button(Janela, text="Sair da Aplicação", command=Janela.destroy,width=15)
Sair.place(x=0,y=125)
##############################################################
################ ROTINAS CRIAÇÃO EXIBIÇÃO DA TREEVIEW#########
##############################################################
#### TreeView - define columns Treeview
columns = ('Matricula', 'Nome', 'Cód_Seg', 'Salário')
tree = ttk.Treeview(Janela, columns=columns, show='headings')
# define headings
tree.heading('Matricula', text='Matrícula do Cliente')
tree.heading('Nome', text='Nome do Cliente')
tree.heading('Cód_Seg', text='Código de segurança do Cliente')
tree.heading('Salário', text='Salário do Cliente')
#### Exibe a TreeView
label3 = Label (Janela, text = "Role a tela para baixo com o Mouse")
label3.place(x=180,y=260) 
label3["font"] = ("Arial","8","bold",)
label3["fg"]=("blue")
label3["bg"]=("white")
label4 = Label (Janela, text = "Selecione o registro para Alterar/Excluir")
label4.place(x=180,y=280)
label4["font"] = ("Arial","8","bold",)
label4["fg"]=("red")
label4["bg"]=("white")
My_Select() #Executa a função
##############################################################
################ LOGOTIPO ####################################
##############################################################
# Read the Image
image = Image.open("Logo MY.BANK.bmp")
resize_image = image.resize((200, 100))
img = ImageTk.PhotoImage(resize_image)
Logo = Label(image=img)
Logo.image = img
Logo.place(x=425,y=300)
Janela.mainloop()