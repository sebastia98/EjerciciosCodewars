def generate_hashtag(cadena):
    hastag = "#"
    cadena = cadena.capitalize()
    if cadena == "" or len(cadena) > 140:
        return False
    espacio = False
    for letra in cadena:
        if letra == " ":
            espacio = True
    if espacio == False:
        hastag += cadena
        return hastag
    elif espacio == True:
        mayuscula = False
        for letra in cadena:
            if mayuscula == True:
                letra = letra.upper()
                hastag += letra
            else:
                hastag += letra
            if letra == " ":
                mayuscula = True
            else:
                mayuscula = False
        return hastag.replace(" ", "")
