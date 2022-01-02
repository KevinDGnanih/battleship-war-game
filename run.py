# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def get_user_name():
    """
    Get name input from user
    """

    user_name = input("Please enter your name:\n")

    return user_name


def main():
    """
    Run all program functions
    """
    user_name = get_user_name()
    


print("----------------------------------\nWelcome to BATTLESHIP WAR GAME !!\nBoard size: 6. Number of ships: 5\nTop left corner is row: 0, col: 0\n----------------------------------\n")
main()