from tkinter import *
from Player import Player
from PlayerTurret import PlayerTurret
from time import time
import RunningValues
from Invader import Invader


colours = ("red", "yellow")


master = Tk()
text_canvas = Canvas(master,bg="black")
text_canvas.pack(fill=X)

RunningValues.score_variable = IntVar()
RunningValues.lives_variable = IntVar()
RunningValues.lives_variable.set(100)
RunningValues.messages_variable = StringVar()


Label(text_canvas, text="score",bg="black", fg="white").pack(side=LEFT)
score_label=Label(text_canvas, textvariable=RunningValues.score_variable, bg="black",fg="white")
score_label.pack(side=LEFT)

Label(text_canvas, text="lives",bg="black", fg="white").pack(side=LEFT)
lives_label=Label(text_canvas, textvariable=RunningValues.lives_variable, bg="black",fg="white")
lives_label.pack(side=LEFT)
messages_label=Label(text_canvas, textvariable=RunningValues.messages_variable, bg="black",fg="white")
messages_label.pack(side=LEFT)


canvas = Canvas(master,
                bg="black",
           width=RunningValues.canvas_width,
           height=RunningValues.canvas_height)
canvas.pack()

player = Player(canvas,RunningValues.canvas_width,RunningValues.canvas_height)
player_turret = PlayerTurret(canvas,RunningValues.canvas_width,RunningValues.canvas_height)

RunningValues.render_list.append(player)
RunningValues.render_list.append(player_turret)
space_between_x = 50
space_between_y = 50
for xx in range(1,11):
    for yy in range(1,7):
        RunningValues.render_list.append(Invader(canvas, RunningValues.canvas_width-xx*space_between_x , yy * space_between_y))

def key(event):
    if event.char == event.keysym:
        msg = 'Normal Key %r' % event.char
    elif len(event.char) == 1:
        msg = 'Punctuation Key %r (%r)' % (event.keysym, event.char)
    else:
        msg = 'Special Key %r' % event.keysym

    if event.keysym == "Right" :
        player.move(1)
        player_turret.move(1)
    elif event.keysym == "Left" :
        player.move(-1)
        player_turret.move(-1)
    elif event.keysym == "space" : player_turret.fire()


def unix_time_millis():

    return int(time() * 1000 )


def render():
    now = unix_time_millis()
    for f in RunningValues.render_list:
        f.render()

    for f in RunningValues.render_list:
        for o in RunningValues.render_list:
            if o != f and f.collide(o) :
                f.hit(o)
                o.hit(f)


    for d in RunningValues.delete_list:
        del d
    RunningValues.delete_list.clear()

    RunningValues.invader_group_change()


    and_now = unix_time_millis()
    diff =  (and_now - now)
    if not RunningValues.game_over :
        master.after( int(10 - diff ) , render)
    else :
        RunningValues.messages_variable.set("GAME OVER")
    microseconds = now


master.bind_all('<Key>', key)

master.after(100, render)

mainloop()

