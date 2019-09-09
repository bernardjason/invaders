from tkinter import *
import RunningValues
import Invader
import Bunker
from tkinter import messagebox

colours = ("red", "yellow")

master = Tk()


RunningValues.invader_photo1 = PhotoImage(file="invader.gif")
RunningValues.invader_photo2 = PhotoImage(file="invader2.gif")

master.attributes("-fullscreen", True)
RunningValues.canvas_width = master.winfo_screenwidth()
RunningValues.canvas_height = master.winfo_screenheight()

text_canvas = Canvas(master, bg="black")
text_canvas.pack(fill=X)

RunningValues.score_variable = IntVar()
RunningValues.lives_variable = IntVar()
RunningValues.messages_variable = StringVar()

Label(text_canvas, text="score", bg="black", fg="white").pack(side=LEFT)
score_label = Label(text_canvas, textvariable=RunningValues.score_variable, bg="black", fg="white")
score_label.pack(side=LEFT)

Label(text_canvas, text="lives", bg="black", fg="white").pack(side=LEFT)
lives_label = Label(text_canvas, textvariable=RunningValues.lives_variable, bg="black", fg="white")
lives_label.pack(side=LEFT)
messages_label = Label(text_canvas, textvariable=RunningValues.messages_variable, bg="black", fg="white")
messages_label.pack(side=LEFT)

canvas = Canvas(master,
                bg="black",
                width=RunningValues.canvas_width,
                height=RunningValues.canvas_height)
canvas.pack()

pressedStatus = {"Left": False, "Right": False, "space": False, "Escape": False}


def pressed(event):
    pressedStatus[event.keysym] = True


def released(event):
    pressedStatus[event.keysym] = False


def set_bindings():
    for char in ["Left", "Right", "space", "Escape"]:
        master.bind("<KeyPress-%s>" % char, pressed)
        master.bind("<KeyRelease-%s>" % char, released)


tps_ticker=0
tps_last_ticker=0
time_taken=0
tps_last=0
def render():
    global canvas,tps_ticker,tps_last,tps_last_ticker,time_taken
    xx= RunningValues.unix_time_millis()
    now = RunningValues.unix_time_millis()
    tps_ticker=tps_ticker+1
    if now-tps_last > 1000:
        print(time_taken / (tps_ticker - tps_last_ticker),(tps_ticker - tps_last_ticker))
        tps_last_ticker = tps_ticker
        time_taken = 0
        tps_last=now

    if RunningValues.is_create_player:
        RunningValues.create_player(canvas)

    if pressedStatus["Left"]:
        RunningValues.player.move(-1)
        RunningValues.player_turret.move(-1)

    if pressedStatus["Right"]:
        RunningValues.player.move(1)
        RunningValues.player_turret.move(1)

    if pressedStatus["space"]:
        RunningValues.player_turret.fire()

    if pressedStatus["Escape"]:
        sys.exit(0)

    for f in RunningValues.render_list:
        f.render()

    for f in RunningValues.collision_list:
        for o in RunningValues.render_list:
            if o != f and f.collide(o):
                f.hit(o)
                o.hit(f)


    for d in RunningValues.delete_list:
        del d
    RunningValues.delete_list.clear()

    Invader.invader_group_change()

    and_now = RunningValues.unix_time_millis()
    diff = (and_now - now)

    if Invader.all_dead():
        canvas.delete("all")
        RunningValues.player_dead()
        start_game(RunningValues.score_variable.get(), RunningValues.lives_variable.get())

    if not RunningValues.game_over:
        master.after(int(10 - diff), render)
    else:
        play_again = messagebox.askyesno("Game Over", "score %i new game?" % (RunningValues.score_variable.get()))
        if not play_again:
            sys.exit(0)

        canvas.delete("all")
        RunningValues.player_dead()

        start_game()
        master.after(int(10 - diff), render)

    time_taken = time_taken + RunningValues.unix_time_millis() - xx

def start_game(score=0, lives=3):
    global canvas, pressedStatus
    pressedStatus = {"Left": False, "Right": False, "space": False, "Escape": False}

    for f in RunningValues.render_list:
        del f
    RunningValues.render_list.clear()
    RunningValues.collision_list.clear()

    RunningValues.game_over = False
    Invader.setup(canvas)
    Bunker.setup(canvas)
    RunningValues.lives_variable.set(lives)
    RunningValues.score_variable.set(score)
    RunningValues.messages_variable.set("")
    RunningValues.is_create_player = True


set_bindings()
start_game()
master.after(100, render)

mainloop()
