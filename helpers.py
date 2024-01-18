

def reset():
    print("Reset")
    






def check_mines(row, column, mines, count):
    print(str(row)+str(column))
    for i in range(count):
        if(str(mines[i]) == str(row)+str(column)):
            print(True)

