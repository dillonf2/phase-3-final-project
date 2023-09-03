# Pick a Number - CLI Game

**Pick a Number** is a simple CLI game designed for situations where a group needs to settle debates or make decisions by picking a number between 1 and 10. The winner is decided by whose guess is closest mathematically and recorded in the high scores (if their guess was good enough!). Unlike the classic "pick a number between 1 and 10" scenario, you can customize the range to your liking. This allows for both a larger maximum number and an unlimited number of participants. The winner's accuracy percentage is based on how close their guess is to the random number within the specified range.

## Features

- Start a new game and challenge participants to guess a random number within a specified range.
- Use the game as a tiebreaker or decision-making tool in group situations.
- View the top 10 leaderboard with the most accurate guesses.
- Record game statistics including participant names, guessed numbers, accuracy percentages, and more.
- Handle tiebreakers through a random selection process for equally accurate guesses.

## Getting Started

1. Clone this repository to your local machine.
2. Make sure you have Python 3.6+ installed.
3. Install the required dependencies using `pipenv install`.
4. Navigate into the lib directory.
5. Run the game using `pipenv run python cli.py`.

## How to Play

1. Run the game using the command mentioned above.
2. Press Enter to start a new game or enter any text followed by Enter to view the top 10 leaderboard.
3. Follow the on-screen instructions to set the game parameters and participant guesses.
4. The game will announce the winner based on guess accuracy, and in case of a tie, a random winner will be selected.

## Database

The game utilizes SQLAlchemy ORM to manage a SQLite database. It includes three related tables: `games`, `participants`, and `high_scores`.

## Feedback and Contributions

Feedback, suggestions, and contributions are welcome! If you encounter any issues or have ideas to improve the game, please create a new issue or pull request.

Enjoy the game and happy guessing!
