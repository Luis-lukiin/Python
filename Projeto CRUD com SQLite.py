#________________________
#UMC
#Programador Luis Carlos e Luiz Gustavo
#atividade de listas 
#06/04/2024 update 26/06/2024
#salario=locale.currency(lista_cliente[dados][1],grouping=True,symbol=True)
#locale.setlocale(locale.LC_ALL,'pt_BR.UTF-8')
#________________________
import os
lista_cliente={}
import locale
import sqlite3
from sqlite_dump import iterdump
import funcoes as fun
conect=sqlite3.connect("Tabela.db")
cursor=conect.cursor()
cursor.close
conect.close
def diminuir(str):
    max = 4
    if len(str) > max:
        return str[:max]
    else:
        return str
while True:
    os.system('cls')
    locale.setlocale(locale.LC_ALL,'pt_BR.UTF-8')
    cor_2=(f"\033[1;32;40m")
    cor_1=(f"\033[1;32m")
    cor_0=(f"\033[1m")
    cor_3=(f"\033[1;34m")
    cor_4=(f"\033[1;31m")
    cor_fim=(f"\033[0m")
    print(f'''{cor_2}
                                             
         ░█▄█░█░█░░░░█▀▄░█▀█░█▀█░█░█         
         ░█░█░░█░░░░░█▀▄░█▀█░█░█░█▀▄         
         ░▀░▀░░▀░░▀░░▀▀░░▀░▀░▀░▀░▀░▀         
                                             
{cor_fim}''')
    print(f"{cor_1}____________ Sua lista atual é: ____________{cor_fim}")
    print(f"{cor_1}Matr______Nome_____Cód.Seg_________Salário__{cor_fim}")
    with sqlite3.connect("Tabela.db") as conex:
       with closing(conex.cursor()) as cursor:
         cursor.execute('''SELECT * FROM CLients''')
       salario=locale.currency(dados[2],grouping=True,symbol=True)
       print(f"{cor_3}{'Mátricula':<10}{cor_fim}{cor_0}{'dados[0]':<10}{'dados[1]'}\t{salario}{cor_fim}") 
    opc=input(f'''
{cor_1}================= Opções ====================={cor_fim}
{cor_1}[1]{cor_fim} {cor_0}Relatório com os itens da lista{cor_fim}
{cor_1}[2]{cor_fim} {cor_0}Inserir um/alguns novo(s) item(ns) na lista{cor_fim}     
{cor_1}[3]{cor_fim} {cor_0}Alterar algum(ns) item(ns) da lista{cor_fim}   
{cor_1}[4]{cor_fim} {cor_0}Excluir algum(ns) item(ns) da lista{cor_fim}
{cor_1}[5]{cor_fim} {cor_0}Pesquisa por nome na lista{cor_fim}
{cor_1}[6]{cor_fim} {cor_0}Sair do programa{cor_fim}             
{cor_0}Selecione alguma das opções acima:{cor_fim} ''')
    if opc not in ['1','2','3','4','5','6']:
     os.system("cls")
     print(f'''{cor_4}OPÇÃO INVÁLIDA
 ░░░░░░░░░░░█████████████
░░░░░░░░░███░███░░░░░░██
███░░░░░██░░░░██░██████████
████████░░░░░░████░░░░░░░██
████░░░░░░░░░░██░░██████████
████░░░░░░░░░░░███░░░░░░░░░██
████░░░░░░░░░░░██░░██████████
████░░░░░░░░░░░░████░░░░░░░░█
████░░░░░░░░░░░░░███░░████░░█
█████████░░░░░░░░░░████░░░░░█
███░░░░░██░░░░░░░░░░░░░█████
░░░░░░░░░███░░░░░░░██████
░░░░░░░░░░░██░░░░░░██
░░░░░░░░░░░░███░░░░░██
░░░░░░░░░░░░░░██░░░░██
░░░░░░░░░░░░░░░███░░░██
░░░░░░░░░░░░░░░░░██░░░█
░░░░░░░░░░░░░░░░░░█░░░█
░░░░░░░░░░░░░░░░░░██░██
░░░░░░░░░░░░░░░░░░░███{cor_fim}''')
     input(f"{cor_0}Pressione enter para voltar{cor_fim}")
    elif opc == '6' :
     os.system('cls')
     print(f'''{cor_4}Fim do programa{cor_fim}\n{cor_0}Espero que você tenha gostado.{cor_fim}
      _,     _   _    ,_
  .o888P     Y8o8Y     Y888o.
 d88888      88888      88888b
d888888b_  _d88888b_  _d888888b
8888888888888888888888888888888
8888888888888888888888888888888
YJGS8P"Y888P"Y888P"Y888P"Y8888P
 Y888   '8'   Y8P   '8'   888Y
  '8o          V          o8'
    `                     ` ''')
     break
    elif opc == '1' :
     os.system("cls")
     print(f"{cor_0}Relatório das matriculas registradas:{cor_fim}\n")
     for chave,dados in lista_cliente.items():
       salario=locale.currency(dados[2],grouping=True,symbol=True)
       print(f"{cor_3}{chave:<10}{cor_fim}{cor_0}{dados[0]:<10}{dados[1]}\t{salario}{cor_fim}")
       fun.save_txt(lista_cliente)
     input(f"\n{cor_0}Pressione enter para retornar:{cor_fim} ")
    elif opc == '2' :
      while True:
       os.system("cls")
       try:
        novo=int(input(f"{cor_0}Insira o número da matricula:{cor_fim} "))
       except ValueError as error:
         input(f"{cor_4}A matrícula pode conter apenas números, pressione 'enter' e tente novamente.{cor_fim}")
       else:
        if novo not in lista_cliente:
         nm=input(f"{cor_0}Insira o nome a ser registrado:{cor_fim} ")
         n_cont=input(f"{cor_0}Insira o número da sua conta:{cor_fim} ")
         real_n_cont=diminuir(n_cont)
         try:
          sal=float(input(f"{cor_0}Insira o salario correspondente:{cor_fim} "))
         except ValueError as error:
          input(f"{cor_4}O salário pode conter apenas números, pressione 'enter' e tente novamente. (retornando na matrícula){cor_fim}")
         else:
          lista_cliente[novo]=[nm,real_n_cont,sal]
          print(f"{cor_1}Matricula adicionada com êxito!{cor_fim}")
          fun.save_txt(lista_cliente)
          i=input(f"{cor_0}Se quiser adicionar mais elementos para tua lista, pressione {cor_4}'F'{cor_fim}\n{cor_0}Caso contrario pressione {cor_1}'enter'{cor_fim}{cor_0} para retornar ao menu:{cor_fim} ")
          if i not in ['f','F']:
           break
          elif novo in lista_cliente:
           print(f"{cor_4}Esta matricula já está cadastrada{cor_fim}")
           i=input(f"{cor_0}Para tentar novamente pressione {cor_4}'F'{cor_fim}\n{cor_0}Caso contrario pressione {cor_1}'enter'{cor_fim} {cor_0}para retornar ao menu:{cor_fim} ")
           if i not in ['f','F']:
            break
    elif opc == '3':
         while True:
          os.system("cls")
          for chave,dados in lista_cliente.items():
            salario=locale.currency(dados[2],grouping=True,symbol=True)
            print(f"{cor_3}{chave:<10}{cor_fim}{cor_0}{dados[0]:<10}{dados[1]}\t{salario}{cor_fim}")
          try:
           matric=int(input(f"\n{cor_0}Entre com a matricula a ser alterada:{cor_fim} "))
          except ValueError as error:
            input(f"{cor_4}A matrícula pode conter apenas números, pressione 'enter' e tente novamente.{cor_fim}")
          else:
           if matric not in lista_cliente:
            print(f"{cor_4}Esta matricula não existe!{cor_fim}")
            i=input(f"{cor_0}Para tentar novamente pressione {cor_4}'F'{cor_fim}\n{cor_0}Caso contrario pressione {cor_1}'enter'{cor_fim} {cor_0}para retornar ao menu:{cor_fim} ")
            if i not in ['f','F']:
              break
           elif matric in lista_cliente:
            nome=input(f"{cor_0}entre com a alteração do nome{cor_fim} : ")
            n_cont=input(f"{cor_0}Insira o número da sua conta:{cor_fim} ")
            real_n_cont=diminuir(n_cont)
            try:
             sal=float(input(f"{cor_0}entre com a alteração do salário{cor_fim} :"))
            except ValueError as error:
              input(f"{cor_4}O salário pode conter apenas números, pressione 'enter' e tente novamente.{cor_fim}")
            else:
             lista_cliente[matric]=[nome,real_n_cont,sal]
             print(f"{cor_1}Sua lista atualizou!{cor_fim}")
             fun.save_txt(lista_cliente)
             i=input(f"{cor_0}Se quiser alterar mais elementos da tua lista, pressione {cor_4}'F'{cor_fim}\n{cor_0}Caso contrario pressione {cor_1}'enter'{cor_fim} {cor_0}para retornar ao menu:{cor_fim} ")
            if i not in ['f','F']:
              break
    elif opc == '4':
      while True:
        os.system('cls')
        for chave,dados in lista_cliente.items():
          salario=locale.currency(dados[2],grouping=True,symbol=True)
          print(f"{cor_3}{chave:<10}{cor_fim}{cor_0}{dados[0]:<10}{dados[1]}\t{salario}{cor_fim}")
        try:
         delete=int(input(f"{cor_0}indique qual matricula você quer deletar da tua lista:{cor_fim} "))
        except ValueError as error:
         input(f"{cor_4}A matrícula pode conter apenas números, pressione 'enter' e tente novamente.{cor_fim}")
        else:
         if delete not in lista_cliente:
          print(f"{cor_4}Esta matricula não existe!{cor_fim}")
          i=input(f"{cor_0}Para tentar novamente pressione {cor_4}'F'{cor_fim}\n{cor_0}Caso contrario pressione {cor_1}'enter'{cor_fim} {cor_0}para retornar ao menu:{cor_fim} ")
          if i not in ['f','F']:
           break
         else:
          del lista_cliente[delete]
          print(f"{cor_1}Sua lista atualizou!{cor_fim}")
          fun.save_txt(lista_cliente)
          i=input(f"{cor_0}Se quiser deletar mais elementos da tua lista, pressione {cor_4}'F'{cor_fim}\n{cor_0}Caso contrario pressione {cor_1}'enter'{cor_fim} {cor_0}para retornar ao menu:{cor_fim} ")
         if i not in ['f','F']:
          break
    elif opc == "5":
      os.system('cls')
      nm=input(f'''{cor_0}Entre com o nome a ser pesquisado: {cor_fim}''')
      for chave,dados in lista_cliente.items():
        if nm in dados[0]:
          salario=locale.currency(dados[2],grouping=True,symbol=True)
          print(f"{cor_3}{chave:<10}{cor_fim}{cor_0}{dados[0]:<10}{dados[1]}\t{salario}{cor_fim}") 
      input(f"\n{cor_0}Pressione {cor_1}'enter'{cor_fim} {cor_0}para retornar ao menu:{cor_fim} ")