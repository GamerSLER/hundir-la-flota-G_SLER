from barco import Barco
from mapa import Mapa
barcos_disponibles = ['portaviones', 'acorazado', 'destructor', 'fragata']

mapa_jugador_1 = Mapa()
mapa_jugador_1.rellenarMapa()
barcos_jugador_1 = []
for fila in mapa_jugador_1.get_mapa_oculto():
    for columna in fila:
        print(columna, end="\t\t")
    print("\n")

for i in range(4):
    barco_valido = False
    while not barco_valido:
        barco = Barco(barcos_disponibles[i])
        barcos_jugador_1.append(barco)
        print(barco.get_longitud())
        try:
            mapa_jugador_1.posicionar_barco(
                barco,
                input(f"En qué orientación deseas poner el barco ({barcos_disponibles[i]})? ('V'ertical o 'H'orizontal):"),
                int(input("Introduzca la coordenada x en la que empieza el barco: ")),
                int(input("Introduzca la coordenada y en la que empieza el barco: "))
            )
            barco_valido = True
            mapa_jugador_1.get_diseno()
        except ValueError as e:
            barcos_jugador_1.pop()
            print(e)


for i in range(4):
    mapa_jugador_1.golpear(int(input("Coordenada x para atacar: ")), int(input("Coordenada y para atacar: ")))
    mapa_jugador_1.get_diseno()


mapa_jugador_2 = Mapa()
mapa_jugador_2.rellenarMapa()