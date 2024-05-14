import math
import random
class NCardGame:
    def __init__(self):
        self.function_calls_calculate = 0
        self.function_calls_minmax = 0
        self.function_calls_alpha_beta = 0
    def calculate_score_and_penalty(self, card1, card2):
        self.function_calls_calculate += 1
            
        # One Rule
        if card1 == 1:
            if card2 == 1:
                return 5, 5
            else:
                return 10, 0
        if card2 == 1:
            return 0, 10
        
        # Three Rule
        if card1 == 3:
            if card2 == 3:
                return 2, 2
            else:
                return 5, 0
        if card2 == 3:
            return 0, 5

        # Divisibility Rule, Lesser Will Get No Penalty
        if card1 % card2 ==0:
            if card1>card2:
                return card1-card2,0
            else:
                return 0,card2-card1
            
        # Winner Gets Reward, Loser Gets Penalty
        return card1 - card2, card2 - card1
    def minimax_with_alpha_beta_pruning(self, cards1, cards2, depth, alpha, beta, is_maximizing_player, played_cards1=None, played_cards2=None):
        self.function_calls_alpha_beta += 1
        if depth == 0 or len(cards1) == 0 or len(cards2) == 0:
            return 0, None

        if played_cards1 is None:
            played_cards1 = set()
        if played_cards2 is None:
            played_cards2 = set()

        if is_maximizing_player:
            best_score = -math.inf
            best_move = None
            for card1 in cards1:
                if card1 in played_cards1:
                    continue
                for card2 in cards2:
                    if card2 in played_cards2:
                        continue
                    score, _ = self.calculate_score_and_penalty(card1, card2)
                    next_cards1 = [c for c in cards1 if c != card1]
                    next_cards2 = [c for c in cards2 if c != card2]
                    next_played_cards1 = played_cards1.copy()
                    next_played_cards2 = played_cards2.copy()
                    next_played_cards1.add(card1)
                    next_played_cards2.add(card2)
                    next_score, _ = self.minimax_with_alpha_beta_pruning(next_cards1, next_cards2, depth - 1, alpha, beta, False, next_played_cards1, next_played_cards2)
                    if score + next_score > best_score:
                        best_move = (card1, card2)
                        best_score = score + next_score
                    alpha = max(alpha, best_score)
                    # if depth == 6:
                    #     print(f"======>LeafNode=>Player 1: {card1}, Player 2: {card2}, Score: {score}, Next Score: {next_score}")
                    #     print(f"Best Score: {best_score} Best Move: {best_move}")
                    if beta <= alpha:
                        break
                    
            return best_score, best_move
        else:
            best_score = math.inf
            best_move = None
            for card1 in cards1:
                if card1 in played_cards1:
                    continue
                for card2 in cards2:
                    if card2 in played_cards2:
                        continue
                    _, penalty = self.calculate_score_and_penalty(card1, card2)
                    next_cards1 = [c for c in cards1 if c != card1]
                    next_cards2 = [c for c in cards2 if c != card2]
                    next_played_cards1 = played_cards1.copy()
                    next_played_cards2 = played_cards2.copy()
                    next_played_cards1.add(card1)
                    next_played_cards2.add(card2)
                    next_score, _ = self.minimax_with_alpha_beta_pruning(next_cards1, next_cards2, depth - 1, alpha, beta, True, next_played_cards1, next_played_cards2)
                    if penalty + next_score < best_score:
                        best_move = (card1, card2)
                        best_score = penalty + next_score
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
                    # if depth == 6:
                    #     print(f"======>LeafNode=>Player 1: {card1}, Player 2: {card2}, Score: {penalty}, Next Score: {next_score}")
                    #     print(f"Best Score: {best_score} Best Move: {best_move}")
            return best_score, best_move
    def minimax_without_alpha_beta_pruning(self, cards1, cards2, depth, is_maximizing_player, played_cards1=None, played_cards2=None):
        self.function_calls_minmax += 1
        if depth == 0 or len(cards1) == 0 or len(cards2) == 0:
            return 0, None

        if played_cards1 is None:
            played_cards1 = set()
        if played_cards2 is None:
            played_cards2 = set()

        if is_maximizing_player:
            best_score = -math.inf
            best_move = None
            for card1 in cards1:
                if card1 in played_cards1:
                    continue
                for card2 in cards2:
                    if card2 in played_cards2:
                        continue
                    score, _ = self.calculate_score_and_penalty(card1, card2)
                    next_cards1 = [c for c in cards1 if c != card1]
                    next_cards2 = [c for c in cards2 if c != card2]
                    next_played_cards1 = played_cards1.copy()
                    next_played_cards2 = played_cards2.copy()
                    next_played_cards1.add(card1)
                    next_played_cards2.add(card2)
                    next_score, _ = self.minimax_without_alpha_beta_pruning(next_cards1, next_cards2, depth - 1, False, next_played_cards1, next_played_cards2)
                    if score + next_score > best_score:
                        best_move = (card1, card2)
                        best_score = score + next_score

            return best_score, best_move
        else:
            best_score = math.inf
            best_move = None
            for card1 in cards1:
                if card1 in played_cards1:
                    continue
                for card2 in cards2:
                    if card2 in played_cards2:
                        continue
                    _, penalty = self.calculate_score_and_penalty(card1, card2)
                    next_cards1 = [c for c in cards1 if c != card1]
                    next_cards2 = [c for c in cards2 if c != card2]
                    next_played_cards1 = played_cards1.copy()
                    next_played_cards2 = played_cards2.copy()
                    next_played_cards1.add(card1)
                    next_played_cards2.add(card2)
                    next_score, _ = self.minimax_without_alpha_beta_pruning(next_cards1, next_cards2, depth - 1, True, next_played_cards1, next_played_cards2)
                    if penalty + next_score < best_score:
                        best_move = (card1, card2)
                        best_score = penalty + next_score

            return best_score, best_move



