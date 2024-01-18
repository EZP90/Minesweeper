from random import *
from tkinter import *
import helpers




# Ein Fenster erstellen
window = Tk()
# Den Fenstertitle erstellen
window.title("Minesweeper")

x = 10
y = 10
mine_count = 10
mines = []

for i in range(mine_count):
    mines = sample(range(0,x*y), mine_count)



reset_button  = Button(window, height = 1, width = 5, text="Reset", command=helpers.reset()).grid()
exit = Button(window, height = 1, width = 5, text="Close", command=window.quit).grid()

mine = [[dim for dim in range(y)] for dim in range(x)]  # x*y dimensional list of lists
mine_label = Label()

for i in range(x):
    for j in range(y):
        # arrange the Buttons in a grid in x*y dimension and call check_mines on click with row and column as parameter
        mine_button = Button(window, height=1, width=1, command=lambda row=i, column=j: helpers.check_mines(row, column, mines, mine_count)).grid(row=i+1, column=j+1, padx=0, pady=0)   

# print(mine) # test



# In der Ereignisschleife auf Eingabe des Benutzers warten.
window.mainloop()