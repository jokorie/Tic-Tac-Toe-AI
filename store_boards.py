from board_evaluation import *
from board_generation import *
import pickle

def store_root_board():
  '''
  Stores the root tree node which holds all possible board developments in file called board.combinations
  '''
  board = [['-', '-', '-'], 
           ['-', '-', '-'], 
           ['-', '-', '-']]

  root = TreeNode(board, depth = 0)

  root.generate_all_boards(True)

  with open('board.combinations', 'wb') as board_combinations_file:
    pickle.dump(root, board_combinations_file)

def call_root_board():
  '''
  Access the root tree node from board.combinations and returns the variable
  '''
  with open('board.combinations', 'rb') as board_combinations_file:
    root = pickle.load(board_combinations_file)
    return root

if __name__ == '__main__':
  store_root_board()
  root = call_root_board()
  root.display_board()

