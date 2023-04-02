import datetime


class Board:
    def __init__(self):

        self.string_board = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
        self.empty = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        print("Board was successfully build!\n")

    def display_board(self, board):
        print("\n%s | %s | %s |" % (board[0], board[1], board[2]))
        print("-" * 11)
        print("%s | %s | %s |" % (board[3], board[4], board[5]))
        print("-" * 11)
        print("%s | %s | %s |" % (board[6], board[7], board[8]))

    def player_input(self, player: int, board: []):

        try:
            symbols = ["O", "X"]

            # Assume that cell is empty
            is_cell_empty = True

            # Get user input
            position = int(input("Player %d, choose field for symbol %s: " % (player + 1, symbols[player])))

            # Check if user's input is a valid controller input.
            if position not in range(9):
                print("not a member of [0, 1, 2, 3, 4, 5, 6, 7, 8]")
                self.display_board(board=board)

            # Check if user's position-input is filled by O or X
            if board[position] == symbols[0] or board[position] == symbols[1]:
                is_cell_empty = False

            # Tell the user that the cell is already taken
            if not is_cell_empty:
                print("The cell is already taken! Enter a cell that is empty\n")
                self.display_board(board=board)

            else:
                # Remove int from list
                self.empty.remove(position)

                board[position] = symbols[player]
        except Exception as inst:
            print("An exception was caught:", inst)

    def check_win(self, board):
        '''


        :param board: Board object
        :return: 0 or 1
        '''
        for win_combination in self.win_combinations:
            won = True
            # Check if the character 'O' exists in a win combination
            if board[win_combination[0]] == board[win_combination[1]] == board[win_combination[2]] == 'O':
                print("O wins!")
                self.display_board(board=board)
                self.play_again()  # conditional end of program

            # Check if the character 'X' exists in a win combination
            if board[win_combination[0]] == board[win_combination[1]] == board[win_combination[2]] == 'X':
                print("X wins!")
                self.display_board(board=board)
                self.play_again()  # conditional end of program

            else:
                won = False

        if won:
            return 0
        else:
            return 1

    def play_toe(self):
        player = 0

        while self.empty and self.check_win(self.string_board):
            self.display_board(self.string_board)
            print("\n")
            self.player_input(player, self.string_board)
            player = int(not player)

        if not self.empty:
            self.display_board(self.string_board)
            print("It is a draw!\n")
            self.play_again()

    def play_again(self):
        while True:
            ask = input("Rematch? y/n: ").lower()
            if ask[0] == 'y':
                print("Ok! Reinitialising a new board")
                self.string_board = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
                self.empty = [0, 1, 2, 3, 4, 5, 6, 7, 8]
                self.play_toe()

            elif ask[0] == 'n':
                datetime_now = datetime.datetime.now().strftime("%Y-%m-%d-%X")
                print("Ok! Program quiting %s" % datetime_now)
                quit()

            else:
                print("Program could not handle that")
                self.play_again()
