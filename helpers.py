

import random
import math

mines = []

def reset():
    print("Reset")



def check_borders(row, column):
    global mines
    bordered_mines = 0
    
    
    
    return bordered_mines


def check_mines(row, column):
    global mines
    
    index = row*10+column
    
    print(index)
    if mines.__contains__(index):
        return True
    
    return check_borders(row, column)
    
    
    
    
def set_mines(mine_count):
    global mines
    size = 100
    for i in range(mine_count):
        number = math.floor(size*random.random())  #create a random number 
        if mines.__contains__(number) :             #check if number already created
            i -=1                                   #if yes decrease i to generate a new random number
        else : mines.append(number)                 #else add number to minelist
        
    mines.sort()
    
        
    print(mines)
