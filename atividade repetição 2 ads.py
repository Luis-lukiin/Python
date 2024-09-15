#UMC
#Programador Luís Carlos
#atividade repetição ads
#30/03/2024
print("programa para ler seu número inteiro")
N=int(input("insíra um número maior que 1 e contaremos todos os outros antes dele: "))
while N <= 1 :
    print("OPÇÃO INVÁLIDA.. por favor insira um número maior que 1")
    break
i=1
while i <= N :
    print(i)
    i+=1
