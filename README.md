# Battleship War Game

## Code Institute Project Portfolio 03

Battleship is a terminal game programed with Python, which runs in the Code Institute mock terminal on Heroku.

It's a funny and a widely-known board game in which the goal is to destroy the opposing player's fleet.
It all depends on the luck of your finding shots to initially hit your targets.

[Here is the live version of the live game](assets/image/am-i.jpg)

Image from [Am I Responsive](http://ami.responsivedesign.is/).

## UX

I wanted to create a simple Battleship game for anyone, for them to have fun in a very easy way to input data.

## How to play

In this version of Battleship the user starts the game by first typing the name of the player.
Then the game will lunch the game boards and randomly populate 5 ships. 
The player will then be ask to enter coordinates to find out the AI ships and sink them.
The grid always start on: 0 row and 0 column. Guesses are marked on the board with an X
and hits are marked by *. To win the whole game, you will have to sink all the AI's ships before
it sinks yours!

## Features

### Existing Features

- __Start the Battle__

    - One board each are generated on the specified grid size
    - Ships are randomly placed on the player and the AI board
    - The player can see where his ships are located by a (@) mark
    - The player can not see where the AI ships are located on the board

![Board](assets/image/start-battle.jpg)


- __In game Guess__
    
    - Player input implemented
    - Viewing in game score
    - View chosen guess

![Board](assets/image/in-game.jpg)


- __In game Validation__

    - Only numbers are verified as an input
    - The player can't guess the same coordinates twice
    - Coordinates outside the grid size are not allowed
    - The Data is maintained in class instances

![Board](assets/image/in-valid.jpg)



### Features Let to Implement
I'd like to implement:
- Allow user to position ships themselves
- Make row with numbers and columns with letters

## Data Model

I chosen the option to use two classes for the game model. One GameBoard class and the othe Game class.

- __GameBoard Class__

    - self.size = To set the board size
    - self.name = To get the name of players
    - self.num_ships = To set number of ships in-game
    - self.player = Bolian indicate if the board belongs to a player or AI
    - self.board = To set up the board printing
    - self.guesses = List of passed guesses
    - self.placing_ships = Creates in-memory board with the players ship

- __Game Class__

    - self.size = To set the board size
    - self.num_ships = To set number of ships in-game
    - self.scores = Set score when ship is sunk

## Testing

- Code validator and test

    - [PEP 8 linter](http://pep8online.com/)
    - No errors were found when passing through the test

- Manual invalid inputs
    - Validate that Value Error is given to the player when wrong value is entered
    - Write string, text instead of numbers when numbers are expected
    - Out of bounds inputs example out of grid number
    - Same guess cannot be performed more than once

- Local terminal and the Code institute Heroku terminal
    - Test done on my local terminal in Gitpod
    - Test done when project was deployed on Heroku with the Code Institute mockup terminal


## Bugs

No known bugs


- Validator Testing
    - PEP 8
![](assets/image/pep.jpg)

## Languages, Frameworks, IDE, Librarires and Programs

[Python](https://en.wikipedia.org/wiki/History_of_Python)
    - The programming language Python was used. 

[GitHub:](https://github.com/)
- GitHub was used to store the projects code after being pushed from Git.

[Gitpod:](https://www.gitpod.io/)
- Was used to complement the development and write my project and push all commits through integrated "git" to Github.

[Heroku:](https://www.heroku.com/what)
- Was used for deployment of the project live in the cloud.
