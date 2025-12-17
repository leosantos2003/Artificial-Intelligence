# Artificial Intelligence

**UFRGS - INF01048 - Inteligência Artificial - 2025/2**

## About

This repository documents the four Artificial Intelligence projects proposed during the semester by the respective University discipline.

* [Project 1 - Supervised Learning](https://github.com/leosantos2003/Artificial-Intelligence/tree/main/trabalho_1_ia):
   * Part 1: Linear Regression. The first exercise consists of implementing the gradient descent algorithm for linear regression in Python 3. The goal is to predict farm prices using a fictitious dataset.
   * Part 2: TensorFlow/Keras. The second exercise focuses on evaluating neural networks for image classification using the TensorFlow/Keras library. The work is developed using a notebook.
  
* [Project 2 - Reinforcement Learning](https://github.com/leosantos2003/Artificial-Intelligence/tree/main/trabalho_2_ia):
   * The project consists of implementing and testing Value Iteration and Q-Learning algorithms. We use the Gridworld, Crawler (robot), and Pacman environments.
  
   * Task 1: Value Iteration. We implement the ValueIterationAgent agent in the `valueIterationAgents.py` file.
   * Task 2: Bridge Crossing Analysis. In the `analysis.py` file, we change just one of the parameters (discount or noise) so that the agent decides to cross the bridge in BridgeGrid.
   * Task 3: Q-Learning. We implement the main QLearningAgent methods in the `qlearningAgents.py` file.
   * Task 4: Epsilon Greedy. We implement the getAction method in `qlearningAgents.py`.
   * Task 5: Q-Learning and Pacman. We run Pacman with the previews implementations.
   * Task 6: Approximated Q-Learning. We implement ApproximateQAgent (also in `qlearningAgents.py`).

* [Project 3 - Graph Search (8-puzzle)](https://github.com/leosantos2003/Artificial-Intelligence/tree/main/trabalho_3_ia):
   * Consists of implementing a solver for the 8-puzzle game using the A* search algorithm to compare the efficiency of the Hamming and Manhattan distance heuristics.

* [Project 4 - Adversarial Search (Othello)](https://github.com/leosantos2003/Artificial-Intelligence/tree/main/trabalho_4_ia):
   * Consists of mplementing intelligent agents using adversarial search (Minimax with Alpha-Beta pruning) for the games Tic-Tac-Toe Misere and Othello, focusing on the development and competitive comparison of different heuristic evaluation functions.
 
   * Task 1: Generic Minimax. Implementation of the Minimax algorithm with Alpha-Beta pruning in the minimax_move function of the `minimax.py` file, independent of the specific game.
   * Task 2: Tic-Tac-Toe Misere. Implementation of the utility function and the depth-limit-free play logic in the `tttm_minimax.py` file.
   * Task 3: Othello - Counting Heuristic. Implementation of the heuristic based on piece difference and execution with limited depth in `othello_minimax_count.py`.
   * Task 4: Othello - Positional Heuristic: Implementation of the heuristic based on positional values ​​of the board (mask) in `othello_minimax_mask.py`.
   * Task 5: Othello - Custom Heuristic. Development of an original heuristic that surpasses the basic ones in `othello_minimax_custom.py`.
   * Task 6: Tournament Agent. Implementation of the best possible agent for competition (optimized Minimax or MCTS) in the `tournament_agent.py` file, respecting time and memory limits.

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

## Contact

Leonardo Santos - <leorsantos2003@gmail.com>
