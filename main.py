import arcade
import random

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

R = 25
G = 50
B = 100

class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.Z1 = True
        self.Z2 = True
        self.Z3 = True

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()

    def on_update(self, delta_time):
        global R,G,B
        if(self.Z1):
            if(R > 255):
                self.Z1 = False
            else:
                R += 1
        else:
            if(R < 0):
                self.Z1 = True
            else:
                R -= 1
        if (self.Z2):
            if (G > 255):
                self.Z2 = False
            else:
                G += 1
        else:
            if (G < 0):
                self.Z2 = True
            else:
                G -= 1
        if (self.Z3):
            if (B > 255):
                self.Z3 = False
            else:
                B += 1
        else:
            if (B < 0):
                self.Z3 = True
            else:
                B -= 1

        arcade.set_background_color((R,G,B))

def main():
    my_game = MyGame()
    my_game.setup()
    arcade.run()

main()