from pico2d import *
import math

open_canvas()

character = load_image("character.png")
grass = load_image("grass.png")

def runCircle():
    # print("Circle")
    r = 200
    cx, cy = 400, 290
    for deg in range(0, 360, 5):
        x = cx + r * math.cos(math.radians(deg))
        y = cy + r * math.sin(math.radians(deg))
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)

def runRect():
    # print("Rect")

    # bottom
    for x in range(50, 750+1, 5):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        delay(0.01)


while True:
    runRect()
    # runCircle()

close_canvas()
