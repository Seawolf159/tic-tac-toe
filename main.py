"""Basic Tic-Tac-Toe game."""

__version__ = "1"

import copy
import os
import random
import tkinter
from tkinter import messagebox

import pygame

from board import Board
from computer_player import ComputerPlayer
from main_menu import MainMenu
from player import Player

MAIN_DIR = os.path.dirname(__file__)
IMAGES_DIR = os.path.join(MAIN_DIR, os.path.abspath("assets/images"))


def load_image(image_name):
    """Load an image from the assets/images subdirectory.
    Images are converted as i am told that this will be faster.
    """  

    image = pygame.image.load(os.path.join(IMAGES_DIR, image_name)).convert()
    return image


def make_computer_move(screen, board, player, p3, turn, move_added=None):
    """Function to figure out the best move for the computer to play.
    
    TODO: The computer player sucks right now. Fix it.
    Currently the computer will never choose to make a worse move.

    TODO: Update text to reflect how it actually ends up doing it.
    Uses recursion and backtracking to make a list of best moves and if no 
    moves win immediately, pick one of the best moves at random.
    """

    # Condition for breaking the recursion and coming back to the normal world.
    # If the computer ends up winning on the final board, return the best 
    # options that will lead to his victory.

    if check_ended(board, p3) == True:
        return
    else:
        # TODO: Change this so that the player can choose if it'll be "X" or 
        # "O". Right now computer will always be player "X".
        if turn % 2 != 0:
            active_player = p3
        else:
            active_player = player

        for square, value in board.items():
            if value[0] == False:
                p3.move = square
                board[square][0] = active_player.marker
                make_computer_move(screen, board, player, p3, turn + 1)
                board[square][0] = False


def place_marker(screen, board, player):
    """Place a marker in the clicked position, if the square is empty."""

    if player.pos[0] >= 0 and player.pos[0] <= 90:
        if player.pos[1] >= 0 and player.pos[1] <= 90:
            if not board[1][0]:
                board[1][0] = player.marker
                screen.blit(player.marker_image, (0, 0))
                return True
        elif player.pos[1] >= 110 and player.pos[1] <= 190:
            if not board[4][0]:
                board[4][0] = player.marker
                screen.blit(player.marker_image, (0, 110))
                return True
        elif player.pos[1] >= 210 and player.pos[1] <= 300:
            if not board[7][0]:
                board[7][0] = player.marker
                screen.blit(player.marker_image, (0, 210))
                return True
    elif player.pos[0] >= 110 and player.pos[0] <= 190:
        if player.pos[1] >= 0 and player.pos[1] <= 90:
            if not board[2][0]:
                board[2][0] = player.marker
                screen.blit(player.marker_image, (110, 0))
                return True
        elif player.pos[1] >= 110 and player.pos[1] <= 190:
            if not board[5][0]:
                board[5][0] = player.marker
                screen.blit(player.marker_image, (110, 110))
                return True
        elif player.pos[1] >= 210 and player.pos[1] <= 300:
            if not board[8][0]:
                board[8][0] = player.marker
                screen.blit(player.marker_image, (110, 210))
                return True
    elif player.pos[0] >= 210 and player.pos[0] <= 300:
        if player.pos[1] >= 0 and player.pos[1] <= 90:
            if not board[3][0]:
                board[3][0] = player.marker
                screen.blit(player.marker_image, (210, 0))
                return True
        elif player.pos[1] >= 110 and player.pos[1] <= 190:
            if not board[6][0]:
                board[6][0] = player.marker
                screen.blit(player.marker_image, (210, 110))
                return True
        elif player.pos[1] >= 210 and player.pos[1] <= 300:
            if not board[9][0]:
                board[9][0] = player.marker
                screen.blit(player.marker_image, (210, 210))
                return True
    return False


def place_computer_marker(screen, board, player):
    board[player.move][0] = player.marker
    screen.blit(player.marker_image, board[player.move][1])
    pygame.display.update()


