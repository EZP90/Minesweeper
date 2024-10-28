
import tkinter as tk
import helpers




# Ein Fenster erstellen
window = tk.Tk()
# Den Fenstertitle erstellen
window.title("Minesweeper")

x = 10
y = 10
mine_count = 10



reset_button  = tk.Button(window, text="Reset", command=helpers.reset())
exit = tk.Button(window, text="Close", command=window.quit)

mine = [[dim for dim in range(y)] for dim in range(x)]  # x*y dimensional list of lists

helpers.set_mines(mine_count)

for i in range(x):
    for j in range(y):
        # arrange the Buttons in a grid in x*y dimension and call check_mines on click with row and column as parameter
        mine_button = tk.Button(window, height=1, width=2, text=" ", command=lambda row=i, column=j: 
            helpers.check_mines(row, column)).grid(row=i+1, column=j+1, padx=0, pady=0)
        
        


# print(mine) # test


# In der Ereignisschleife auf Eingabe des Benutzers warten.
window.mainloop()