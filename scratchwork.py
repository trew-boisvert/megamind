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

test cases (2025)
    all incorrect (1346)
    one correct, wrong location (0789)
    one correct, correct location (2469)
    guessed same correct number twice, should only say correct once (0790)
    guessed correct number there is 2 of, should say correct once (9287)
    three correct, two correct location (2092)
"""


        
