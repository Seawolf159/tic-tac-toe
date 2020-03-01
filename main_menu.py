import os
import tkinter as tk
from tkinter import *

MAIN_DIR = os.path.dirname(__file__)
IMAGES_DIR = os.path.join(MAIN_DIR, os.path.abspath("assets/images"))


class MainMenu:

    def __init__(self):
        self.parent = tk.Tk()
        self.parent.iconbitmap(os.path.join(IMAGES_DIR, "game_icon.ico"))
        self.parent.title("Tic-Tac-Toe")
        self.parent.geometry("300x200")
        self.parent.resizable(0, 0)
        self.parent.protocol("WM_DELETE_WINDOW", self.close_main_menu)

        self.mode = None

        self.human_opponent_frame = Frame(self.parent, 
                                          width=300, 
                                          height=100)
        self.human_opponent_frame.pack_propagate(0)
        self.human_opponent_frame.pack()

        self.computer_opponent_frame = Frame(self.parent, 
                                             width=300, 
                                             height=100)
        self.computer_opponent_frame.pack_propagate(0)
        self.computer_opponent_frame.pack()

        self.human_opponent_button = tk.Button(self.human_opponent_frame,
                                        text="Play against human",
                                        command=self.play_human)
        self.human_opponent_button.pack(fill=BOTH, expand=1)
        self.computer_opponent_button = tk.Button(self.computer_opponent_frame,
                                           text="Play against computer",
                                           command=self.play_computer)
        self.computer_opponent_button.pack(fill=BOTH, expand=1)
        self.parent.mainloop()

    def play_human(self):
        self.mode = "human"
        self.close_main_menu()

    def play_computer(self):
        self.mode = "computer"
        self.close_main_menu()

    def close_main_menu(self):
        self.parent.destroy()
