import simpleaudio as sa

filename = '/src/python/invaders/invader.wav'
background = sa.WaveObject.from_wave_file('invader.wav')
invader_hit = sa.WaveObject.from_wave_file('invaderhit.wav')
player_hit = sa.WaveObject.from_wave_file('playerhit.wav')


def play():
    global background
    background.play()


def invader():
    global invader_hit
    invader_hit.play()


def hit():
    global player_hit
    player_hit.play()
