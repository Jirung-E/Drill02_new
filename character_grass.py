from pico2d import *
import math

open_canvas()

character = load_image("character.png")
grass = load_image("grass.png")

def runCircle():
    print("Circle")
    pass

def runRect():
    print("Rect")
    pass



while True:
    clear_canvas_now()
    grass.draw_now(400, 30)

    runCircle()
    runRect()

    delay(0.01)

close_canvas()
