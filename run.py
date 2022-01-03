class GameBoard:
    """
    Main board class. Sets board size, the number of ships,
    the player's name and the board type (player board or computer).
    Has also methods for adding ships and guesses and printing the board
    """
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.num_ships = num_ships
        self.name = name
        self.type = type


def get_player_name():
    """
    Get name input from player
    """
    while True:

        get_name = input("Please enter a name with no more than 10 characters:\n")
        name_is = get_name

        if validate_name(name_is):
            print("-" * 35)
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
                f"No more than 10 characters required, you entered {len(values)}"
                )
    except ValueError as e:
        print(f"Invalid name: {e}, please try again.\n")
        return False

    return True


def new_game():
    """
    Run all games functions and starts a new game.
    Sets the board size and number of ships, resets
    the scores and initialises the boards.
    """
    size = 6
    num_ships = 5
    print("+", "-" * 35, "+")
    print("   Welcome to BATTLESHIP WAR GAME !!")
    print(f"   Board size: {size}. Number of ships: {num_ships}")
    print("   Top left corner is row: 0, col: 0")
    print("+", "-" * 35, "+")
    get_player_name()

    ai_board = GameBoard(size, num_ships, "AI", type="AI")




new_game()
