
import tkinter as tk
import random
import math

mines = []

def reset():
    print("Reset")



def check_borders(row, column):
    global mines
    bordered_mines = 0
    
    for i in [-1, 0 , 1]:
        for j in [-1, 0, 1]:
            index = (row+i)*10+(column+j)
            if mines.__contains__(index):
                #print(index)
                bordered_mines += 1
    
    
    return bordered_mines


def check_mines(row, column, button):
    global mines
    
    
    index = row*10+column
    
    print(index)
    if mines.__contains__(index):
        try:
            button[row][column].config(text="X")
        except AttributeError:
            print("Error: The object passed is not a tkinter Button.")
            print(f"Received type: {type(button)}")
    else:
        amount = check_borders(row, column)
        try:
            button[row][column].config(text=amount)
        except AttributeError:
            print("Error: The object passed is not a tkinter Button.")
            print(f"Received type: {type(button)}")
    
    
    
    
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
