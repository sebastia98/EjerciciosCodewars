def queue_time(consumidores, cajas):
    if len(consumidores) == 1:
        return consumidores[0]
    elif cajas == 1:
        suma = 0
        for elemento in consumidores:
            suma += elemento
        return suma
    elif len(consumidores) <= cajas:
        consumidores = sorted(consumidores)
        return consumidores[len(consumidores) - 1]
    else:
        