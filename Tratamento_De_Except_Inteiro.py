def LeiaInt(msg):
    while True:
        try:
            m=int(input(msg))
        except:
            print(f'\033[0;31mERRO Digite um Numero Inteiro.\033[m')
        else:
            return m