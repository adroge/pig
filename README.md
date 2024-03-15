# The Game of Pig

## Software Requirements

- Python 3.12 or later

## Purpose

This is an example of expressive code, and the Principle of Single Responsibility. You should be able to look at the game loop at the bottom to understand what the code does.

- Expressive Code has descriptive variable names and functions to the extent that someone who doesn't know programming should be able to make some sense of it
- The Principle of Single Responsibility states that each function does **only one thing**
- Aside from the main loop, each function is under six lines, and therefore very small, and easy to understand
  - It's easier to debug and understand very small functions than it is a very large one

### Next Steps

Create an AI that would be player 2. You could modify the `want_to_roll_again()` function to detect whose turn it is, and if it's Player One's, let the player choose, but if it's Player Two's, have the AI choose. Following the same approach of descriptive function names, with no function being any longer than six lines.

- It's helpful to lower the `WINNING_SCORE` constant while testing how the game works.
- Sometimes it's easier to write the function just to get it working, and then refactor it into smaller well named functions.

The next step after adding AI would be to consider how to refactor into classes.

## Game Rules

The object of the game Pig is to be the first player to score 100 points. Each turn, a player repeatedly rolls a single die until either the player decides to hold (stop rolling) or a 1 is rolled. (Either end the turn.)

- If a 1 is rolled, the player scores nothing.
- If the player holds before a 1 is rolled,the player scores the turn total, the sum of the rolls of that turn.

Players take turns until one player wins by holding and reaching a score of 100 or more
points.

## Example

The first player, Jane, begins a turn with a roll of 5. Jane could hold and score 5 points, but chooses to roll again. Jane rolls a 2, and could hold with a turn total of 7 points, but chooses to roll again. Jane rolls a 1, and must end her turn without scoring. The next player, Richard, rolls the sequence 5-5-3-5-4, after which he chooses to hold, and adds his turn total of 22 points to his score.
