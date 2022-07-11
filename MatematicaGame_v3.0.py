import random
import operator


class Player:
    def __init__(self, name):
        self.score = 0
        self.name = name
        self.index = 0

    def set_score(self):
        self.score += 1

    def set_index(self, index):
        self.index = index


print("\n\n\t\t */*/*/*/**/*/*/*/*/*/*/*/*/*/*/*/*/*/*/"
      "\n\t\t*/*/*/*/* Juego EBR PYTHON S.A /*/*/*/*/*/*"
      "\n\t\t*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/")


def get_result():
    pass


def juego():
    print("\n\n\nHOLA, Este es un juego matemático\nGana el jugador con mas puntos!")
    cant_jugadores = int(input("\nCuantos Jugadores son: "))
    cant_preguntas = int(input("\nCuantas preguntas: "))
    jugadores = []
    resp_jugador = 0

    for i in range(cant_jugadores):
        nombre = input(f"\nJugador {i + 1}: ")
        jugadores.append(Player(nombre))
        jugadores[i].set_index(i)

    for i in range(cant_preguntas):
        for x in jugadores:
            operador = {'*': operator.mul}
            num_1 = random.randint(1, 100)
            num_2 = random.randint(1, 100)
            operacion = random.choice(list(operador.keys()))
            respuesta = operador.get(operacion)(num_1, num_2)

            res1 = 0
            res2 = 0
            res3 = 0
            opciones = [res1, res2, res3]

            print(f'\n\n{x.name} Cuanto es {num_1}{operacion}{num_2}?\n')
            x1 = random.randint(0, 2)

            if x1 == 1:
                opciones[x1] = respuesta
                opciones[x1 + 1] = operador.get(operacion)(num_1, num_2) + random.randint(2, 100)
                opciones[x1 - 1] = operador.get(operacion)(num_1, num_2) + rando3m.randint(2, 100)
            elif x1 == 2:
                opciones[x1] = respuesta
                opciones[x1 - 2] = operador.get(operacion)(num_1, num_2) + random.randint(2, 100)
                opciones[x1 - 1] = operador.get(operacion)(num_1, num_2) + random.randint(2, 100)
            elif x1 == 0:
                opciones[x1] = respuesta
                opciones[x1 + 2] = operador.get(operacion)(num_1, num_2) + random.randint(2, 100)
                opciones[x1 + 1] = operador.get(operacion)(num_1, num_2) + random.randint(2, 100)

            end = False
            while not end:
                try:
                    op = input(f"1 -> {opciones[0]}\t\t2 -> {opciones[1]}\t\t3 ->{opciones[2]}\n\nRESPUESTA: ")
                    resp_jugador = opciones[int(op) - 1]
                    end = True
                except (ValueError, IndexError):
                    print("\n\n\t\t\tError: OPCION INCORRECTA!\n")

            if resp_jugador == respuesta:
                print("\n!C O R R E C T O! Sumaste un punto\n\n")
                x.set_score()
            else:
                print("\n! I N C O R R E C T O !\n\n")

    print("\n\n\nPUNTOS")
    for x in jugadores:
        print(f"{x.name} = {x.score}")

    ganador = None
    max_score = 0
    empate = False
    for x in jugadores:
        if x.index == 0:
            ganador = x
            max_score = x.score
        else:
            if x.score > max_score:
                ganador = x
                max_score = x.score
            elif x.score == max_score:
                empate = True

    if not empate:
        print(f"\nFELICIDADES {ganador.name} HAS GANADO!!!!!\tObtuviste {ganador.score} puntos")
    else:
        print(f"\nEL JUEGO HA QUEDADO EMPATE")


juego()
