import numpy as np # type: ignore
def completion(arr):
    global a
    rows, cols = arr.shape
    for row in range(rows):
        for col in range(cols-3):
            if np.all(arr[row,col] == arr[row,col+1] == arr[row,col+2] ==arr[row,col+3] and arr[row,col] != 0):
                print(f' user{arr[row,col]} win the game')
                a = 0
                return a
    for col in range(cols):
        for row in range(rows-3):
            if np.all(arr[row,col] == arr[row+1,col] == arr[row+2,col] ==arr[row+3,col] and arr[row,col] != 0):
                print(f' user{arr[row,col]} win the game')
                a = 0
                return a

                
    for col in range(cols-3):
        for row in range(rows-3):
            if np.all(arr[row,col] == arr[row+1,col+1] == arr[row+2,col+2] ==arr[row+3,col+3] and arr[row,col] != 0):
                print(f' user{arr[row,col]} win the game')
                a = 0
                return a
                
    for col in range(cols-3):
        for row in range(rows-3):
            if np.all(arr[row,col] == arr[row+1,col-1] == arr[row+2,col-2] ==arr[row+3,col-3] and arr[row,col] != 0):
                print(f' user{arr[row,col]} win the game')
                a = 0
                return a

def no_space_in_column(column):
    while z[0,column] == -7:
        column = input("The column you have choosed is full; please make another choice")
        if z[:] == -7:
            print("There is no winner")
            a = 0
        

def filling(column,collect_4,turn):
    collect_4[z[0,column],column] = turn
    z[0,column] = z[0,column] - 1
    print(collect_4)
    collect_4 = collect_4.astype(int)


collect_4 = np.zeros((7,7))
print(collect_4)
z = np.full((1,7),-1)
a = 1
column = 0

while a == 1:
    user_1 = int(input("User1 : choose your column:")) -1
    column = user_1
    turn = 1
    no_space_in_column(column)
    filling(column,collect_4,turn)
    completion(collect_4)
    if a == 0:
        break

    user_2 = int(input("User2 : choose your column:")) -1
    column = user_2
    turn = 2
    no_space_in_column(column)
    filling(column,collect_4,turn)
    completion(collect_4)
    if a == 0:
        break