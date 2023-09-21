from pico2d import *
import math

open_canvas()

character = load_image("character.png")
grass = load_image("grass.png")

def renderFrame(char_x, char_y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(char_x, char_y)
    delay(0.01)

def runCircle():
    # print("Circle")
    r = 200
    cx, cy = 400, 290
    for deg in range(0, 360, 5):
        x = cx + r * math.cos(math.radians(deg))
        y = cy + r * math.sin(math.radians(deg))
        renderFrame(x, y)

def runRect():
    # print("Rect")

    # bottom(left->right)
    for x in range(50, 750+1, 5):
        renderFrame(x, 90)


while True:
    runCircle()
    runRect()

close_canvas()
