import os
os.system("cls")

def converter_para_12h(hora, minu):
    if hora == 0:
        print(f"12:{minu:02d} AM")
    elif 1 <= hora < 12:
        print(f"{hora}:{minu:02d} AM")
    elif hora == 12:
        print(f"12:{minu:02d} PM")
    else:
        print(f"{hora-12}:{minu:02d} PM")

def dozePM(hora, minu):
    if hora == 12:
        print(f"12:{minu:02d} PM")
    elif hora == 13:
        print(f"1:{minu:02d} PM")
    elif hora == 14:
        print(f"2:{minu:02d} PM")
    elif hora == 15:
        print(f"3:{minu:02d} PM")
    elif hora == 16:
        print(f"4:{minu:02d} PM")
    elif hora == 17:
        print(f"5:{minu:02d} PM")
    elif hora == 18:
        print(f"6:{minu:02d} PM")
    elif hora == 19:
        print(f"7:{minu:02d} PM")
    elif hora == 20:
        print(f"8:{minu:02d} PM")
    elif hora == 21:
        print(f"9:{minu:02d} PM")
    elif hora == 22:
        print(f"10:{minu:02d} PM")
    elif hora == 23:
        print(f"11:{minu:02d} PM")

def dozeAM(hora, minu):
    if hora == 0:
        print(f"12:{minu:02d} AM")
    elif hora == 1:
        print(f"01:{minu:02d} AM")
    elif hora == 2:
        print(f"02:{minu:02d} AM")
    elif hora == 3:
        print(f"03:{minu:02d} AM")
    elif hora == 4:
        print(f"04:{minu:02d} AM")
    elif hora == 5:
        print(f"05:{minu:02d} AM")
    elif hora == 6:
        print(f"06:{minu:02d} AM")
    elif hora == 7:
        print(f"07:{minu:02d} AM")
    elif hora == 8:
        print(f"08:{minu:02d} AM")
    elif hora == 9:
        print(f"09:{minu:02d} AM")
    elif hora == 10:
        print(f"10:{minu:02d} AM")
    elif hora == 11:
        print(f"11:{minu:02d} AM")

def vintPM(hora, minu, m_n):
    if m_n.lower() == "pm":
        if hora == 12:
            print(f"12:{minu:02d}")
        elif hora == 1:
            print(f"13:{minu:02d}")
        elif hora == 2:
            print(f"14:{minu:02d}")
        elif hora == 3:
            print(f"15:{minu:02d}")
        elif hora == 4:
            print(f"16:{minu:02d}")
        elif hora == 5:
            print(f"17:{minu:02d}")
        elif hora == 6:
            print(f"18:{minu:02d}")
        elif hora == 7:
            print(f"19:{minu:02d}")
        elif hora == 8:
            print(f"20:{minu:02d}")
        elif hora == 9:
            print(f"21:{minu:02d}")
        elif hora == 10:
            print(f"22:{minu:02d}")
        elif hora == 11:
            print(f"23:{minu:02d}")

def vintAM(hora, minu, m_n):
    if m_n.lower() == "am":
        if hora == 12:
            print(f"00:{minu:02d}")
        elif hora == 1:
            print(f"01:{minu:02d}")
        elif hora == 2:
            print(f"02:{minu:02d}")
        elif hora == 3:
            print(f"03:{minu:02d}")
        elif hora == 4:
            print(f"04:{minu:02d}")
        elif hora == 5:
            print(f"05:{minu:02d}")
        elif hora == 6:
            print(f"06:{minu:02d}")
        elif hora == 7:
            print(f"07:{minu:02d}")
        elif hora == 8:
            print(f"08:{minu:02d}")
        elif hora == 9:
            print(f"09:{minu:02d}")
        elif hora == 10:
            print(f"10:{minu:02d}")
        elif hora == 11:
            print(f"11:{minu:02d}")

print("Programa conversor de horas")
ini = input("Escolha o sistema de horário inicial [a] 12 horas [b] 24 horas\n: ")

if ini.lower() == 'a':
    hora = int(input("Insira a hora desejada (1-12): "))
    if hora <= 0 or hora > 12:
        print("Horário inválido.")
    else:
        minu = int(input("Insira os minutos desejados(00-59): "))
        if minu < 0 or minu > 59:
            print("Minutos inválidos.")
        else:
            m_n = input("Manhã ou noite? (AM ou PM): ")
            if m_n.lower() == ["am","AM"]:
                print(f"O horário inserido: {hora}:{minu:02d} AM\nAgora convertido para o formato 24h:")
                vintAM(hora, minu, m_n)
            elif m_n.lower() == ["pm","PM"]:
                print(f"O horário inserido: {hora}:{minu:02d} PM\nAgora convertido para o formato 24h:")
                vintPM(hora, minu, m_n)
elif ini.lower() == 'b':
    hora = int(input("Insira a hora desejada (00-23): "))
    if hora < 0 or hora > 23:
        print("Horário inválido.")
    else:
        minu = int(input("Insira os minutos desejados (00-59): "))
        if minu < 0 or minu > 59:
            print("Minutos inválidos.")
        else:
            print(f"O horário inserido: {hora}:{minu:02d} no formato 24h")
            print("Agora convertido para o formato 12h:")
            converter_para_12h(hora, minu)
else:
    print("Período inválido.")
