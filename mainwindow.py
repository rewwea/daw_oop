from tkinter import *
from creational.singleton import Singleton


class Window(Tk, Singleton):
    def init(self):
        print('calling from __ini__')
        super().__init__()

        def __init__(self):
            print('calling from __ini__')
