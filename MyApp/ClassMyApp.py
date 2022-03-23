import pathlib
import tkinter as tk
import tkinter.ttk as ttk
import pygubu

from ClassGamePad import ClassGamePad

PROJECT_PATH = './'
PROJECT_UI = './MyApp.ui'


class ClassMyApp:

    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)

        # main window
        self.main_window = builder.get_object('toplevelMain', master)
        self.main_window.resizable(width=False, height=False)

        # game pad window
        self.game_pad_window = builder.get_object('toplevelGamePad')
        self.game_pad_window.resizable(width=False, height=False)
        # self.game_pad_window.iconify()
        self.game_pad_window.withdraw()

        builder.connect_callbacks(self)

        # Instantiate hardware communication classes
        self.game_pad = ClassGamePad()

    # game pad callbacks
    def callbackGamePadConnect(self):
        self.game_pad_window.deiconify()
        self.game_pad.connect(0)
        self.callbackGamePadTimer()

    def callbackGamePadDisconnect(self):
        self.game_pad_window.withdraw()
        self.game_pad.disconnect()

    def callbackGamePadTimer(self):
        print('Timer gamepad called ...')

        self.game_pad.getData()
        formatted_axis0 = str(round(self.game_pad.axis0 * 100)/100)
        formatted_axis1 = str(round(self.game_pad.axis1 * 100)/100)
        self.builder.get_variable('entryAxis0TextVariable').set(formatted_axis0)
        self.builder.get_variable('entryAxis1TextVariable').set(formatted_axis1)

        self.game_pad_window.after(100, self.callbackGamePadTimer)




    # main window callbacks
    def callbackCommandExit(self):
        print('bye bye!')
        exit(0)

    def run(self):
        self.main_window.mainloop()
