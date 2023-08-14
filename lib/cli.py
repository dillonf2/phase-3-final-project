#!/usr/bin/env python3

if __name__ == '__main__':
    input("Welcome to the Number Guessing Game! [Press Enter to Continue]")
    input("Try to guess a random number in the specified range. [Press Enter to Continue]")
    input("If you don't specify a range, the default range is 1-10. [Press Enter to Continue]")

    entries= []
    custom_range = input("Enter the maximum range for the random number (press Enter for default 10): ")
    max_range= int(custom_range) if custom_range else 10
    participant= input("Participant Name, Guess: ")
    while participant:
        entries.append(participant)
        participant= input("Participant Name, Guess: ")
    print(entries, max_range)
