import math
import random
from NCardGame import NCardGame  # Assuming NCardGame is a class

class Node:
    def __init__(self, number, cards, parent=None):
        self.cards = cards.copy()
        self.cards.remove(number)
        self.number = number
        self.parent = parent
        self.children = []
        self.visits = 0
        self.score = 0
    
    def return_next_move(self, depth=1):
        if depth == 0 or len(self.children) == 0:
            return 0, None
        for i in range(1, 10):
            n = Node(i, self.cards, self)
            self.children.append(n)
        return max((c.return_next_move(depth - 1) for c in self.children), key=lambda x: x[0])

def RollOut(cards):
    finalscore = 0
    random.shuffle(cards)
    for c in cards:
        game = NCardGame()
        score1, score2 = game.calculate_score_and_penalty(c, random.randint(1, 10))
        finalscore += score1
    return finalscore

def ucb(node):
    if node.visits == 0:
        return float('inf')
    return node.score / node.visits + math.sqrt(2 * math.log(node.parent.visits) / node.visits)

def select(node):
    while node.children:
        node = max(node.children, key=ucb)
    return node

def expand(node):
    child_number = random.choice(node.cards)
    child_node = Node(child_number, node.cards, parent=node)
    node.children.append(child_node)
    return child_node

def backpropagate(node, score):
    while node is not None:
        node.visits += 1
        node.score += score
        node = node.parent

def monte_carlo_tree_search(root, iterations):
    for _ in range(iterations):
        selected_node = select(root)
        if selected_node.cards:
            expanded_node = expand(selected_node)
            simulation_result = RollOut(expanded_node.cards)
            backpropagate(expanded_node, simulation_result)
    
    if root.children:
        best_child = max(root.children, key=lambda x: x.visits)
        return best_child.cards[0]  # Return a card from the best child
    else:
        return root.cards[random.randint(0, len(root.cards) - 1)]