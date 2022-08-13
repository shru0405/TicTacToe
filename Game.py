import os
from turtle import clear


def board():
    print(" __ __ __")
    print("  |" + a[0][0] + " |" + a[0][1] + " |" + a[0][2] + " |")
    print("  |__|__|__|")
    print("  |" + a[1][0] + " |" + a[1][1] + " |" + a[1][2] + " |")
    print("  |__|__|__|")
    print("  |" + a[2][0] + " |" + a[2][1] + " |" + a[2][2] + " |")
    print("  |__|__|__|\n")
def isWin(p):
    for i in range(0 , 3) :
        if (a[i][0] == a[i][1] == a[i][2]) or (a[0][i] == a[1][i] == a[2][i]) or (a[0][0] == a[1][1] == a[2][2]) or (a[0][2] == a[1][1] == a[2][0]) :
            print("PLAYER " + p + " WINS!!!")
            return True
a = [["1" , "2" , "3"] , ["4" , "5" , "6"] , ["7" , "8" , "9"]]
p , q = 0,0
def game() :
    board()
    turn = 0
    while turn <= 9:
        x = input("Player 1 enter cell number: ")
        try :
            x = int(x)
            if x not in range(1,10):
                print("Entry not valid")
                continue
        except:
            print("Entry not valid")
            continue
        p ,q = int((x/3) - 0.1), ((x + 3) % 3) - 1
        if a[p][q] in ["\x1b[32mO\x1b[0m", "\x1b[31mX\x1b[0m"]:
            print("Cell is already filled")
            continue
        a[p][q] = "\x1b[31mX\x1b[0m]"
        os.system('clear')
        os.system('cls')
        board()
        if isWin("1"):
            break
        turn = turn + 1
        if turn == 9:
            print("ITS A DRAW!!!")
            break
        while True:
            o = input("Player 2 enter cell number: ")
            try:
                o = int(o)
                if o not in range(1,10):
                    print("Entry not valid")
                    continue
            except:
                print("Entry not valid")
                continue
            p , q = int((o/3) - 0.1) , ((o + 3) % 3) - 1
            if a[p][q] in [ "\x1b[32mO\x1b[0m", "\x1b[31mX\x1b[0m" ]:
                print("Cell is already filled")
                continue
            a[p][q] = "\x1b[32mO\x1b[0m"
            os.system('clear')
            os.system('cls')
            board()
            if isWin("2"):
                turn = 10
                break
            turn = turn + 1
            break
game()
while True:
    x = input("Rematch? (y/n): ")
    if x == "y":
        os.system('clear')
        os.system('cls')
        a = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        game()
    elif x == "n" :
        os.system('clear')
        os.system('cls')
        exit()
    else:
        print("Please give a valid input")
        continue
