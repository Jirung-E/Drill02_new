from pico2d import *
import math

open_canvas()

character = load_image("character.png")
grass = load_image("grass.png")

def runCircle():
    # print("Circle")
    r = 200
    for deg in range(0, 360, 5):
        x = r * math.cos(math.radians(deg))
        y = r * math.sin(math.radians(deg))
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)

def runRect():
    # print("Rect")
    pass


while True:
    clear_canvas_now()
    grass.draw_now(400, 30)

    runRect()
    runCircle()

    delay(0.01)

close_canvas()
