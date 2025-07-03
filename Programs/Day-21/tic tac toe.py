
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]

    def print_board(self):
        row1 = '| {} | {} | {} |'.format(self.board[0], self.board[1], self.board[2])
        row2 = '| {} | {} | {} |'.format(self.board[3], self.board[4], self.board[5])
        row3 = '| {} | {} | {} |'.format(self.board[6], self.board[7], self.board[8])

        print()
        print(row1)
        print(row2)
        print(row3)
        print()

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_cells(self):
        return ' ' in self.board

    def num_empty_cells(self):
        return self.board.count(' ')

    def make_move(self, letter, move):
        self.board[move] = letter

    def check_winner(self):
        winning_combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for combo in winning_combos:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return self.board[combo[0]]
        if ' ' not in self.board:
            return 'Tie'
        return False

def main():
    game = TicTacToe()
    current_player = 'X'

    while True:
        game.print_board()
        move = input("Player {}, enter your move (1-9): ".format(current_player))
        if move.isdigit() and 1 <= int(move) <= 9 and game.board[int(move) - 1] == ' ':
            game.make_move(current_player, int(move) - 1)
            result = game.check_winner()
            if result:
                game.print_board()
                if result == 'Tie':
                    print("It's a tie!")
                else:
                    print("Player {} wins! Congratulations!".format(result))
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move, try again.")

if __name__ == "__main__":
    main()

