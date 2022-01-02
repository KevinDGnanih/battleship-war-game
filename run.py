def get_player_name():
    """
    Get name input from player
    """
    while True:

        print("Please enter a name with no more than 10 characters")
        get_name = input("Please enter your name:\n")
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
    print("-" * 35)
    print("Welcome to BATTLESHIP WAR GAME !!")
    print("Board size: 6. Number of ships: 5")
    print("Top left corner is row: 0, col: 0")
    print("-" * 35)


new_game()
