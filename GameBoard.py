# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 21:33:43 2021

@author: norbe
"""

import math
import os
import time

class GameBoard:
    def __init__(self, maxX, maxY, refreshrate=15):
        self.__maxX = maxX
        self.__maxY = maxY
        
        #refreshrate = refresh screen x times per second
        self.__refreshrate = refreshrate
        #refreshwait = refresh screen every x seconds
        self.__refreshwait = math.ceil(1/refreshrate)
        
        #board[y][x] for y down, x right of top left position
        self.board = [['#' for i in range(maxX)] for i in range(maxY)]
        
        self.prntBoard = True
        
        if os.name == 'nt':
            #for windows
            self.__clearScreen = lambda: os.system('cls')
        else:
            #for other os
            self.__clearScreen = lambda: os.system('clear')
        
    #print board once
    def boardString(self):
        boardStr = ''
        for row in self.board:
            for col in row:
                boardStr += col
            boardStr +=  '\n'
        return(boardStr)
    
    def printBoard(self):
        print(self.boardString())
     
    #intended to run on it's own function
    def printBoardCont(self):
        self.prntBoard = True
        while self.prntBoard:
            self.__clearScreen()
            self.printBoard()
            time.sleep(self.__refreshwait)
            
    #stop while loop that prints board
    def stopPrinting(self):
        self.prntBoard = False
        
    #takes a dict of { (x, y): 'c' } and modifies characer at pos x,y to 'c' 
    #assumes value is always 1 character (string of len 1)
    def modifyBoard(self, changesDict):
        for key, value in changesDict.items():
            x, y = key
            if x < 0 or x > self.__maxX or y < 0 or y > self.__maxY:
                raise ValueError(f"x or y value out of range.\ngiven x:{x}, y:{y}.\nvalues must in range 0 to maxX {self.__maxX} or maxY {self.__maxY}")
            self.board[y][x] = value

#for testing
if __name__ == '__main__':
    b = GameBoard(50, 47, 60)
    print(b.boardString())
    b.printBoardCont()
    # b.modifyBoard({(5,3):'O'})
    # print(b.boardString())
    # print('after clear')