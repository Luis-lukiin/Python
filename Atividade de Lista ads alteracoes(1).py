#________________________
#UMC
#Programador Luis Carlos
#atividade de listas 
#06/04/2024
#________________________
lista_cliente=[]
import os 
while True:
    os.system('cls')
    print("Sua lista atual é: ",lista_cliente)
    opc=input('''
================= Opções =====================
[1] Relatório com os itens da lista
[2] Inserir um/alguns novo(s) item(ns) na lista     
[3] Alterar algum(ns) item(ns) da lista   
[4] Excluir algum(ns) item(ns) da lista
[5] Sair do programa
Selecione alguma das opções acima: ''')
    if opc not in ['1','2','3','4','5']:
     os.system("cls")
     print("OPÇÃO INVÁLIDA")
     input("Pressione enter para voltar")
    if opc == '5' :
     os.system('cls')
     print("fim do programa, espero que você tenha gostado.")
     break
    if opc == '1' :
     os.system("cls")
     print("Sua lista e seus indices:\n")
     for ind,val in enumerate(lista_cliente):
            print (ind, " => ", val)
     print("\nSua lista em ordem crescente:\n",sorted(lista_cliente,reverse=False))
     print("Sua lista em ordem decrescente:\n",sorted(lista_cliente,reverse=True)) 
     input("Pressione enter para retornar")
    if opc == '2' :
      while True:
       os.system("cls")
       inserir=input("insira o que voçê quer introduzir na tua lista: ")
       lista_cliente.append(inserir)
       print("atualmente sua lista é: ",lista_cliente,)
       i=input("Se quiser adicionar mais elementos para tua lista, pressione 'F'\nCaso contrario pressione 'enter' para retornar ao menu: ")
       if i not in ['f','F']:
         break
    if opc == '3':
         while True:
          os.system("cls")
          for ind,val in enumerate(lista_cliente):
            print (ind, " => ", val)
          alt=int(input("Entre com o indice a ser alterado: "))
          novo_alt=input("entre com a alteração: ")
          lista_cliente[alt]=novo_alt
          print("Sua lista atualizada: ",lista_cliente,)
          i=input("Se quiser alterar mais elementos da tua lista, pressione 'F'\nCaso contrario pressione 'enter' para retornar ao menu: ")
          if i not in ['f','F']:
            break
    if opc == '4':
      os.system('cls')
      while True:
       for ind,val in enumerate(lista_cliente):
          print (ind, "=>" , val)
       delete=int(input("indique qual elemento você quer deletar da tua lista: "))
       del lista_cliente[delete]
       print("Sua lista atualizada: ",lista_cliente,)
       i=input("Se quiser alterar mais elementos da tua lista, pressione 'F'\nCaso contrario pressione 'enter' para retornar ao menu: ")
       if i not in ['f','F']:
        break