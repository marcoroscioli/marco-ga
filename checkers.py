# Define constants for the board size and empty cell representation
EMPTY = ' '
WHITE_PIECE = "@"
BLACK_PIECE = "#"

# Initialize the 8x8 board with empty spaces
board = [[EMPTY for _ in range(8)] for _ in range(8)]

# Function to print the 2D array in a readable format
def print_board(board):
    # Print column headers
    print("   a  b  c  d  e  f  g  h")
    
    # Print each row with row numbers
    for row in range(8):
        row_str = str(row + 1) + " "
        for col in range(8):
            row_str += "[" + board[row][col] + "]"
        print(row_str)
        
# Place a single white piece on the board
def init_board():
	board[0][0] = BLACK_PIECE
	board[0][2] = BLACK_PIECE
	board[0][4] = BLACK_PIECE
	board[0][6] = BLACK_PIECE
	board[1][1] = BLACK_PIECE
	board[1][3] = BLACK_PIECE
	board[1][5] = BLACK_PIECE
	board[1][7] = BLACK_PIECE
	board[2][0] = BLACK_PIECE
	board[2][2] = BLACK_PIECE
	board[2][4] = BLACK_PIECE
	board[2][6] = BLACK_PIECE
	board[5][1] = WHITE_PIECE
	board[5][3] = WHITE_PIECE
	board[5][5] = WHITE_PIECE
	board[5][7] = WHITE_PIECE
	board[6][0] = WHITE_PIECE
	board[6][2] = WHITE_PIECE
	board[6][4] = WHITE_PIECE
	board[6][6] = WHITE_PIECE
	board[7][1] = WHITE_PIECE
	board[7][3] = WHITE_PIECE
	board[7][5] = WHITE_PIECE
	board[7][7] = WHITE_PIECE

# Main function to initialize and display the board
def main():
    print_board(board)
    init_board()
    print_board(board)
    player_move = input("Make your move")      #computer_move = move[0:2]
    board[5][1] = EMPTY
    board[4][2] = WHITE_PIECE
    print_board(board)

    
# Run the main function
if __name__ == "__main__":
    main()