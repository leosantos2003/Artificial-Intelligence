# T4 \- Artificial Intelligence: Adversarial Search

* **Agent:** `o_cara`

# 1\. Group Identification  
* Bernardo Fellini Oliveira \- 00323402 \- Turma B  
* Vinícius Gross Castro \- 00324541 \- Turma B  
* Leonardo Rocha dos Santos	\- 00341831 \- Turma B

# 2\. Additional Libraries

This work uses only standard Python 3 libraries (specifically `math` for `inf` in the minimax algorithm).

No additional libraries are required for execution.

# 3\. Evaluation of Alpha-Beta Pruning (Tic-Tac-Toe Misere)

As requested in item "a" of section 2.2 of the statement, an evaluation was carried out of the performance of the agent that we chose to name `o_cara` in the Reverse Tic-Tac-Toe game.

The implemented algorithm was Minimax with alpha-beta pruning and unlimited depth (`max_depth = -1`).

The results of the manual tests were:

* **Does minimax always win or draw when playing against the \`randomplayer\`?**

* **Yes.** In tests performed against the `randomplayer`, the agent `o_cara` (playing with the optimal strategy) never lost. The result was a draw, proving that the agent plays in a way that avoids errors.

* **Does minimax always break even?**  
* **Yes.** When executing `o_cara` (Blacks) against `o_cara` (Whites), the result of the game was a draw. This indicates that both players are playing the optimal strategy, and the game ends with the board full without either player being forced to lose.

* **Does minimax not lose to you when you use your best strategy?**  
* **Yes.** The agent never lost to a human player. In the tests, there were two results:  
        1.  The human player made a mistake (aligning three pieces) and **lost** (the agent `o_cara` won).  
        2.  The human player played with the best strategy and the game ended in a **draw**.

\---

# 4\. Assessment and Implementation (Othello)

As requested in item "b" of section 2.2 of the statement, a tournament was held between the 3 Minimax algorithms with different heuristics being used by the agent `o_cara`. Each algorithm faced each other twice, once playing first and once playing last.

Each Minimax algorithm was run with alpha-beta pruning and a fixed depth limited to 5 levels (the greatest depth that did not exceed the stipulated limit of 5 seconds per play).

Our custom heuristic was a combination of the positional value and piece counting heuristics, plus two more heuristics:

* **Immediate Mobility Heuristic:** It considers states where the player has more legal moves than their opponent as better. The greater the difference in legal moves between the player and the opponent, the better the state.  
* **Potential Mobility Heuristic:** It considers states where the opponent's pieces are surrounded by blank spaces as better, as these represent states where the player will likely have more opportunities to attack in the future.

This custom heuristic was based on these two websites:  
[**http://home.datacomm.ch/t\_wolf/tw/misc/reversi/html/index.html**](http://home.datacomm.ch/t_wolf/tw/misc/reversi/html/index.html)  
[**https://www.cs.cornell.edu/\~yuli/othello/othello.html**](https://www.cs.cornell.edu/~yuli/othello/othello.html)  
They each describe, at a high level, an implementation of an Othello bot using Minimax search with alpha-beta pruning and heuristics, and state that the mobility of pieces in Othello is one of the best heuristics to follow.  
Our main difference in heuristic considerations was maintaining the piece counting heuristic with the same relative weight compared to the other heuristics, as we saw in the tournament that this resulted in the best outcome for our customized heuristic.

The results of the tournament between algorithms with different heuristics were:

* Piece count X Place value:
  Score: **22 x 42**  
  Victory: **Place value**  
* Positional value X Piece count:  
  Score: **22 x 42**  
  Victory: **Piece count**  
* Piece count X Custom heuristic:  
  Score: **19 x 45**  
  Victory: **Custom heuristic**  
* Custom heuristic X Piece count:  
  Score: **41 x 23**  
  Victory: **Custom heuristic**  
* Place value X Custom heuristic:  
  Score: **20 x 44**  
  Victory: **Custom heuristic**  
* Custom heuristic X Place value:  
  Score: **37 x 27**  
  Victory: **Custom heuristic**


**Final results:** 

1. Custom heuristic: **4 victories**  
2. Place value e Piece count: **1 Victory each (**the captured pieces are the same for both heuristics.**)**

Based on the results, it's clear that our customized heuristic was the most successful, winning all its matches. From the results, we can assume that the player who plays last has an advantage in the game.
