# Battleship War Game

## Code Institute Project Portfolio 03

Battleship is a terminal game programed with Python, which runs in the Code Institute mock terminal on Heroku.

It's a funny and widely-known board game in which the goal is to destroy the opposing player's fleet.
It all depends on the luck of your finding shots to initially hit your targets.

![alt text](image/am-i.jpg)

Image from [Am I Responsive](http://ami.responsivedesign.is/).

Give it a try

The live link can be found here - https://battleship-war-kdg.herokuapp.com/

## UX

I wanted to create a simple Battleship game for anyone, for them to have fun in a very easy way to input data.

## How to play

In this version of Battleshi,p the user starts the game by first typing the name of the player.
Then the game will lunch the game boards and randomly populate 5 ships. 
The player will then be asked to enter coordinates to find out the AI ships and sink them.
The grid always starts on 0 rows and 0 columns. Guesses are marked on the board with an X
and hits are marked by *. To win the whole game, you will have to sink all the AI's ships before
it sinks yours!

## Features

### Existing Features

- __Start the Battle__

    - One board each is generated on the specified grid size
    - Ships are randomly placed on the player and the AI board
    - The player can see where his ships are located by a (@) mark
    - The player can not see where the AI ships are located on the board

![alt text](image/start-battle.jpg)


- __In game Guess__
    
    - Player input implemented
    - Viewing in-game score
    - View chosen guess

![alt text](image/in-game.jpg)


- __In game Validation__

    - Only numbers are verified as an input
    - The player can't guess the same coordinates twice
    - Coordinates outside the grid size are not allowed
    - The Data is maintained in class instances

![alt text](image/in-valid.jpg)



### Features Let to Implement
I'd like to implement:
- Allow players to position ships themselves
- Make rows with numbers and columns with letters

## Data Model

I have chosen the option to use two classes for the game model. One GameBoard class and the other Game class.

- __GameBoard Class__

    - self.size = To set the board size
    - self.name = To get the name of players
    - self.num_ships = To set number of ships in-game
    - self.player = Boolean indicate if the board belongs to a player or AI
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
    - Validate that Value Error is given to the player when the wrong value is entered
    - Write string, text instead of numbers when numbers are expected
    - Out of bounds inputs example out of grid number
    - The same guess cannot be performed more than once

- Local terminal and the Code institute Heroku terminal
    - Test is done on my local terminal in Gitpod
    - Test is done when the project was deployed on Heroku with the Code Institute mockup terminal


## Bugs

No known bugs


- Validator Testing
    - PEP 8
![alt text](image/pep.jpg)

## Languages, Frameworks, IDE, Librarires and Programs

[Python](https://en.wikipedia.org/wiki/History_of_Python)
- The programming language Python was used. 

[GitHub:](https://github.com/)
- GitHub was used to store the projects code after being pushed from Git.

[Gitpod:](https://www.gitpod.io/)
- Was used to complement the development and write my project and push all commits through integrated "git" to Github.

[Heroku:](https://www.heroku.com/what)
- Was used for deployment of the project live in the cloud.



## Deplyement

This project was published and deployed using the Code Institute mock terminal for Heroku

- Setps for deployment:
    - Fork or clone this repository
    - Create a new Heroku application
    - Set the buildpack to "Python" and "Node.js" in that order
    - Link the Heroku app to the repository
    - Choose either "Automatic deployment" or "Manual deploy"

The live link can be found here - https://battleship-war-kdg.herokuapp.com/


## Credits

- Code Institute project 3 Scope Video
- Stackoverflow

## Acknoledgments

- My mentor Guido Cecilio for his support and time
- Code Institute idea from the Project Portofiolo 3


Kevin.G
