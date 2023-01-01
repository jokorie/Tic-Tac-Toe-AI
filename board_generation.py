# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 00:37:57 2022

@author: justin
"""
from board_evaluation import evaluation

import copy

class TreeNode:
    def __init__(self, board, parent = None, depth = 0, children = []):
        self.board = board
        self.parent = parent
        self.value = None
        self.depth = depth
        self.children = children
        self.maxTurn = (depth%2 == 0)
        self.trail = False
    
    def get_board(self):
        return copy.deepcopy(self.board)
        
    def set_board(self, board):
        self.board = board
        
    def display_board(self):
        '''displays board in tic tac toe format
        '''
        print('-----Printing Board-----')
        print(self.get_board()[0])
        print(self.get_board()[1])
        print(self.get_board()[2])
        print('-----Board Printed-----')
    
    def get_children(self):
        return copy.copy(self.children)
    
    def get_parent(self):
        return copy.copy(self.parent)
    
    def set_children(self, childlist):
        if len(self.get_children()) == 0:
            self.children = childlist[:]
        else:
            self.children += childlist
            
    def get_descendants(self):
        '''
        Returns the total number of valid board combinations or potential offspring nodes from current board state
        '''
        desc = len(self.get_children())
        for child in self.get_children():
            desc += child.get_descendants()
        return desc
    
    def get_depth(self):
        return self.depth
    
    def is_max_turn(self):
        '''
        Returns True if maximizer player's turn
                False if minimizer player's turn
        '''
        return self.maxTurn
    
    def set_board_val(self):
        '''
        Returns the value of the current board state. Incentivizes arriving at favorable terminal board states quicker
        '''
        self.value = evaluation(self.get_board())/self.get_depth()
        
        
    def get_board_val(self):
        return self.value
    
    def get_trail(self):
        return self.trail
    
    def set_trail_true(self):
        self.trail = True
        
    def set_trail_false(self, siblings = False):
        '''
        Sets the trail of the current node = to False. 
        If siblings = True, then it sets the trails of all of its siblings to false as well
        '''
        if siblings == True:
            for child in self.get_parent().get_children():
                child.set_trail_false()
        else:
            self.trail = False
    
    def reset_trail(self):
        '''
        Sets the trails of the active node and all its resulting combinations to False
        '''
        self.trail = False
        for child in self.get_children():
            child.reset_trail()
    
    def display_status(self):
        print('-----Status of Current Node-----')
        print('parent is', self.get_parent().display_board())
        self.display_board()
        print('There are', len(self.get_children()), 'children')
        print('The trail of the active node is set to', self.get_trail())
        print('The board value is', self.get_board_val())
        print('-----End of Status Report-----')
    
    def generate_boards(self):
        # print('Board for Tree depth =', self.get_depth())
        # self.display_board()
        self.set_board_val()
        for i in range(len(self.get_board())):
            for j in range(len(self.get_board())):
                if (self.get_board()[i][j] == None or self.get_board()[i][j] == '-') and self.get_board_val() == 0:                    
                    if self.is_max_turn():
                        child_board = self.get_board()
                        child_board[i][j] = 'X'
                    else:
                        child_board = self.get_board()
                        child_board[i][j] = 'O'
                    child = TreeNode(child_board, self, self.get_depth() + 1)
                    self.set_children([child])
                    child_board = self.get_board()
                    
        for child in self.get_children():
            child.generate_boards()
    

    def minimax(self):
        self.set_board_val()
        if self.get_board_val() != 0 or len(self.get_children()) == 0:
            return self.get_board_val()
        
        if self.is_max_turn():
            max_board_val = -1000
            for child in self.get_children():
                tboard_eval = child.minimax()
                if tboard_eval > max_board_val:
                    child.set_trail_false(siblings = True)
                    child.set_trail_true()
                    max_board_val = tboard_eval   
                else:
                    child.reset_trail()
            # if self.get_depth() == 6:
            #     print('The max estimated score is', max_board_val)
            return max_board_val
        
        else:
            min_board_val = 1000
            for child in self.get_children():
                tboard_eval = child.minimax()
                if tboard_eval < min_board_val:
                    child.set_trail_false(siblings = True)
                    child.set_trail_true()
                    min_board_val = tboard_eval
                else:
                    child.reset_trail()
            return min_board_val   
        
    def make_move(self, full = False):
        self.display_board()
        for child in self.get_children():
            if child.get_trail() == True:
                child.display_board()
                if full:
                    for grandchild in child.get_children():
                        if grandchild.get_trail() == True:
                            grandchild.make_move(True)

 
                                  
board = [['X', 'O', '-'], 
         ['-', 'X', '-'], 
         ['-', '-', 'O']]
root = TreeNode(board, depth = 4)

root.generate_boards()
root.minimax()
root.make_move(True)

# for child in root.get_children():
#     if child.get_trail() == True:
#         child.display_board()
#         for grandchild in child.get_children():
#             count = 0
#             if grandchild.get_trail() == True:
#                 count += 1
#                 grandchild.display_board()
#                 print()
#         print(count)

# counter = 0
# for row in board:
#     counter += row.count('X') + row.count('O')

# print(root.board)
# print(len(root.get_board()))
# print()
# for child in root.get_children():
#     print('Here are the trails of the children:', child.get_trail())
# print(root.board is root.get_board())
# print(len(root.children))
# oboard = root.get_board()
# board[0][1] = 'Y'
# root.set_board(board)
# nboard = root.get_board()
# print(oboard == nboard)
# print(root.get_descendants())


        
        
            
        
