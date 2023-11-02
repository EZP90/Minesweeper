import random
from tkinter import *
import reset



# Ein Fenster erstellen
window = Tk()
# Den Fenstertitle erstellen
window.title("Minesweeper")



reset  = Button(window, text="Reset", command=reset.reset())
exit = Button(window, text="Close", command=window.quit)





# In der Ereignisschleife auf Eingabe des Benutzers warten.
window.mainloop()