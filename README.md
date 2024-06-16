# HandsOnAI

Welcome to the HandsOnAI repository! This repository contains a series of tutorials and projects that provide hands-on experience with various artificial intelligence (AI) techniques and algorithms. Each tutorial is designed to help you understand and implement core AI concepts through practical examples and exercises.

## Contents

### Tutorial 1: Searching
This tutorial covers fundamental search algorithms that are essential for problem-solving in AI. The implemented algorithms include:

- **Breadth-First Search (BFS)**: An algorithm for traversing or searching tree or graph data structures. It starts at the root node and explores all neighboring nodes at the present depth level before moving on to nodes at the next depth level.
- **Depth-First Search (DFS)**: An algorithm for traversing or searching tree or graph data structures. It starts at the root node and explores as far as possible along each branch before backtracking.
- **A* Search**: A heuristic search algorithm that finds the shortest path from a start node to a goal node in a weighted graph. It combines the benefits of Dijkstra’s algorithm and Greedy Best-First-Search.

### Tutorial 2: Monte Carlo Tree Search & Alpha-Beta Pruning
This tutorial introduces advanced search algorithms used in decision-making processes, particularly in game playing AI:

- **Monte Carlo Tree Search (MCTS)**: A heuristic search algorithm for decision processes, most notably employed in game play. It involves building a search tree based on random sampling of the search space.
- **Alpha-Beta Pruning**: An optimization technique for the minimax algorithm that reduces the number of nodes evaluated in the search tree. It is used to decrease the computation time in decision-making processes by pruning branches that cannot influence the final decision.

### Tutorial 3: Reinforcement Learning
This tutorial delves into reinforcement learning, a type of machine learning where an agent learns to make decisions by taking actions in an environment to maximize cumulative rewards. Key topics include:

#### Step 1: Introduction to OpenAI Gym or similar
**Task**: Students should install OpenAI Gym and familiarize themselves with its basic functionality.  
**Deliverable**: Write a brief report or code comments on how OpenAI Gym environments work, focusing on the methods like `reset()` and `step()`.

#### Step 2: Exploring Markov Decision Processes (MDP)
**Environment Suggestion**: FrozenLake-v1  
**Task**: Students should analyze the chosen environment as an MDP. Identify states, actions, rewards, and transitions.  
**Deliverable**: Provide a detailed description of the FrozenLake-v1 as an MDP in the report.

#### Step 3: Implementing Value Iteration
**Task**: Students implement the Value Iteration algorithm to solve the FrozenLake-v1 environment.  
**Deliverable**: 
- Python code for the Value Iteration algorithm.
- A plot showing the convergence of the state value function.
- A discussion on how the policy derived from Value Iteration performs in the environment.

#### Step 4: Implementing Q-Learning
**Task**: Implement the Q-learning algorithm and test it in the same FrozenLake-v1 environment.  
**Deliverable**:
- Python code for the Q-learning algorithm.
- Plots showing the learning curve (rewards over episodes).
- An evaluation comparing the performance of the learned policy against the policy from Value Iteration.

### Tutorial 4: Neural Networks
This tutorial provides a comprehensive introduction to neural networks, covering fundamental concepts and practical implementation. Topics include:

- **Perceptrons**: The simplest type of artificial neural network, which consists of a single layer of weights connected to input features.
- **Multi-layer Perceptrons (MLPs)**: A class of feedforward artificial neural networks with multiple layers of nodes, each layer fully connected to the next one.
- **Backpropagation**: A supervised learning algorithm used for training neural networks, involving the propagation of the error backward through the network to update the weights.

## Usage
Each tutorial is contained in its respective Jupyter Notebook file. To start a tutorial, simply open the corresponding `.ipynb` file in Jupyter Notebook and follow the instructions within. The notebooks include explanations, code examples, and exercises to reinforce your understanding of the concepts.

## Contributing
Contributions are welcome! If you have any improvements or new tutorials to add, please fork the repository and create a pull request. When contributing, please ensure your work adheres to the existing style and structure of the repository.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.