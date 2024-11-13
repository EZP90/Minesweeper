
import tkinter as tk
import helpers
from functools import partial




# Ein Fenster erstellen
window = tk.Tk()
# Den Fenstertitle erstellen
window.title("Minesweeper")

topframe = tk.Frame(window, bg="grey", padx=10, pady=10)
topframe.pack(side="top")
mineframe = tk.Frame(window, bg="grey", padx=0, pady=0)
mineframe.pack(fill="both", expand=True)

x = 10
y = 10
mine_count = 10
mine_button = [[dim for dim in range(y)] for dim in range(x)]  # x*y dimensional list of lists



reset_button  = tk.Button(topframe, text="Reset", command=partial(helpers.reset)).grid(row=0, column=0)
exit = tk.Button(topframe, text="Close", command=window.quit).grid(row=0, column=1)



helpers.set_mines(mine_count)

for i in range(x):
    for j in range(y):
        #print(i,j)
        # arrange the Buttons in a grid in x*y dimension and call check_mines on click with row and column as parameter
        mine_button[i][j] = tk.Button(mineframe, height=1, width=2, text=" ", command=partial(helpers.check_mines,i,j,mine_button))
        mine_button[i][j].grid(row=i+1, column=j+1, padx=0, pady=0)
        


# print(mine) # test



# In der Ereignisschleife auf Eingabe des Benutzers warten.
window.mainloop()