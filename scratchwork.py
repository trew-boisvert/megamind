"""
game start
4 digit number code gotten from API
on loop
    player can see history of guesses and feedback and remaining turns
    player guesses combo
        check if win, end game
            offer replay
        feedback on:
            if a number is correct or if number and digit is correct
            if whole guess was wrong
            add to guess counter
            ten guesses ends the game 
                offer replay
think about:
    don't make it recursive in the replays
    handling incorrect input (wrong chars, length)

test cases (2025)
    all incorrect (1346)
    one correct, wrong location (0789)
    one correct, correct location (2469)
    guessed same correct number twice, should only say correct once (0790)
    guessed correct number there is 2 of, should say correct once (9287)
    three correct, two correct location (2092)
    ten wrong guesses, game over
    ten guesses, last one all correct, game win
    win in under 10 guesses
"""
import requests

num_to_guess = requests.get('https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new').text.replace("\n", "")
print(num_to_guess)
print(type(num_to_guess))
def game():
    num_guesses = 1
    history_guesses = []
    while num_guesses <= 10:
        for guess in history_guesses:
            print(guess)
        print()
        print(f"Round {num_guesses} of 10")
        print()
        current_guess = input("What is your guess?")
        if current_guess == num_to_guess:
            print("You win!")
            break
        elif current_guess.isnumeric() == False:
            print("Guesses need to be numeric")
            continue
        elif len(current_guess) != 4:
            print("Guesses should be exactly four numbers")
        else:
            tally_correct_num_loc = 0
            tally_correct_num_no_loc = 0
            #check for correct number and location

            for num in range(4):
                if current_guess[num] == num_to_guess[num]:
                    #update counter
                    tally_correct_num_loc += 1  
            copy_answer = list(num_to_guess)
            print("copy answer", copy_answer)

            #check correct guess wrong location   
            for char in current_guess:
                if char in copy_answer:
                    copy_answer.remove(char)
                    #update counter
                    tally_correct_num_no_loc += 1
            #check for all wrong (if both counters empty)
            #give feedback
            if tally_correct_num_no_loc == 0:
                feedback = "All wrong"
            else:
                feedback = f"{tally_correct_num_no_loc} correct numbers and {tally_correct_num_loc} correct location"        
            #add feedback to history
            history_guesses.append(f"Round {num_guesses} Guess: {current_guess} Feedback: {feedback}")
            #add to num of guesses counter
            num_guesses += 1

game()