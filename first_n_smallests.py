def first_n_smallest(listaNumeros, elementosTotal):

    if elementosTotal == 0 or not listaNumeros:
        return []

    if elementosTotal == len(listaNumeros):
        return listaNumeros

    listaMenores = []
    maximo = 0
    for posicion, numero in enumerate(listaNumeros[:elementosTotal]):
        listaMenores.append(numero)
        if numero >= maximo:
            maximo = numero

    assert len(listaMenores) == elementosTotal

    for numero in listaNumeros[posicion + 1:]:
        if numero < maximo:
            listaMenores.append(numero)
            maximo = calcularMaximo(listaMenores[:])
            extraerUltimoMaximo(listaMenores, maximo)
            maximo = calcularMaximo(listaMenores[:])
            assert len(listaMenores) == elementosTotal

    return listaMenores


def calcularMaximo(lista):
    lista.sort()
    return lista[-1]


def extraerUltimoMaximo(lista, maximo):
    lista.reverse()
    # try - except necesario
    lista.remove(maximo)
    lista.reverse()


if __name__ == "__main__":  
    assert first_n_smallest([1, 2, 3, 4, 5], 0) == []
    assert first_n_smallest([1, 2, 3, 4, 5], 0) == []
    assert first_n_smallest([5, 4, 3, 2, 1], 3) == [3, 2, 1]