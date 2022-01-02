# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def get_user_name():
    """
    Get name input from user
    """
    while True:

        print("---Please enter a name with no more than 10 characters---")
        get_name = input("Please enter your name:\n")
        name_is = get_name

        if validate_name(name_is):
            print("Name is valid!")
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

    """
    try:
        if str.isalpha(user_name):
            raise ValueError(
                f"Only letters required, you provided {user_name}"
            )
    except ValueError as e:
        print(f"Invalid entry: {e}, please try again\n")
        return False
    """

    return True


def main():
    """
    Run all program functions
    """
    user_name = get_user_name()


print("----------------------------------\nWelcome to BATTLESHIP WAR GAME !!\nBoard size: 6. Number of ships: 5\nTop left corner is row: 0, col: 0\n----------------------------------\n")
main()
