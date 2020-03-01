from player import Player


class ComputerPlayer(Player):

    def __init__(self, marker, marker_image):
        Player.__init__(self, marker, marker_image)
        self.move = None
