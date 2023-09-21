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
        x = cx + r * math.cos(math.radians(deg - 90))
        y = cy + r * math.sin(math.radians(deg - 90))
        renderFrame(x, y)

def runRect():
    # print("Rect")

    # bottom(left->right)
    for x in range(50, 750+1, 5):
        renderFrame(x, 90)

    # right(bottom->top)
    for y in range(90, 550+1, 5):
        renderFrame(750, y)

    # top(right->left)
    for x in range(750, 50-1, -5):
        renderFrame(x, 550)

    # left(top->bottom)
    for y in range(550, 90-1, -5):
        renderFrame(50, y)




while True:
    runCircle()
    break
    # runRect()

close_canvas()
