import os

import eel


from engine.feutures import findContact
from engine.feutures import *
from engine.command import *


def start():
    eel.init("www")

    playAssistantsound()


    os.system('start msedge.exe --app="http://localhost:8000/index.html"')


    eel.start('index.html', mode=None, host='localhost',  block=True)


