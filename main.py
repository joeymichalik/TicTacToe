# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Board:
    def __init__(self):
        self.state = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Turns the mark number into the mark as string
    @staticmethod
    def state_to_mark(number):
        if number == 0:
            return " "
        elif number == 1:
            return "X"
        else:
            return "O"

    # Prints the Playboard
    def print_board(self):
        print(" " + self.state_to_mark(self.state[0]) + " | " + self.state_to_mark(
            self.state[1]) + " | " + self.state_to_mark(self.state[2]) + " ")
        print(" " + self.state_to_mark(self.state[3]) + " | " + self.state_to_mark(
            self.state[4]) + " | " + self.state_to_mark(self.state[5]) + " ")
        print(" " + self.state_to_mark(self.state[6]) + " | " + self.state_to_mark(
            self.state[7]) + " | " + self.state_to_mark(self.state[8]) + " ")

    def board_full(self):
        for item in self.state:
            if item == 0:
                return False
        return True

    def make_move(self, grid_cell, player):
        self.state[grid_cell] = player.mark

    def check_state(self, grid_cell):
        if self.state[grid_cell] == 0:
            return True
        else:
            return False

    def check_win(self):
        # 0,1,2 - 3,4,5 - 6,7,8
        # 0,3,6 - 1,4,7 - 2,5,8
        # 0,4,8 - 2,4,6
        if self.state[0] == self.state[1] == self.state[2] != 0:
            return True
        elif self.state[3] == self.state[4] == self.state[5] != 0:
            return True
        elif self.state[6] == self.state[7] == self.state[8] != 0:
            return True
        elif self.state[0] == self.state[3] == self.state[6] != 0:
            return True
        elif self.state[1] == self.state[4] == self.state[7] != 0:
            return True
        elif self.state[2] == self.state[5] == self.state[8] != 0:
            return True
        elif self.state[0] == self.state[4] == self.state[8] != 0:
            return True
        elif self.state[2] == self.state[4] == self.state[6] != 0:
            return True
        else:
            return False


class Player:
    def __init__(self, mark):
        self.mark = mark


if __name__ == '__main__':
    p1 = Player(1)
    p2 = Player(-1)
    board = Board()
    active_player = 1

    while not board.board_full():
        board.print_board()
        print(board.state[0:9])
        if active_player == 1:
            print("PLAYER ONE: Place your mark! (1-9)")
        else:
            print("PLAYER TWO: Place your mark! (1-9)")
        try:
            cell = int(input()) - 1
        except ValueError:
            print('\033[31m' + "Type in a valid number!" + '\033[39m')
            continue
        if cell < 0 or cell > 8:
            print('\033[31m' + "Type in a valid number!" + '\033[39m')
            continue
        if board.check_state(cell):
            if active_player == 1:
                board.make_move(cell, p1)
            else:
                board.make_move(cell, p2)
            if board.check_win():
                print("Congrats!")
                board.print_board()
                if active_player == 1:
                    print("PLAYER ONE - YOU WON!")
                else:
                    print("PLAYER TWO - YOU WON!")
                break
            else:
                if active_player == 1:
                    active_player = 2
                else:
                    active_player = 1
        else:
            print('\033[31m' + "There's already a mark DUMBASS! Place it somewhere else..." + '\033[39m')
            continue
    else:
        board.print_board()
        print('\033[31m' + "No turns left! Good Luck next time!")