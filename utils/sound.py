import pyxel


def sound_set_up():
    pyxel.sound(0).set(notes='A2C3', tones='TT',
                       volumes='33', effects='NN', speed=10)
    pyxel.sound(1).set(notes='A2C2', tones='TT',
                       volumes='33', effects='NN', speed=10)
    pyxel.sound(3).set(notes=("f0 r a4 r  f0 f0 a4 r" "f0 r a4 r   f0 f0 a4 f0"),
                       tones="n", volumes="1", effects="f", speed=25)
    pyxel.music(0).set([], [], [3], [])
