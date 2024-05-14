# N-Card Game Rules

## Overview
N-Card Game is a two-player card game where each player is dealt a set of cards. Players take turns playing cards from their hands, and the game progresses until all cards have been played. At the end, scores are calculated based on certain rules, and the player with the highest score wins. To Play Now:
```
python3 main.py
```
Then Choose AI strategy (1: Normal Minimax, 2: Alpha-Beta-Pruning, 3: MCTS), Enter Input From Your Card Number! You Will See Summary At Last!
## Setup
1. The game begins with a deck of cards containing numbers from 1 to 10.
2. The deck is shuffled, and the cards are distributed equally between two players.
3. Each player receives an equal number of cards from the shuffled deck.

## Gameplay
1. Players take turns playing a single card from their hand.
2. The AI player and the human player alternate turns.
3. On each turn, the human player selects a card from their hand to play.
4. The AI player selects a card using a decision-making algorithm.
5. Once both players have played a card, the round ends, and scores are calculated.
6. The game continues until all cards have been played.

## Scoring Rules
1. **One Rule**: If one player plays a card with the value 1 and the other player does not, the player who played the card with 1 receives a score of 10, while the other player receives a score of 0. If both players play a card with the value 1, each player receives a score of 5.
2. **Three Rule**: If one player plays a card with the value 3 and the other player does not, the player who played the card with 3 receives a score of 5, while the other player receives a score of 0. If both players play a card with the value 3, each player receives a score of 2.
3. **Divisibility Rule**: If one player's card is divisible by the other player's card, the player with the larger card receives a penalty equal to the absolute difference between the two cards, while the player with the smaller card receives no penalty.
4. **Winner Gets Reward Loser Gets Penalty**: In all other cases, the player with the higher card value receives a score equal to the difference between the two card values, while the other player receives a score equal to the negative of that difference.

## Game End
1. The game ends when all cards have been played.
2. Final scores are calculated by summing the scores obtained in each round.
3. The player with the highest total score wins the game.

## Example Gameplay
1. The human player selects a card to play.
2. The AI player uses a decision-making algorithm to select a card.
3. Scores are calculated based on the rules mentioned above.
4. The process repeats until all cards have been played.
5. The player with the highest score at the end wins the game.

## Implementation Details
- The game is implemented in Python using classes and functions to represent the game logic.
- Decision-making algorithms such as Minimax with Alpha-Beta Pruning, Monte Carlo Tree Search are utilized for the AI player's moves.
- Function calls for various operations within the game are tracked for analysis and optimization purposes.


