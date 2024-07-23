from random import choices
from random import choice

class AI:
    updatePath = {'P1': True, 'P2': True}
    paths = {'P1': [], 'P2': []}
    goal = {'P1': (0,2), 'P2': (4,2)}
    enemy = {'P1': 'P2', 'P2': 'P1'}

    def get_move(self, player, game):
        print("\nPLAYER: ", player)
        if (self.updatePath[player]):
            self.paths[player] = game.extract_path(game.player_positions[player], self.goal[player])
            self.updatePath[player] = False
            
        action = choices(['move', 'wall'], weights=[70, 30], k=1)[0]
        if action == 'move':
            return self.move(player, game)
            
        elif action == 'wall':
            self.updatePath['P1'] = True
            self.updatePath['P2'] = True
            return self.place_wall(player, game, game.player_positions[self.enemy[player]])
    
    def move(self, player, game):
        move = self.paths[player].pop(0)
        return move
    
    
    def place_wall(self, player, game, enemy_position):
        legal_moves = game.get_legal_moves()
        
        wall_moves = [move for move in legal_moves if move[0] in ('H', 'V')]
        
        wall_moves.sort(key=lambda move: (abs(move[1] - enemy_position[0]) + abs(move[2] - enemy_position[1]), move[0] == 'V'))
        
        for move in wall_moves:
            if move[0] == 'H':
                return move
        return wall_moves[0] if wall_moves else self.move(player, game)
