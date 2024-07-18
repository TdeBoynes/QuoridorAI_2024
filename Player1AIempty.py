import random
from AI import AI

class Player1AI:
    def __init__(self):
        self.ai = AI()

    def get_move(self, game):
        move = self.ai.get_move('P1', game)
        return move
