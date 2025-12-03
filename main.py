from barco import barco
import random as r

barcos_jugador1 = [barco(1, 1), barco(2, 2), barco(3, 3), barco(4, 4)]
barcos_jugador2 = [barco(1, 1), barco(2, 2), barco(3, 3), barco(4, 4)]

def generarMapa():
    mapa_battleship = []
    tamano_mapa = r.randint(7, 10)
    for i in range(tamano_mapa):
        mapa_battleship.append({})
        for j in range(tamano_mapa):
            mapa_battleship[i].append("•")
    return mapa_battleship
mapa_battleship_jugador1 = generarMapa()
mapa_battleship_jugador2 = generarMapa()
    
def mostrarMapa(mapa):
    for fila in mapa:
        print(fila)
        
def colocarBarco():
# Barco: 🚢 
    print("BARCOS")
    for i in range(4):
        posX_barco = int(input(f"Coordenada x del barco de tamaño {i}:  "))
        posY_barco = int(input(f"Coordenada y del barco de tamaño {i}:  "))
        direccion = input("En horizontal ('H') o vertical ('V'):  ")

def colocarBomba():
    bomba = "💥"
    print("BOMBA")
    posX_bomba = int(input("Coordenada x de la bomba: "))
    posY_bomba = int(input("Coordenada y de la bomba: "))

def main():
    pass