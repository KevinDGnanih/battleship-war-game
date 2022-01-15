"""
BATTLESHIP WAR GAME
"""

from random import randint


def random_coordinate(grid_size):
    """
    Returns a random coordinate
    """
    row = randint(0, grid_size - 1)
    column = randint(0, grid_size - 1)
    return (row, column)


class GameBoard:
    """
    Mainboard class. Sets board size, the number of ships,
    the player's name, and if it's a computer playing or a player.
    Has methods for adding ships and guesses and printing the board
    """

    def __init__(self, size, num_ships, name, player=False):
        self.size = size
        self.num_ships = num_ships
        self.name = name
        self.player = player
        self.board = [["~" for row in range(size)] for column in range(size)]
        self.ships = []
        self.guesses = []
        self.placing_ships()

    def print_style(self):
        """
        Prints the board for AI and player with the name
        """
        print(f"{self.name}'s Board:")
        for row in self.board:
            print(" ".join(row))

    def guess(self, row, column):
        """
        Mark a guess on the board
        """
        self.guesses.append((row, column))
        self.board[row][column] = "X"

        if (row, column) in self.ships:
            self.board[row][column] = "*"
            return True
        else:
            return False

    def already_guessed(self, row, column):
        """
        Returns True if the coordinates have already been guessed before
        """
        if (row, column) in self.guesses:
            return True
        return False

    def last_shoot(self):
        """
        Returns the last shoot
        """
        return self.guesses[-1]

    def placing_ships(self):
        """
        Placing  ships on the board
        """
        for _ in range(self.num_ships):
            row, column = random_coordinate(self.size)
            while (row, column) in self.ships:
                row, column = random_coordinate(self.size)
            self.ships.append((row, column))
            if self.player:
                self.board[row][column] = "@"


class Game:
    """
    Class to initialize the game, set up the player boards and
    other parameters and handle the playing of it
    """

    def __init__(self, size, num_ships):
        self.size = size
        self.num_ships = num_ships
        self.scores = {"ai": 0, "player": 0}

    def new_game(self):
        """
        Show welcome screen, initialize the boards and start the game
        """
        print("+", "-" * 35, "+")
        print("   Welcome to BATTLESHIP WAR GAME !!")
        print("   Board size: 6. Number of ships: 5")
        print("   Top left corner is row: 0, col: 0")
        print("+", "-" * 35, "+")
        self.play_game()

    def play_game(self):
        """
        The main game loop takes care of guesses and exits the game if it's
        completed or if the player no longer wants to play.
        """
        player_name = input("Please enter your name:\n")
        print("+", "-" * 35, "+")
        player_board = GameBoard(self.size, self.num_ships, player_name,
                                 player=True)
        self.player_board = player_board
        ai_board = GameBoard(self.size, self.num_ships, "AI", player=False)
        self.ai_board = ai_board

        while True:
            self.print_boards()
            if self.game_over():
                self.overall_winner()
                restart_choice = input("Type \"yes\" if you would like to" +
                                       " quit the game or anything else to" +
                                       " start again\n")
                if restart_choice == "yes":
                    break
                else:
                    self.new_game()

            # player guess
            row, column = self.ask_guess()
            while not self.valid_guess(row, column):
                row, column = self.ask_guess()
            player_hit = self.ai_board.guess(row, column)

            # computer guess
            row, column = random_coordinate(self.size)
            while self.player_board.already_guessed(row, column):
                row, column = random_coordinate(self.size)
            ai_hit = self.player_board.guess(row, column)

            # end of round
            self.round_info(player_hit, ai_hit)
            choice = input("Type \"quit\" to quit or anything else " +
                           "to continue.\n")
            if choice == "quit":
                break

    def overall_winner(self):
        """
        Naming the overall winner
        """
        diff = self.scores["player"] - self.scores["ai"]

        if diff < 0:
            print("AI won")
        elif diff > 0:
            print("You WON")
        else:
            print("It's a tie...")

    def ask_guess(self):
        """
        Asks the user for row and column and validate that they are numbers
        before returning them
        """
        while True:
            try:
                print("-" * 45)
                row = input("Guess a row:\n")
                row = int(row)
                column = input("Guess a column:\n")
                column = int(column)
                break
            except ValueError:
                print("Row and column must be numbers")

        return (row, column)

    def print_boards(self):
        """
        Print current board status on screen
        """
        self.player_board.print_style()
        self.ai_board.print_style()

    def valid_guess(self, row, column):
        """
        Returns True if the coordinates are within the board grid and if they
        haven't been guessed before
        """

        try:
            if not 0 <= row < 6:
                raise ValueError(
                    print("Row and column must be between 0 and 5," +
                          f"you entered {row}, {column}")
                )
            if not 0 <= column < 6:
                raise ValueError(
                    print("Row and column must be between 0 and 5," +
                          f"you entered {row}, {column}")
                )
            if self.ai_board.already_guessed(row, column):
                print("Ouppss, you cannot enter twice the same coordinates")
                return False
        except ValueError as error:
            print(f"Invalide coordinates: {error}, please try again.\n")
            return False

        return True

    def game_over(self):
        """
        Checks if either player has sunk the other player's battle ships
        """
        if self.scores["player"] == self.num_ships or \
           self.scores["ai"] == self.num_ships:
            return True
        return False

    def round_info(self, player_hit, computer_hit):
        """
        Output the scores after each round
        """
        print("+", "-" * 35, "+")
        print(f"You guessed: {self.ai_board.last_shoot()}")

        if player_hit:
            self.scores["player"] += 1
            print("That was a HIT!!!")
        else:
            print("Oh no you a miss!")

        print(f"AI guessed: {self.player_board.last_shoot()}")

        if computer_hit:
            self.scores["ai"] += 1
            print("That was a HIT!!!")
        else:
            print("That was a miss!")

        print("+", "-" * 35, "+")
        print("\nAfter this round, the scores are:")
        print(f"{self.player_board.name}:" +
              f"{self.scores['player']} . AI:{self.scores['ai']}")
        print("+", "-" * 35, "+")


game = Game(size=6, num_ships=5)
game.new_game()
