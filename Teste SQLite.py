#________________________
#UMC
#Programador Luis Carlos e Luiz Gustavo
#atividade de listas 
#06/04/2024 update 26/06/2024
#salario=locale.currency(lista_cliente[dados][1],grouping=True,symbol=True)
#locale.setlocale(locale.LC_ALL,'pt_BR.UTF-8')
#________________________
import os
import locale
import sqlite3
from sqlite_dump import iterdump
conexão=sqlite3.connect("Tabela.db")
cursor=conexão.cursor()
cursor.execute(''' DROP TABLE IF EXISTS Clients;''')
cursor.execute('''create table Clients (
matr integer not null primary key,
nome varchar(50) not null,
cod_seg char(4) not null,
salario integer not null);''')
cursor.execute('''
INSERT INTO Clients
values (111,'Luis','L123',15900.0),
(112,'Carlos','T498',14500.0),
(113,'Teste','82G3',11700.0),
(114,'Exemplo','46P0',13600.0),
(115,'Luk','15A9',17800.0); ''')
conexão.commit 
cursor.close
conexão.close
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
    with sqlite3.connect("Tabela.db") as conexão:
         cursor.execute('''SELECT * FROM Clients''')
         result= cursor.fetchall()
         print(f"{cor_3}{result}{cor_fim}") 
    opc=input(f'''
{cor_1}================= Opções ====================={cor_fim}
{cor_1}[1]{cor_fim} {cor_0}Relatório com os itens da lista{cor_fim}
{cor_1}[2]{cor_fim} {cor_0}Inserir um/alguns novo(s) item(ns) na lista{cor_fim}     
{cor_1}[3]{cor_fim} {cor_0}Alterar algum(ns) item(ns) da lista{cor_fim}   
{cor_1}[4]{cor_fim} {cor_0}Excluir algum(ns) item(ns) da lista{cor_fim}
{cor_1}[5]{cor_fim} {cor_0}Pesquisa por nome na lista{cor_fim}
{cor_1}[6]{cor_fim} {cor_0}Sair do programa{cor_fim}             
{cor_0}Selecione alguma das opções acima:{cor_fim} ''')