# El joven periodista Ricardo Jorge debe relatar un partido de tenis, pero no conoce las reglas
# del deporte. En particular, no ha logrado aprender cómo saber si un set ya terminó, y quién lo
# ganó.
# Un partido de tenis se divide en sets. Para ganar un set, un jugador debe ganar 6 juegos, pero
# además debe haber ganado por lo menos dos juegos más que su rival. Si el set está empatado
# a 5 juegos, el ganador es el primero que llegue a 7. Si el set está empatado a 6 juegos, el set
# se define en un último juego, en cuyo caso el resultado final es 7-6.
# Sabiendo que el jugador A ha ganado m juegos, y el jugador B, n juegos, al periodista le
# gustaría saber:
# ● si A ganó el set, o
# ● si B ganó el set, o
# ● si el set todavía no termina, o
# ● si el resultado es inválido (por ejemplo, 8-6 o 7-3).

set_jugador_a = int(input("Ingrese número de SET del Jugador A: "))
set_jugador_b = int(input("Ingrese número de SET del Jugador B: "))

if set_jugador_a <= 7 and set_jugador_b <= 7:
    if set_jugador_a >= 6 or set_jugador_b >= 6:
        if set_jugador_a >= 6 and set_jugador_a - set_jugador_b >= 2:
            print("Ganador: Jugador A")
        elif set_jugador_b >= 6 and set_jugador_b - set_jugador_a >= 2:
            print("Ganador: Jugador B")
        elif set_jugador_a == 7 and set_jugador_b == 6:
            print("Ganador: Jugador A (Resultado final: 7-6)")
        elif set_jugador_b == 7 and set_jugador_a == 6:
            print("Ganador: Jugador B (Resultado final: 7-6)")
        else:
            print("El set todavía no termina")
    else:
        print("El set todavía no termina")
else:
    print("Resultado inválido")
