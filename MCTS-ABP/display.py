def display_cards(cards, player_name):
    print(f"+{'-' * 28}+")
    print(f"| {player_name}'s Cards: {' ' * (21 - len(player_name))} |")
    print(f"+{'-' * 28}+")
    for card in cards:
        print(f"| {card:^26} |")
    print(f"+{'-' * 28}+")
def display_game_info(game_number, depth):
    print(f"+{'-' * 28}+")
    print(f"| {'NCard Game':^26} |")
    print(f"| {'Depth: ' + str(depth):^26} |")
    print(f"| {'Game Number: ' + str(game_number):^26} |")
    print(f"+{'-' * 28}+")
def display_result(AIScore, HumanScore):
    print(f"+{'-' * 28}+")
    print(f"| {'Final Scores':^26} |")
    print(f"| {'AI: ' + str(AIScore):^12} {'Human: ' + str(HumanScore):^12} |")
    print(f"+{'-' * 28}+")