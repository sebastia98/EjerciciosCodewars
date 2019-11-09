def countBits(entero):
    contador = 1
    if entero == 0:
        return 0
    while entero > 1:
        if entero % 2 == 1:
            contador += 1
        entero = entero // 2
    return contador