def check_ended(board, player):
    """Check the board if anyone has three in a row."""

    # Check Horizontal win condition
    horizontal = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for row in horizontal:
        for square in row:
            if board[square][0] == player.marker:
                continue
            else:
                break
        else:
            return True

    # Check Vertical win condition
    vertical = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    for column in vertical:
        for square in column:
            if board[square][0] == player.marker:
                continue
            else:
                break
        else:
            return True

    # Check Diagonal win condition
    diagonal = [[1, 5, 9], [3, 5, 7]]
    for slash in diagonal:
        for square in slash:
            if board[square][0] == player.marker:
                continue
            else:
                break
        else:
            return True

    # Check if it is a draw
    for square_state in board.values():
        if square_state[0] == False:
            break
    else:
        return "draw"
    return False



def game_end(winner):
    """End of game message.
    The game has either been won by someone or resulted in a draw and this 
    function will show you a message asking you if you want to play again and 
    you are able to click a button saying yes or no.
    """
    if winner in ["X", "O"]:
        game_end_text = (f"The game is over. Player {winner} won!" 
            " Do you want to play again?")
    elif winner == "draw":
        game_end_text = ("The game is a draw. No player is victorious. Do you"
        " want to play again?")
    root = tkinter.Tk()
    root.wm_withdraw()
    result = messagebox.askyesno(title="Play again?", message=game_end_text)
    root.destroy()
    return result


def main(main_menu):
    """Main function for the game."""

    pygame.init()

    # Initiate the playing board as a dictionary. Looks as follows:
    # "one" | "two" | "three"
    # ------------
    # "four" | "five" | "six"
    # ------------
    # "seven" | "eight" | "nine"
    # place_marker() sets the values as one of ["X", "O"] when a move has been 
    # made. 
    # the (0, 0) part in [False, (0, 0)] is the top left position of the square
    # in pixels. This is only used for placing the computer moves on the board.
    board = {
        1: [False, (0, 0)],
        2: [False, (110, 0)],
        3: [False, (210, 0)],
        4: [False, (0, 110)],
        5: [False, (110, 110)],
        6: [False, (210, 110)],
        7: [False, (0, 210)],
        8: [False, (110, 210)],
        9: [False, (210, 210)],
    }

    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("Tic-Tac-Toe")
    pygame.display.set_icon(pygame.image.load(os.path.join(IMAGES_DIR, 
        "game_icon.png")))
    background = load_image("board_grid.png")
    screen.blit(background, (0, 0))
    pygame.display.update()

    # Loads an image of "an X" symbol
    p1 = Player("X", load_image("player1.png"))
    # Loads an image of "an O" symbol
    p2 = Player("O", load_image("player2.png"))

    # TODO: remake this so the computer player can be "X" or "O"
    # initiate the computer player
    p3 = ComputerPlayer("X", load_image("player1.png"))

    # Currently, selecting computer in the menu will give a really bad computer 
    # player.
    if main_menu.mode == "computer":
        play_computer = True
    else:
        play_computer = False

    turn = 1
    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if turn % 2 != 0 and play_computer:
                board_copy = copy.deepcopy(board)
                make_computer_move(screen, board_copy, p2, p3, turn)
                place_computer_marker(screen, board, p3)
                result = check_ended(board, p3)

                if result == True:
                    answer = game_end(p3.marker)
                    if answer:
                        return True
                    else:
                        return False
                elif result == "draw":
                    answer = game_end("draw")
                    if answer:
                        return True
                    else:
                        return False
                turn += 1

            if pygame.mouse.get_pressed() == (1, 0, 0):
                if turn % 2 != 0 and not play_computer:
                    active_player = p1
                else:
                    active_player = p2

                active_player.pos = pygame.mouse.get_pos()

                if place_marker(screen, board, active_player):
                    turn += 1
                    pygame.display.update()  
                    result = check_ended(board, active_player)

                    if result == True:
                        answer = game_end(active_player.marker)
                        if answer:
                            return True
                        else:
                            return False
                    elif result == "draw":
                        answer = game_end("draw")
                        if answer:
                            return True
                        else:
                            return False

        pygame.display.update()


if __name__ == "__main__":
    import sys
    while True:
        main_menu = MainMenu()       
        finish = main(main_menu)
        if finish:
            pygame.quit()
            continue
        else:
            pygame.quit()
            sys.exit()
