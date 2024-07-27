https://bit.ly/SMAPI15639
print("thank you for downloading file")
def draw_board(board):
  print('-------------')
  for i in range(3):
    print('|', board[i][0], '|', board[i][1], '|', board[i][2], '|')
    print('-------------')

def check_win(board):
  # تحقق من الصفوف والأعمدة والقطرين
  for i in range(3):
    if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
      return True
    if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
      return True
  if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
    return True
  if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
    return True
  return False

def play_game():
  board = [[' ' for _ in range(3)] for _ in range(3)]
  current_player = 'X'
  while True:
    draw_board(board)
    row = int(input("Enter row (1-3): ")) - 1
    col = int(input("Enter column (1-3): ")) - 1
    if board[row][col] != ' ':
      print("That spot is already taken. Try again.")
      continue
    board[row][col] = current_player
    if check_win(board):
      print(current_player, "wins!")
      break
    if all(all(cell != ' ' for cell in row) for row in board):
      print("Tie game.")
      break
    current_player = 'O' if current_player == 'X' else 'X'

play_game()
