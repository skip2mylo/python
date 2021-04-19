
#create an empty board
board = [
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
]

# put out the ships
board_ans = [
['x',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
]

#show the board
def print_board(x):
    count = 0
 
    for row in x:
        for i in row:
            if i == "x":
                print("[x_]",end="")
            elif i =="m":
                print("[m_]",end="")
            elif i ==" ":
                print("[__]",end="")
        print(count)
        count +=1
    print (" A   B   C   D   E   F   G   H   I   J  ")



#shoot
d = {
    "A":0,
    "B":1,
    "C":2,
    "D":3,
    "E":4,
    "F":5,
    "G":6,
    "H":7,
    "I":8,
    "J":9
}

def shooting(i,j):
    if board_ans[i][j] == "x":
        print("You hit the ship!")
        board[i][j] = "x"
    else:
        print("You missed")
        board[i][j] = "m"
    print_board(board)

def shoot():
    u_shoot =input("Shoot at (ex. B2):  ")
    row = int(u_shoot[1])
    col = d.get(u_shoot[0].upper())
    shooting(row,col)

print("Let's play a game!\n\n")
print_board(board)
turn = 5

while turn > 0:
    shoot()
    turn -=1    

    if board == board_ans:
        print("You win!!! Game ends")
        break

    if turn == 0:
        print("You lose...Game over")
        break
        
    print(f"You have {turn} times of tries left.")




  
