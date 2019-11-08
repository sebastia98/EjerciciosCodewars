
def permute_a_palindrome(string):
    string=string.lower()
    letras_solas=[]
    letras_sobrantes=[]

    for caracter in string:
        contador_letras=string.count(caracter)
        
        if contador_letras  == 1:
            letras_solas.append(caracter)
        elif contador_letras % 2 != 0 :
            letras_sobrantes.append(caracter)
        
    

    if len(letras_solas) > 1:
        return False
    elif len(letras_solas) >= 1 and len(letras_sobrantes) >= 1:
        return False
    elif len(letras_sobrantes) > 1:
        return False
    else:
        return True
        







