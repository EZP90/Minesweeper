import random
from tkinter import *
import helpers




# Ein Fenster erstellen
window = Tk()
# Den Fenstertitle erstellen
window.title("Minesweeper")

x = 10
y = 10



reset_button  = Button(window, text="Reset", command=helpers.reset())
exit = Button(window, text="Close", command=window.quit)

mine = [[dim for dim in range(y)] for dim in range(x)]  # x*y dimensional list of lists

for i in range(x):
    for j in range(y):
        mine_button = Button(window, command=helpers.check_mines(), text=str(i)+str(j)).grid(row=i+1, column=j+1, padx=0, pady=0)   # arrange the Buttons in a grid in x*y dimension

# print(mine) # test


# In der Ereignisschleife auf Eingabe des Benutzers warten.
window.mainloop()