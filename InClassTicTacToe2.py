name1 = input("Player one name: ")
name2 = input("Player two name: ")
initial1 = name1[0].upper()
initial2 = name2[0].upper()

board = "........."
#print intial position
print ("intial position:")
print(board[:3])
print(board[3:6])
print(board[6:])
print()
#sets up board 
print("Each move must be input as \"row, column\"")

player1 = input("%s: " % name1)
row1 = int(player1[0])
column1 = int(player1[-1])
index1 = (row1-1)*3 + (column1-1)
board = board[:index1] + initial1 + board[index1 + 1:]

print ("Updated position:")
print(board[:3])
print(board[3:6])
print(board[6:])
print()

player2 = input("%s: " % name2)
row1 = int(player2[0])
column1 = int(player2[-1])
# 0 and 1 refer to index of their input. 0 is the first and -1 is always the last input.
index1 = (row1-1)*3 + (column1-1)
board = board[:index1] + initial2 + board[index1 + 1:]

print ("Updated position:")
print(board[:3])
print(board[3:6])
print(board[6:])
print()

player1 = input("%s: " % name1)
row1 = int(player1[0])
column1 = int(player1[-1])
index1 = (row1-1)*3 + (column1-1)
board = board[:index1] + initial1 + board[index1 + 1:]

print ("Updated position:")
print(board[:3])
print(board[3:6])
print(board[6:])
print()

player2 = input("%s: " % name2)
row1 = int(player2[0])
column1 = int(player2[-1])
# 0 and 1 refer to index of their input. 0 is the first and -1 is always the last input.
index1 = (row1-1)*3 + (column1-1)
board = board[:index1] + initial2 + board[index1 + 1:]

print ("Updated position:")
print(board[:3])
print(board[3:6])
print(board[6:])
print()

player1 = input("%s: " % name1)
row1 = int(player1[0])
column1 = int(player1[-1])
index1 = (row1-1)*3 + (column1-1)
board = board[:index1] + initial1 + board[index1 + 1:]

print ("Updated position:")
print(board[:3])
print(board[3:6])
print(board[6:])
print()

player2 = input("%s: " % name2)
row1 = int(player2[0])
column1 = int(player2[-1])
# 0 and 1 refer to index of their input. 0 is the first and -1 is always the last input.
index1 = (row1-1)*3 + (column1-1)
board = board[:index1] + initial2 + board[index1 + 1:]

print ("Updated position:")
print(board[:3])
print(board[3:6])
print(board[6:])
print()

player1 = input("%s: " % name1)
row1 = int(player1[0])
column1 = int(player1[-1])
index1 = (row1-1)*3 + (column1-1)
board = board[:index1] + initial1 + board[index1 + 1:]

print ("Updated position:")
print(board[:3])
print(board[3:6])
print(board[6:])
print()

player2 = input("%s: " % name2)
row1 = int(player2[0])
column1 = int(player2[-1])
# 0 and 1 refer to index of their input. 0 is the first and -1 is always the last input.
index1 = (row1-1)*3 + (column1-1)
board = board[:index1] + initial2 + board[index1 + 1:]

print ("Updated position:")
print(board[:3])
print(board[3:6])
print(board[6:])
print()

player1 = input("%s: " % name1)
row1 = int(player1[0])
column1 = int(player1[-1])
index1 = (row1-1)*3 + (column1-1)
board = board[:index1] + initial1 + board[index1 + 1:]

print ("Updated position:")
print(board[:3])
print(board[3:6])
print(board[6:])
print()