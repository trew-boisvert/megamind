import requests


def choose_difficulty():
    print("Which difficulty level would you like?  1 (easy) 2 (normal) 3 (hard)?")
    difficulty = input("1/2/3 --- ")

    if difficulty == '1':
        level = '3'
    elif difficulty == '2':
        level = '4'
    elif difficulty == '3':
        level = '5'
    else:
        print("Unexpected input, but we'll assume you mean normal mode")
        level = '4'

    payload = {'num': level,
               'min': '0',
               'max': '7',
               'col': '1',
               'base': '10',
               'format': 'plain',
               'rnd': 'new'
               }

    api_request = requests.get('https://www.random.org/integers/', params=payload)
    num_to_guess = api_request.text.replace("\n", "")
    return [level, num_to_guess]


def game():
    level_and_num_to_guess = choose_difficulty()
    level = int(level_and_num_to_guess[0])
    num_to_guess = level_and_num_to_guess[1]
    num_guesses = 1
    history_guesses = []

    while num_guesses <= 10:
        print("--------------GUESS HISTORY----------------")
        for guess in history_guesses:
            print(guess)
        print("--------------------------------------------")
        print()
        print(f"Round {num_guesses} of 10")
        print()
        current_guess = input("What is your guess?")
        if current_guess == num_to_guess:
            print()
            print("*** You win! ***")
            break
        elif current_guess.isnumeric() is False:
            print()
            print("*** Guesses need to be numeric ***")
            print()
            continue
        elif len(current_guess) != level:
            print()
            print(f"*** Guesses should be exactly {level} numbers ***")
            print()
        else:
            tally_correct_num_loc = 0
            tally_correct_num_no_loc = 0

            for num in range(level):
                if current_guess[num] == num_to_guess[num]:
                    tally_correct_num_loc += 1
            copy_answer = list(num_to_guess)

            for char in current_guess:
                if char in copy_answer:
                    copy_answer.remove(char)
                    tally_correct_num_no_loc += 1
            if tally_correct_num_no_loc == 0:
                feedback = "All wrong"
            else:
                feedback = f"{tally_correct_num_no_loc} correct numbers and {tally_correct_num_loc} correct location"
            history_guesses.append(f"Round {num_guesses} Guess: {current_guess} Feedback: {feedback}")
            num_guesses += 1
    print(f"The answer was {num_to_guess}")


def play():
    print("Welcome!")
    while True:
        print("Would you like to play a game of mastermind?")
        play_game = input("y/n:   ")
        if play_game == "y":
            game()
        else:
            print("Alright, enjoy your day!")
            break


play()