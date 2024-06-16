import random
import math
from display import display_game_info, display_cards, display_result
from NCardGame import NCardGame
from NCardGameMCTS import Node, monte_carlo_tree_search
import time
import resource
def initialize_cards(Number_of_Cards=10):
    cards = []
    n = 0
    while n < Number_of_Cards:
        cards.append(random.randint(1, 10))
        n += 1
    return cards
def get_player_input(player_cards, player_name):
    selected_card = int(input(f'{player_name}, enter your card: '))
    while selected_card not in player_cards:
        print(f'Invalid card. Please enter a valid card from your cards: {player_cards}')
        selected_card = int(input(f'{player_name}, enter your card: '))
    return selected_card
def choose_ai_strategy():
    strategy = input("Choose AI strategy (1: Normal Minimax, 2: Alpha-Beta-Pruning, 3: MCTS): ")
    while strategy not in ['1', '2', '3']:
        print("Invalid choice! Please choose again.")
        strategy = input("Choose AI strategy (1: Normal Minimax, 2: Alpha-Beta-Pruning, 3: MCTS): ")
    return strategy
def play_game(depth, player1_cards, player2_cards, ai_strategy):
    global AI_TIME
    AI_TIME = 0
    game_number = 1
    HumanScore = 0
    AIScore = 0
    root = Node(player1_cards[0], cards=player1_cards)

    for i in range(depth):
        print('\n' * 5)
        display_game_info(game_number, depth)
        display_cards(player2_cards, "Human")
        humanplayed = get_player_input(player2_cards, "Human")

        display_cards(player1_cards, "AI")
        ai_played = -1  
        start_time = time.time()
        if ai_strategy == '1':
            _, ai_played = card_game.minimax_without_alpha_beta_pruning(player1_cards, list(range(1, depth + 1)), depth, True)
        elif ai_strategy == '2':
            _, ai_played = card_game.minimax_with_alpha_beta_pruning(player1_cards, list(range(1, depth + 1)), depth, -math.inf, math.inf, True)
        elif ai_strategy == '3':
            count =0
            while ai_played not in player1_cards:
                if count>10:
                    break
                best_child = monte_carlo_tree_search(root, 1000)
                try:
                    ai_played = best_child.number
                except Exception as e:
                    ai_played = best_child
                    ai_played = (ai_played, 0)
                count+=1
            ai_played = (player1_cards[random.randint(0, len(player1_cards)-1)], 0)
        aitime = time.time() - start_time
        AI_TIME +=aitime
        print(f'AI Thinking Time: {aitime}')
        print(f'AI Played: {ai_played}')
        player2_cards.remove(humanplayed)
        player1_cards.remove(ai_played[0])  # Fixing the bug

        ai_score, human_score = card_game.calculate_score_and_penalty(ai_played[0], humanplayed)
        AIScore += ai_score
        HumanScore += human_score
        display_result(AIScore, HumanScore)
        game_number += 1

    display_result(AIScore, HumanScore)

    if AIScore > HumanScore:
        print('AI Wins!')
    elif HumanScore > AIScore:
        print('Human Wins!')
    else:
        print('Game Drawn')


if __name__ == "__main__":
   
    start_time = time.time()
    AI_TIME = 0
    cards = initialize_cards(20)
    random.shuffle(cards)
    depth = int((len(cards) + 1) / 2)
    player1_cards = cards[:len(cards) // 2]
    player2_cards = cards[len(cards) // 2:]
    card_game = NCardGame()
    ai_strategy = choose_ai_strategy()
    
    play_game(depth, player1_cards, player2_cards, ai_strategy)

    end_time = time.time()
    elapsed_time = end_time - start_time
    max_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024  # in kilobytes
    
    print('Summary')
    if ai_strategy == '1':
        print("Function Calls Minimax:", card_game.function_calls_minmax)
    elif ai_strategy == '2':
        print("Function Calls Minimax with Alpha-Beta Pruning:", card_game.function_calls_alpha_beta)
    elif ai_strategy == '3':
        print("Summary of MCTS")
    print("Elapsed time:(Full)", elapsed_time, "seconds")
    print("Elapsed time:(AI Thinking)", AI_TIME, "seconds")
    print("Maximum memory usage:", max_memory, "KB")
    
    