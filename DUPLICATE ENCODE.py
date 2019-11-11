def duplicate_encode(word):
    word_encoded=""
    word=word.lower()
    for caracter in word:
        cont=word.count(caracter)
        if cont > 1:
            word_encoded=word_encoded+")"
        else:
            word_encoded=word_encoded+"("
    return word_encoded
        

        