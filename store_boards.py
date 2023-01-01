from board_evaluation import *
from board_generation import *
import pickle

board = [['-', '-', '-'], 
         ['-', '-', '-'], 
         ['-', '-', '-']]

root = TreeNode(board, depth = 0)

root.generate_boards()

with open('board.combinations', 'wb') as board_combinations_file:
  pickle.dump(root, board_combinations_file)

# with open('board.combinations', 'rb') as board_combinations_file:
#   root = pickle.load(board_combinations_file)
#   # root.display_board()
#   root.display_status()
#   for child in root.get_children():
#     child.display_board()