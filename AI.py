# File: ai.py

from random import choices
from random import choice

class AI:
    updatePath = True
    goal = {'P1': (0,2), 'P2': (4,2)}
    paths = {'P1': [], 'P2': []}

    def get_move(self, player, game):
        if (self.updatePath):
            self.paths[player] = game.extract_path(game.player_positions[player], self.goal[player])
            self.updatePath = False
            

        action = choices(['move', 'wall'], weights=[70, 30], k=1)[0]
        print("\nPLAYER: ", player)    
        if action == 'move':
            return self.move(player, game)
            
        elif action == 'wall':
            self.updatePath = True
            return self.place_wall(game)
    
    def move(self, player, game):
        move = self.paths[player].pop(0)
        return move
        # legal_moves = game.get_legal_moves()
        # return choice(legal_moves)
        # if legal_moves:
        # else:
        #     return None  # No legal moves available
    
    def place_wall(self, game):
        legal_moves = game.get_legal_moves()
        return choice(legal_moves)
        # Implement logic to place a wall
        pass
