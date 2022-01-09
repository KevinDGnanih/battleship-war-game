"""
BATTLESHIP WAR GAME
"""
from random import randint


def random_coordinates(size):
    """
    Returns a random coordinate
    """
    row = randint(0, size - 1)
    column = randint(0, size - 1)
    return (row, column)


class GameBoard:
    """
    Figuring out everything for this class
    """
    def __init__(self, who, size, num_ships, name, player=False):
        self.who = who
        self.size = size
        self.num_ships = num_ships
        self.name = name
        self.player = player
        self.board = [["~" for row in range(size)] for column in range(size)]
        self.ships = []
        self.guesses = []
        self.placing_ships()

    def print_board(self):
        """
        Print the board for AI and player
        """
        for row in self.board:
            print(" ".join(row))

    def placing_ships(self):
        """
        Placing ships on the boards
        """
        for _ in range(self.num_ships):
            row, column = random_coordinates(self.size)
            while (row, column) in self.ships:
                row, column = random_coordinates(self.size)
            self.ships.append((row, column))
            if self.player:
                self.board[row][column] = "@"

    def ask_guess(self):
        """
        Asks the player to guess a row and a column then
        validate if the inputs are integers before to return them
        """
        while True:
            try:
                print("+", "-" * 35, "+")
                row = input("Guess a row:\n")
                row = int(row)
                column = input("Guess a column:\n")
                column = int(column)
                if valid_guess(row, column):
                    return self.guess(row, column)
            except ValueError:
                print("Row and column guesses must be numbers, please try again")

        return (row, column)

    def guess(self, row, column):
        """
        Make a guess and mark it on the board
        """
        self.guesses.append((row, column))
        self.board[row][column] = "X"

        if valid_guess(row, column):
            if (row, column) in self.ships:
                self.board[row][column] = "*"
            return True
        else:
            return False


def get_player_name():
    """
    Get name input from player
    """
    while True:

        get_name = input("Please enter a name:\n")
        name_is = get_name

        if validate_name(name_is):
            print("+", "-" * 35, "+")
            break

    return name_is


def validate_name(values):
    """
    Raises ValueError if the string has other characters than letters
    and has no more than 10 letters
    """

    try:
        if len(values) > 10:
            raise ValueError(
                f"10 characters maximum required, you entered {len(values)}"
                )
        if len(values) == 0:
            raise ValueError(
                f"You haven't enter any character {values}"
            )
    except ValueError as error:
        print(f"Invalid name: {error}, please try again.\n")
        return False

    return True


def valid_guess(row, column):
    """
    Returns True if the coordinates are within the board grid
    and if they haven't been guesses before
    """
    try:
        if not (0 <= row) < 6 and (0 <= column) < 6:
            raise ValueError(
                print("Row and column must be between 0 and 6")
            )

    except ValueError as error:
        print(f"Invalide coordinates: {error}, please try again.\n")
        return False

    return True


def play_game():
    """
    Starting the game functions
    """
    player_name = get_player_name()
    player_board = GameBoard(who="player", size=6, num_ships=5, name=player_name, player=True)
    ai_board = GameBoard(who="ai", size=6, num_ships=5, name="Computer")

    print(f"{player_name}'s Board:")
    player_board.print_board()
    print("AI Board:")
    ai_board.print_board()

    game_on = True

    while game_on:
        guess = player_board.ask_guess()
        if guess:
            game_on = False


def new_game():
    """
    Run all games functions and starts a new game.
    Sets the board size and number of ships, resets
    the scores and initialises the boards.
    """
    print("+", "-" * 35, "+")
    print("   Welcome to BATTLESHIP WAR GAME !!")
    print("   Board size: 6. Number of ships: 5")
    print("   Top left corner is row: 0, col: 0")
    print("+", "-" * 35, "+")
    play_game()


new_game()