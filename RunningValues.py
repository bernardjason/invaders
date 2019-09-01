from tkinter import *

render_list = list()
canvas_width = 1000
canvas_height = 800

move_down: int = 0
direction:int = -1
next_direction:int = 0
next_down:int = 0

landed_y = canvas_height - 20
game_over = False

score_variable:IntVar
lives_variable:IntVar
messages_variable:StringVar


def down():
    global next_down
    next_down = 8

def invader_group_change():
    global next_direction, direction,next_down , move_down

    if next_direction != 0 :
        direction = next_direction
    if next_down != 0 :
        move_down = next_down
        next_down = 0
    if move_down > 0 :
        move_down=move_down -1

delete_list = list()
