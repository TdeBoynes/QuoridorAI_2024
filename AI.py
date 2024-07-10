# File: ai.py

from random import choice

class AI:
    def get_move(self, game):
        action = choice(['move', 'wall'])
        return self.move(game)
        # if action == 'move':
        # elif action == 'wall':
        #     return self.place_wall(game)
    
    def move(self, game):
        legal_moves = game.get_legal_moves()
        print("YYYEEEE\n\n", legal_moves)
        return choice(legal_moves)
        # if legal_moves:
        # else:
        #     return None  # No legal moves available
    
    def place_wall(self, game):
        # Implement logic to place a wall
        pass
