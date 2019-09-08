from tkinter import *
from time import time
from Player import Player
from PlayerTurret import PlayerTurret

render_list = list()
canvas_width = 1000
canvas_height = 800

is_create_player = True
player: Player
player_turret: PlayerTurret

game_over = False

score_variable: IntVar
lives_variable: IntVar
messages_variable: StringVar

invader_photo1: PhotoImage
invader_photo2: PhotoImage


def unix_time_millis():
    return int(time() * 1000)


def create_player(canvas):
    global render_list, is_create_player, player, player_turret
    player = Player(canvas, canvas_width, canvas_height)
    player_turret = PlayerTurret(canvas, canvas_width, canvas_height)
    render_list.append(player)
    render_list.append(player_turret)
    is_create_player = False


def player_dead():
    global render_list, is_create_player, player, player_turret, lives_variable, game_over
    player.cleanup()
    player_turret.cleanup()
    if player in render_list:
        render_list.remove(player)
    if player_turret in render_list:
        render_list.remove(player_turret)

    if lives_variable.get() <= 0:
        game_over = True
    else:
        is_create_player = True


delete_list = list()
