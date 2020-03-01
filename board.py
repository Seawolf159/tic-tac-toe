import pygame


class Board:
    
    def __init__(self):

        self.board = {
            1: [False, 45, 45],
            2: [False, 150, 45],
            3: [False, 250, 45],
            4: [False, 45, 150],
            5: [False, 150, 150],
            6: [False, 250, 150],
            7: [False, 45, 250],
            8: [False, 150, 250],
            9: [False, 250, 250],
        }
