while True:
 id=int(input("Coloque sua idade: "))
 if id<1 or id>120:
    print("Essa idade não existe")
    break
 if id<16:
    print("Você não pode votar. (não eleitor)")
    break
 if id>=18 and id <=65:
    print("Você é um eleitor obrigatório.")
    break
 else:
    print("Você pode votar se quiser. (eleitor facultativo)")
    break