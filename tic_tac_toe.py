matrix1 = [" ", "|", " ", "|", " "]
matrix2 = [" ", "|", " ", "|", " "]
matrix3 = [" ", "|", " ", "|", " "]


def check_hrz(check_list):
    if check_list[0] == check_list[2] == check_list[4] != " ":
        print("winner is", check_list[0])


def update_list():
    empty_list1 = ""
    for line in matrix1:
        empty_list1 += line
        # print(empty_list1)
    empty_list2 = ""
    for line2 in matrix2:
        empty_list2 += line2
    empty_list3 = ""
    for line3 in matrix3:
        empty_list3 += line3

    print(empty_list1)
    print('_ _ _')
    print(empty_list2)
    print('_ _ _')
    print(empty_list3)

    if empty_list1[0] == empty_list2[2] == empty_list3[4] != " " or empty_list1[4] == empty_list2[2] == empty_list3[0] != " ":
        print("Winner is diagonal:", empty_list2[2])

    for x in [empty_list1, empty_list2, empty_list3]:
        check_hrz(x)

    for n in [0, 2, 4]:
        if empty_list3[n] == empty_list2[n] == empty_list1[n] != " ":
            print("Winner is:", empty_list3[n])

update_list()

player1 = input("What figure do you want to play? X/O:").capitalize()
if player1 == "X":
    player2 = "O"
else:
    player2 = "X"


def player(position, player):
    if 0 < position < 4:
        if position == 1:
            matrix3[0] = player
        elif position == 2:
            matrix3[2] = player
        else:
            matrix3[4] = player
    elif 3 < position < 7:
        if position == 4:
            matrix2[0] = player
        elif position == 5:
            matrix2[2] = player
        else:
            matrix2[4] = player
    else:
        if position == 7:
            matrix1[0] = player
        elif position == 8:
            matrix1[2] = player
        else:
            matrix1[4] = player


def player1_move():
    position_player1 = int(input("Chose a position on the board (1-9):"))
    player(position_player1, player1)
    update_list()


def player2_move():
    position_player2 = int(input("Chose a position on the board (1-9):"))
    player(position_player2, player2)
    update_list()


counter = 0
while counter < 10:
    player1_move()
    counter += 1
    if counter == 9:
        print("No winner")
        break
    player2_move()
    counter += 1
    if counter == 9:
        print("No winner")
        break

