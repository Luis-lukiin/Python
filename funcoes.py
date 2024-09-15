def load_txt ():
  l0=[]
  lista_cliente={}
  with open ('dados.txt','r') as Dados:
    for i in Dados:
      l0.append(i.rstrip().split(","))
    for i in l0:
      chave=int(i[0])
      valor=float(i[3])
      lista_cliente[chave]=[i[1],i[2],valor]
    return lista_cliente 
def save_txt(Dict):
  with open ("dados.txt","w") as Dados:
    for chave, dados in Dict.items():
      Dados.write (f"{chave},{dados[0]},{dados[1]},{dados[2]}\n")