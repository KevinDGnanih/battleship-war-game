from random import randint


scores = {"player": 0, "ai": 0}


class Board:
    """
    Main board class. Sets board size, the number of ships,
    the player's name and the board type (player board or computer).
    Has also methods for adding ships and guesses and printing the board
    """

    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.num_ships = [["." for x in range(size)] for y in range(size)]
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print(self):
        for row in self.board:
            print("".join(row))

    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"

    def add_ship(self, x, y, type="ai"):
        if len(self.ships) >= self.num_ships:
            print("Error: you cannot add any more ships!")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "@"

def get_user_name():
    """
    Get name input from user
    """
    while True:

        print("Please enter a name with no more than 10 characters")
        get_name = input("Please enter your name:\n")
        name_is = get_name

        if validate_name(name_is):
            print("----------------------------------\n")
            break

    return name_is


def validate_name(values):
    """
    Raises ValueError if the string has other characters than letters
    and has no more than 15 letters
    """

    try:
        if len(values) > 10:
            raise ValueError(
                f"No more than 10 characters required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid name: {e}, please try again.\n")
        return False

    return True


def random_point(size):
    """
    Helper function to return a random integer between 0 and size
    """
    return randint(0, size - 1)

#def valid_coordinates(x, y, board):


#def make_guess(board):


def play_game(ai_board, player_board):
    print("Coucou")



def new_game():
    """
    Run all games functions and starts a new game.
    Sets the board size and number of ships, resets
    the scores and initialises the boards.
    """

    size = 6
    num_ships = 5
    scores["player"] = 0
    scores["ai"] = 0
    print("-" * 35)
    print("Welcome to BATTLESHIP WAR GAME !!")
    print("Board size: 6. Number of ships: 5")
    print("Top left corner is row: 0, col: 0")
    print("-" * 35)

    #player_board = Board(size, num_ships, user_name, type="player")
    #ai_board = Board(size, num_ships, "ai", type="ai")

    user_name = get_user_name()
    play_game(player_board, ai_board)


new_game()

