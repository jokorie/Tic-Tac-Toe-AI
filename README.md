# Tic-Tac-Toe-AI
Uses a minimax algorithm to optimize decision making for tic-tac-toe. Game is played in the terminal.

# Motivation
- Over the winter of 2022 my goal was to learn how to play chess and code a competent chess AI. After surfacing over the minimax algorithm, I thought that I might apply this algorithm on simpler games (tic-tac-toe, checkers) before I advance to a more complex game like chess.
- Link to Checkers Repository: https://github.com/jokorie/Checkers-Minimax-AI

# Overview
- Minimax is a famous decision making algorithm which works with two-player turn-based perfect information games. In a proper implementation, every possible game state is represented as a node in a Tree Data Structure, whereas the root node is the starting game state where all other possible game states are fundamentally derived from. 
- A player's turn is represented as the player being in the node which corresponds to the active game state (prior to making a move). We represent all possible moves that a player can make as the offspring child nodes of the active node. In a typical game of minimax, as you traverse the depth of the tree by one level, the turns alternate, ie... after player 1 makes a move it is now player 2's turn.

# Evaluation
- One requisite to the minimiax algorithm is an evaluation function, which can evaluate the current state of the board as favoring either P1 (player 1) or P2 (player 2). Because Tic-Tac-Toe is a simpler & shorter game than other games like chess or checkers, I only assigned terminal board states a non-zero value.
- We will attribute a large possitive number as being an advantageous positioning for P1 and a large negative number as being a favorable positioning for P2. For this reason, we refer to P1 as being the maximizing player as it is attempting to chose a positioning which maximizies the score of its node. Likewise, we will refer to player 2 as being the minimizing player for similar reasons.
- I increased the magnitudes of the board evaluations for terminal states which can be achieved quicker, so that for example a win for P1 on turn 2 might be worth -100 pts whereas the same win but on turn 6 would be a smaller negative number like -60 pts. This makes the AI prioritize wins which can be achieved quicker.

# Minimax
- The minimax algorithm recursively traverses all nodes down a specified depth (or till it reaches a terminal game state) searching for the optimal path assuming the minimizing player, P2 acts rationally. The minimax evaluates these terminal/max depths states and assigns a value to the states using the evaluation function. 
- The parent nodes will consider the values of all its direct children and the optimal value which aligns with the player's status as either the minimizing or maximizing player will be passed up . For example, if it is the maximizing players turn and it has to chose between a child node with the score of -1, 0, or +1, the maximizing player will always chose the node leading to the +1 score in order to maximize its score. 
- In a deeper, more complex game tree, as the parent node is passed up a value from its child nodes, in turn the parent node becomes the child node for its parent node as it passes up a value. Keep in mind that as the you traverse the tree vertically, the turns switch from minimizing player to maximizing player, or vice versa, which affects which node value gets passed up to the parent. See image below of a simplified tic tac toe minimax diagram.

![eo3qr44bp1w96a92t8s2](https://user-images.githubusercontent.com/121595907/216156892-1b97cda1-b64d-40b9-9160-c5e9cd0a5fb2.png)

