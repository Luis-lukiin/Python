#___________________
#UMC
#Luis Carlos
#10/05/2024
#Atividade SQLite
#___________________
import sqlite3
conexão=sqlite3.connect("Tabela.db")
cursor=conexão.cursor()
cursor.execute('''create table usu_cpf (usu_cpf INTEGER PRIMARY KEY, usu_nome VARCHAR(20))''')
conexão.commit()
cursor.close()
conexão.close()