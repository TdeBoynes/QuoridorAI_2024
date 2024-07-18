import random
from AI import AI

class Player2AI:
    def __init__(self):
        self.ai = AI()

    def get_move(self, game):
        move = self.ai.get_move('P2', game)
        return move
