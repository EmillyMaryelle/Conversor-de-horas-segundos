# Conversor-de-horas-segundos

@maryelle822

def relogio_segundos(num_segundos):
    h_minutes = s(num_segundos)
    m_segundos = h_minutes * 3600
    return m_segundos


def h(num_horas):
    minutos = num_horas * 3600
    return minutos

def m(num_horas):
    minutes = h(num_horas)
    segundos = minutes * 3600
    return segundos


def s(num_segundos):
    segundos_horas = num_segundos/3600
    return segundos_horas


escolha=True
while escolha:
    print("""
    1.Converter horas
    2.Converter Segundos
    """)
    escolha= input("Escolha uma opção:  ")
    if escolha=="1":
        print('\n')
        hora = float(input("Horas para converter c/ minutos"))
        print('\n')
        minuto = h(hora)
        segundos = m(hora)
        print(str(hora) + ' horas '+ str(minuto)+'minutos.')
        print(str(hora) + ' horas '
                          '' + str(segundos) + ' segundos.')

    elif escolha=="2":
        print('\n')
        segundo = float(input('Número de segundos '))
        print('\n')
        shoras = s(segundo)
        sminutos = relogio_segundos(segundo)
        print(str(segundo) + ' segundos ' '' + str("{0:.2f}".format(round(shoras, 2))) + ' horas.')
        print(str(segundo) + ' segundos ' ' ' + str("{0:.2f}".format(round(sminutos, 2))) + ' minutos.')

    else:
       print("\n Escolha não válida.\n Tente outra vez.")
