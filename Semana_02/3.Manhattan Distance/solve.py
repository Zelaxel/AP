def solve(input_list):
    
    # 0º = este, 90º = norte, 180º = oeste, 270º = sur
    distancias = {0:0, 90:0, 180:0, 270:0}
    # Empezamos mirando al norte.
    grados = 90

    # Seguimos el camino.
    for paso in input_list:
        # Giramos.
        if paso[0] == 'L': grados += 90
        else: grados -= 90
        # Ajustamos.
        if grados == 360: grados = 0
        if grados == -90: grados = 270
        # Avanzamos.
        distancias[grados] += int(paso[1:])

    # Devolvemos la distancia absoluta recorrida en los ejes x e y.
    return abs(distancias[0] - distancias[180]) + \
           abs(distancias[90] - distancias[270]) 