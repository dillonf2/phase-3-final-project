#!/usr/bin/env python3
import random
from db.models import Game, Participant, HighScore, Session

def calculate_accuracy(guess, number_to_guess, max_range):
    return (1 - abs(guess - number_to_guess) / (max_range-1)) * 100

def display_high_scores(high_scores):
    print("High Scores:")
    sorted_high_scores = sorted(high_scores, key=lambda hs: (hs.guess_accuracy, hs.max_range), reverse=True)
    for rank, high_score in enumerate(sorted_high_scores, start=1):
        print(f"{rank}. Participant: {high_score.participant}")
        print(f"   Range: 1-{high_score.max_range}")
        print(f"   Number to Guess: {high_score.number_to_guess}")
        print(f"   {high_score.participant}'s Guess: {high_score.guess}")
        print(f"   Guess Accuracy: {high_score.guess_accuracy:.2f}%")
        print()

if __name__ == '__main__':
    session= Session()
    
    input_value = input("Press Enter to Start a New Game... To view the Top 10 Guess Leaderboard, Enter Any Text and Then Press Enter.")

    if input_value:
        high_scores = session.query(HighScore).order_by(HighScore.guess_accuracy.desc()).limit(10).all()
        if high_scores:
            display_high_scores(high_scores)
        else:
            print("No games have been played yet.")
    else: 
        input("Welcome to Pick a Number! [Press Enter to Continue]")
        input("Try to guess a random number in the specified range. [Press Enter to Continue]")
        input("If you don't specify a range, the default range is 1-10. [Press Enter to Continue]")

        entries= []
        custom_range = input("Enter the maximum range for the random number (press Enter for default 10): ")
        max_range= int(custom_range) if custom_range else 10
        number_to_guess= random.randint(1, max_range)

        input(f"Time to Guess a Number Between 1-{max_range}! [Press Enter to Continue]")

        while True:
            participant = input("Participant Name (or press Enter to finish): ")
            if not participant:
                if not entries:
                    print("Cannot start game without participants.")
                else:
                    break
    
            while True:
                guess_input = input(f"{participant}, guess a number between 1-{max_range}: ")
        
                try:
                    guess = int(guess_input)
                    if 1 <= guess <= max_range:
                        break
                    else:
                        print(f"Guess must be between 1 and {max_range}.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
    
            entries.append((participant, guess))

        entry_text = "\n".join([f"{participant}: {guess}" for participant, guess in entries])
        input(f'Good Luck Everyone! Here are the participants and their guesses:\n{entry_text}\n[Press Enter to Continue]')
        input(f'And the random number was.... {number_to_guess}!!')

        winner, winning_guess = max(entries, key=lambda entry: calculate_accuracy(entry[1], number_to_guess, max_range))
        winning_accuracy = calculate_accuracy(winning_guess, number_to_guess, max_range)

        winners = [entry for entry in entries if calculate_accuracy(entry[1], number_to_guess, max_range) == calculate_accuracy(winning_guess, number_to_guess, max_range)]

        if len(winners) == 1:
            winner, winning_guess = winners[0]
            winning_accuracy = calculate_accuracy(winning_guess, number_to_guess, max_range)
            input(f'So the winner is...{winner}, with a guess accuracy of {winning_accuracy:.2f}%! Congratulations {winner}!')
        else:
            random_winner = random.choice(winners)
            input(f'There is a tie! A random winner will be selected from the tied participants.')
            input(f'And the random tiebreaker winner is.... {random_winner[0]}!! Congratulations {random_winner[0]}!')

        game = Game(
            max_range=max_range,
            number_to_guess=number_to_guess,
            winner=winner,
            winning_percentage=winning_accuracy
        )

        session.add(game)

        for participant, guess in entries:
            participant_instance = Participant(name=participant, guess=guess)
            game.participants.append(participant_instance)

        high_score = HighScore(
            participant=winner,
            max_range=max_range,
            number_to_guess=number_to_guess,
            guess=winning_guess,
            guess_accuracy=winning_accuracy
        )
        
        game.high_scores.append(high_score)

        session.add(high_score)
        session.commit()

        print("Game Over! High scores have been recorded.")
