def solve(input_list):
    disx = 0
    disy = 0

    dir = "north"

    for next in input_list:
        
        # Mira al norte.
        if dir == "north":
            # Derecha.
            if next[0] == "R":
                dir = "east"
                disx += int(next[1:])
            # Izquierda.
            else:
                dir = "west"
                disx -= int(next[1:])

        # Mira al sur.
        elif dir == "south":
            # Derecha.
            if next[0] == "R":
                dir = "west"
                disx -= int(next[1:])
            # Izquierda.
            else:
                dir = "east"
                disx += int(next[1:])
            
        # Mira al este.
        elif dir == "east":
            # Derecha.
            if next[0] == "R":
                dir = "south"
                disy -= int(next[1:])
            # Izquierda.
            else:
                dir = "north"
                disy += int(next[1:])

        else:
            # Derecha.
            if next[0] == "R":
                dir = "north"
                disy += int(next[1:])
            # Izquierda.
            else:
                dir = "south"
                disy -= int(next[1:])

    return abs(disx) + abs(disy)