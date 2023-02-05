# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 00:37:57 2022

@author: justin
"""
from board_evaluation import evaluation
from store_boards import *
import copy

class TreeNode:
    def __init__(self, board, parent = None, depth = 0, children = []):
        '''
        board - list representing tic tac toe board
        parent - TreeNode object representing parent node
        depth - attribute representing the depth of the tree (increasing as you go down). COuld also be used to represent turn
        children - list containing TreeNode objects of all the potential resulting nodes from one move on the current node
        maxTurn - is it the maximizing players turn?
        value - float representing the value assosciated with the current board state
        trail - indicates the best move
        '''
        self.board = board
        self.parent = parent
        self.value = None
        self.depth = depth
        self.children = children
        self.maxTurn = (depth%2 == 0)
    
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
        if self.get_depth() == 0:
            self.value = 0
        else:
            self.value = int(evaluation(self.get_board())/self.get_depth())
        
    def get_board_val(self):
        return self.value
    
    def input_board_position(self, player_ismin):
        '''
        Allows user interactivity with the tic tac toe board
        User specifies which position they would like to chose
        Return the corresponding child TreeNode object
        '''
        if player_ismin:
            team = 'O'
        else:
            team = 'X'
        while True:
            print('-----please specify your next move-----')
            column = int(input('Column (1-3): '))
            row = int(input('Row (1-3): '))
            print('-----Thank you-----')
            played_board = self.get_board()[:]
            if played_board[row-1][column-1] != '-':
                print('Sorry, the slot you selected is either occupied or does not exist. Try again')
                continue
            break
        played_board[row-1][column-1] = team
        for child in self.get_children():
            if child.get_board() == played_board:
                return child
        else:
            return None

    def select_team(self):
        while True:
            player_team = input('Please input which team you would like to play for ("X" or "O"): ')
            if player_team.upper() == 'X' or player_team.upper() == 'O':
                break
            print('Please try again and input a valid team ("X" or "O")')
        return player_team

    def display_status(self):
        '''
        Displays general information for TreeNode object in a human readable way.
        Primarily used for debugging
        '''
        print('-----Status of Current Node-----')
        if self.get_parent() != None:
            print('parent is', self.get_parent().display_board())
        else:
            print('We are actively in the root node')
        self.display_board()
        print('There are', len(self.get_children()), 'children')
        print('The board value is', self.get_board_val())
        print('-----End of Status Report-----')
    
    def generate_boards(self, all = False):
        '''
        Used to generate all potential offspring corresponding nodes from passed in TreeNode object
        Updates the children attribute of the TreeNode object with all the potential board options
        Recursively repeats the steps for the TreeNode's children until terminal state or draw reached
        '''
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
                    child.set_board_val()
                    self.set_children([child])
                    
        if all:
            for child in self.get_children():
                child.generate_boards(True)

    def minimax(self):
        '''
        Applies the minimax algorithm to recursively search for optimal child nodes
        '''
        # self.set_board_val()
        # self.generate_boards()
        if self.get_board_val() not in [None, 0] or len(self.get_children()) == 0:
            return self, self.get_board_val()
        
        if self.maxTurn:
            max_board_val = None, -1000
            for child in self.get_children():
                tboard_eval = child.minimax()[1]
                if tboard_eval == max(tboard_eval, max_board_val[1]):
                    max_board_val = child, tboard_eval  
            # self.value = max_board_val[1]
            return max_board_val
        
        else:
            min_board_val = None, 1000
            for child in self.get_children():
                tboard_eval = child.minimax()[1]
                if tboard_eval == min(tboard_eval, min_board_val[1]):
                    min_board_val = child, tboard_eval
            # self.value = min_board_val[1]
            return min_board_val  

    def play_game(self, aiismax):
        '''
        Allows the user and the AI to play a game of tic tac toe
        If the ai is the maximizing player and it is the maximizing player's turn to move then, 
        The AI uses the make_move and minimax function to chose the ideal child node
        After the turn switches and the user specifies his best move, if the users move was not 
            already predicted by the minimax algorithm then we need to recalculate the ideal route
        '''
        # self.generate_boards(True)
        while (self.get_board_val() == 0 or self.get_board_val() == None) and len(self.get_children()) != 0:
            self.display_board()
            if (aiismax == self.is_max_turn()):
                ai_move = self.minimax()[0]
                ai_move.play_game(aiismax)
            else:
                player_move = self.input_board_position(aiismax)
                player_move.play_game(aiismax)
        print('-----Game Over-----')
        self.display_board()
        if self.get_board_val() > 0:
            print('X Team Won!!')
        elif self.get_board_val() < 0:
            print('O Team Won!!')
        else:
            print('Close But Tie Game')
        quit()

 
if __name__ == "__main__":                                  
    board = [['-', '-', '-'], 
             ['-', '-', '-'], 
             ['-', '-', '-']]
#     root = TreeNode(board, depth = 0)
#     root.generate_boards()
    root = call_root_board()
    player_team = root.select_team()
    root.play_game((player_team.upper() == "O"))

        
        
            
        
