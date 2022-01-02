# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

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


def new_game():
    """
    Run all games functions and starts a new game.
    Sets the board size and number of ships, resets
    the scores and initialises the boards.
    """

    #size = 6
    #num_ships = 5
    #scores["player"] = 0
    #scores["ai"] = 0
    print("-" * 35)
    print("Welcome to BATTLESHIP WAR GAME !!")
    print("Board size: 6. Number of ships: 5")
    print("Top left corner is row: 0, col: 0")
    print("-" * 35)

    user_name = get_user_name()


new_game()
