import requests


def choose_difficulty():
    """
    Ask player to choose the difficulty level and then fetch the secret number from the API
    Returns a list containing the level and secret number as strings.
    """

    print("Which difficulty level would you like?  1 (easy) 2 (normal) 3 (hard)?")
    difficulty = input("1/2/3 --- ")

    difficulty_levels = {'1': 3, '2': 4, '3': 5}
    level = difficulty_levels.get(difficulty, 4)

    if difficulty not in difficulty_levels:
        print("Unexpected input, but we'll assume you mean normal mode")
        
    payload = {'num': level,
               'min': '0',
               'max': '7',
               'col': '1',
               'base': '10',
               'format': 'plain',
               'rnd': 'new'
               }
    
    api_request = requests.get('https://www.random.org/integers/', params=payload, timeout=5)
    api_request.raise_for_status()
    num_to_guess = api_request.text.replace("\n", "")

    return [level, num_to_guess]


def guess_validity(current_guess, level):
    """
    Check the validity of the player's current guess.
    Returns boolean value.  
    """

    if current_guess.isnumeric() is False:
        print()
        print("*** Guesses need to be numeric ***")
        print()
        return False
    
    if len(current_guess) != level:
        print()
        print(f"*** Guesses should be exactly {level} numbers ***")
        print()
        return False
    
    return True


def create_feedback(current_guess, num_to_guess, level):
    """
    Create feedback on the current guess compared to the secret number.
    Returns a string.
    """

    total_correct_loc = 0
    total_correct_num = 0

    for num in range(level):
        if current_guess[num] == num_to_guess[num]:
            total_correct_loc += 1
    copy_answer = list(num_to_guess)

    for char in current_guess:
        if char in copy_answer:
            copy_answer.remove(char)
            total_correct_num += 1
    if total_correct_num == 0:
        feedback = "All wrong"
    else:
        feedback = f"{total_correct_num} correct numbers and {total_correct_loc} correct location"
    return feedback


def game():
    """
    Runs one game of mastermind.
    """

    level, num_to_guess = choose_difficulty()
    num_guesses = 1
    history_guesses = []

    while num_guesses <= 10:
        print("--------------GUESS HISTORY----------------")
        for guess in history_guesses:
            print(guess)
        print("--------------------------------------------\n")
        print(f"Round {num_guesses} of 10\n")

        current_guess = input("What is your guess?")

        if guess_validity(current_guess, level) is False:
            continue

        if current_guess == num_to_guess:
            print("\n*** You win! ***")
            break
        feedback = create_feedback(current_guess, num_to_guess, level)
        history_guesses.append(f"Round {num_guesses} Guess: {current_guess} Feedback: {feedback}")
        num_guesses += 1

    print(f"The answer was {num_to_guess}")


def play():
    """
    Handles the game play and replay options.
    """

    print("Welcome!")

    while True:
        print("Would you like to play a game of mastermind?")
        play_game = input("y/n:   ")
        if play_game == "y":
            game()
        elif play_game == "n":
            print("Alright, enjoy your day!")
            break
        else:
            print("Sorry, that's not an option.  Please choose 'y' or 'n'.")


play()