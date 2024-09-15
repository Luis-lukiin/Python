#UMC 
#Programador Luís 
#atividade oper logic questão 11
#20/03/2024
print("Programa para avaliar sua faixa etária")
try:
    idade=int(input("Insira sua idade: "))
except: ValueError
print("Valor incorreto, idade apenas em número inteiro.")
if idade <= 12:
    print ("Sua faixa etária é criança.")
elif idade >=12 and idade <=17 :
    print("Sua faixa etária é adolecente.")
elif idade >=18 and idade <=59 :
    print("Sua faixa etária é adulto.")
else:
    print("Sua faixa etária é idoso.")
print("espero que tenha gostado :)")
input("Pressione enter para sair")