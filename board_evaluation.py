# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 00:14:22 2022

@author: justi
"""

#board evaluation
'''
board = [['-', '-', '-'], 
         ['-', '-', '-'], 
         ['-', '-', '-']]
'''

def evaluation(board):
    """
    input: board list(list)
    return: value int
    """
    #checking rows for terminal state
    for row in board:
        if len(set(row)) == 1 and row[0] != '-':
            if row[0] == 'X':
                return 100
            return -100
    
    #checking columns for terminal state  
    for i in range(len(board)):
        if board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] != '-':
            if board[0][i] == 'X':
                return 100
            return -100
    
    #checking diagonals
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != '-':
        if board[0][0] == 'X':
            return 100
        return -100 
    
    if board[2][0] == board[1][1] and board[2][0] == board[0][2] and board[2][0] != '-':
        if board[2][0] == 'X':
            return 100
        return -100 
    
    #returns 0 if board not in a terminal state
    return 0
        
            
            