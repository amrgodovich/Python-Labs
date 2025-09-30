# ---------------------------------------------------------------------
#                               Lap4
# ---------------------------------------------------------------------

# Task Description:
# design and implement a Tic-Tac-Toe game in Python using Object-Oriented Programming (OOP) concepts.
# The game should allow the player to choose whether to play with a friend (human vs human) or against the computer (human vs computer).

# Requirements:

# 1. Core Classes:
#    - Player
#      - Attributes: name, symbol (X or O).
#      - Methods: make_move(board).
#    - HumanPlayer (inherits from Player)
#      - Implements make_move() by asking the user for input.
#    - ComputerPlayer (inherits from Player)
#      - Implements make_move() by choosing a move automatically (random or simple strategy).
#    - Board
#      - Attributes: 3x3 grid.
#      - Methods: display(), update(position, symbol), check_winner(), is_full().
#    - Game
#      - Attributes: players, board, current_turn.
#      - Methods: play(), switch_turns().

# 2. OOP Concepts to Use:
#    - Encapsulation: Keep the board grid private, only modify it using methods.
#    - Inheritance: HumanPlayer and ComputerPlayer inherit from Player.
#    - Polymorphism: make_move() behaves differently depending on the type of player.
#    - Special Methods: Implement __str__() for board display formatting.

# 3. Game Flow:
#    - The program starts by asking:
#      Do you want to play with a friend (1) or vs computer (2)?
#    - If option 1 → two human players enter their names.
#    - If option 2 → one human player enters their name, and the opponent is the computer.
#    - Players take turns placing X or O on the grid.
#    - After each move, the board is displayed.
#    - The game checks if a player has won or if the board is full (draw).
#    - Print the winner or “It’s a draw!” at the end.

# Deliverables:
# - A single Python script (tic_tac_toe.py).
# - The game must run from the terminal using:
#   python tic_tac_toe.py
# - Code should be clean, well-structured, and commented.
# - Every student must attach Code and screenshots of the game in BOTH modes (one with a friend and one against the computer) and place them inside a lab4 folder.



import random

# --------------------------- Player Classes ---------------------------

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board):
        raise NotImplementedError("Subclasses must implement make_move()")


class HumanPlayer(Player):
    def make_move(self, board):
        while True:
            try:
                move = int(input(f"{self.name} ({self.symbol}), enter your move (1-9): "))
                if move < 1 or move > 9:
                    print("Invalid input! Enter a number between 1 and 9.")
                    continue
                if not board.update(move, self.symbol):
                    print("That position is already taken. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input! Enter a number between 1 and 9.")


class ComputerPlayer(Player):
    def make_move(self, board):
        available_moves = [i for i in range(1, 10) if board.is_empty(i)]
        move = random.choice(available_moves)
        print(f"{self.name} ({self.symbol}) chooses position {move}")
        board.update(move, self.symbol)


# --------------------------- Board Class ---------------------------

class Board:
    def __init__(self):
        self.__grid = [" "] * 9

    def display(self):
        print("\n")
        for i in range(3):
            print(" " + " | ".join(self.__grid[i*3:(i+1)*3]))
            if i < 2:
                print("---+---+---")
        print("\n")

    def __str__(self):
        rows = []
        for i in range(3):
            rows.append(" " + " | ".join(self.__grid[i*3:(i+1)*3]))
        return "\n---+---+---\n".join(rows)

    def update(self, position, symbol):
        if self.__grid[position - 1] == " ":
            self.__grid[position - 1] = symbol
            return True
        return False

    def is_empty(self, position):
        return self.__grid[position - 1] == " "

    def check_winner(self, symbol):
        win_conditions = [
            [0,1,2], [3,4,5], [6,7,8],  # rows
            [0,3,6], [1,4,7], [2,5,8],  # columns
            [0,4,8], [2,4,6]            # diagonals
        ]
        for condition in win_conditions:
            if all(self.__grid[i] == symbol for i in condition):
                return True
        return False

    def is_full(self):
        return " " not in self.__grid


# --------------------------- Game Class ---------------------------

class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.current_turn = 0  # Index of current player

    def switch_turns(self):
        self.current_turn = 1 - self.current_turn

    def play(self):
        self.board.display()

        while True:
            current_player = self.players[self.current_turn]
            current_player.make_move(self.board)
            self.board.display()

            if self.board.check_winner(current_player.symbol):
                print(f"{current_player.name} wins")
                break

            if self.board.is_full():
                print("draw!")
                break

            self.switch_turns()


# --------------------------- Main ---------------------------

def main():
    print("welcome to the game")
    print("enter ur opponent")
    print("1. friend")
    print("2. Computer")
    mode = input("Vs: ")

    if mode == "1":
        name1 = input("Enter Player 1 name: ")
        name2 = input("Enter Player 2 name: ")
        player1 = HumanPlayer(name1, "X")
        player2 = HumanPlayer(name2, "O")
    else:
        name1 = input("Enter your name: ")
        player1 = HumanPlayer(name1, "X")
        player2 = ComputerPlayer("Computer", "O")

    game = Game(player1, player2)
    game.play()


if __name__ == "__main__":
    main()
