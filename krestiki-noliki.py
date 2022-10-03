board=["-" for a in range (1,10)]
def print_board():
    print("    1 2 3")
    for i in range(3):
        print(i+1," ", board[0+i*3], board[1+i*3], board [2+i*3])

def choose_box(player):
    x = int(input(f"Введите номер строки, куда поставить {player}: "))
    while not 0 < x < 4:
        x = int(input("Неправильно введен номер строки, введите 1, либо 2, либо 3: "))
    y = int(input(f"Введите номер столбца, куда поставить {player}: "))
    while not 0 < y < 4:
        y = int(input("Неправильно введен номер столбца, введите 1, либо 2, либо 3: "))
    choise= (x-1)*3 + y-1
    return choise

def win_check(player):
    win_comb = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_comb:
        if board[each[0]] == board[each[1]] == board[each[2]] == player:
            return player
    return False

def game():
    step=0
    win = False
    while not win:
        print_board()
        if step % 2 == 0:
            symbol = "X"
        else:
            symbol = "O"
        choise = choose_box(symbol)
        while board[choise] in "XO":
            print("Клетка уже занята, повторите ввод")
            choise = choose_box(symbol)
        board[choise] = symbol
        win = win_check(symbol)
        if win:
            print_board()
            print(f"{win} выиграл!")
            break
        step += 1
        if step == 9:
            print("Ничья!")
            break
    print("Игра закончена!")

game()



