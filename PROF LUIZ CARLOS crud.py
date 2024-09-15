# Prof Luiz Carlos
# ALP
# Dicionários com listas Pré Projeto Crud
#########################################
import os
### definindo o Dicionário: Matricula: Nome, Salário 
RP={
111:["Luiz",15000],
112:["Fulano",14500],
113:["Sicrano",11000],
114:["Beltrano",13000]
}
while True:
   os.system('cls')
   opt=input('''
    Escolha uma opção:
    [1] Pesquisa por Nome
    [2] Relatório
    [3] Inclusão
    [4] SAIR
    Opção = ''')
   if opt not in ["1","2","3","4"]:
     os.system('cls')
     print ("OPÇÃO INVÁLIDA")
     input ('PRESSIONE ENTER PARA VOLTAR AO MENU')
   elif opt=="1":
     os.system('cls')
     nm=input("Entre com o nome a ser pesquisado: ")
     for chave,dados in RP.items():
        if nm in dados[0]:
          print (f'{chave:^10} {dados[0]:^10} R${dados[1]:^10.2f}')
     input ('PRESSIONE ENTER PARA VOLTAR AO MENU')
   elif opt=="2":
     os.system('cls')
     for chave,dados in RP.items():
        print (f'{chave:^10} {dados[0]:^10} R${dados[1]:^10.2f}')
     input ('PRESSIONE ENTER PARA VOLTAR AO MENU')
   elif opt=="3":
     os.system('cls')
     matr=int(input("entre com a matricula: "))
     if matr not in RP:
      nm=input("entre com o nome: ")
      sal=float(input("entre com o salario: "))
      RP[matr]=[nm,sal]
      print ('Registro Adicionado')
      input ('PRESSIONE ENTER PARA VOLTAR AO MENU')
     else:
       print ("Matricula já existe na Base")
       input ('PRESSIONE ENTER PARA VOLTAR AO MENU')
   elif opt=="4":
     input ("Pressione Enter para Finalizar")
     break