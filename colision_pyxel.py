import pyxel
import math

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.jugador_x = 0
        self.jugador_y = 0
        self.jugador_h = 8
        self.jugador_w = 8
        self.bloque_x = 64
        self.bloque_y = 64
        self.bloque_h = 24
        self.bloque_w = 64

        pyxel.run(self.update, self.draw)

    def update(self):
        #MOVIMIENTOS DEL JUGADOR
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.jugador_x = (self.jugador_x + 8) % pyxel.width

        elif pyxel.btn(pyxel.KEY_LEFT):
            self.jugador_x = (self.jugador_x - 8) % pyxel.width

        elif pyxel.btn(pyxel.KEY_UP):
            self.jugador_y = (self.jugador_y - 8) % pyxel.height

        elif pyxel.btn(pyxel.KEY_DOWN):
            self.jugador_y = (self.jugador_y + 8) % pyxel.height
        #COLISION CON LA PARED



    def draw(self):
        #DIBUJADO
        pyxel.cls(0)
        pyxel.rect(self.jugador_x, self.jugador_y, self.jugador_h, self.jugador_w, 9)
        pyxel.rect(self.bloque_x, self.bloque_y, self.bloque_w, self.bloque_h, 3)
        #Simplificando esto creo?

        #2 COLISIOENES




        #1 COLISION CON LA PARED
        #collides = (self.jugador_x <= self.bloque_x and
        #self.jugador_x + self.jugador_w >= self.bloque_x and
        #self.jugador_y <= self.bloque_y + self.bloque_h and
        #self.jugador_h + self.jugador_y >= self.bloque_y)

        #2 COLISIOENES
        collides = (self.jugador_x >= self.bloque_x
        and self.jugador_x <= self.bloque_x + self.bloque_w
        and self.jugador_y >= self.bloque_y
        and self.jugador_y <= self.bloque_y + self.bloque_h) or (self.jugador_x + self.jugador_w  >= self.bloque_x
        and self.jugador_x + self.jugador_w <= self.bloque_x + self.bloque_w
        and self.jugador_y + self.jugador_h >= self.bloque_y
        and self.jugador_y + self.jugador_h <= self.bloque_y + self.bloque_h)


        if(collides):
            pyxel.text(10, 10, "CONIAZO",15)



App()