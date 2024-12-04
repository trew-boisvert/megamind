## Thought Process
I put my original notes in notes.txt.  My approach, considering the timeline and previous obligations around the holiday weekend, was to get something functional quickly, then polish it up.  I didn't go full-out TDD, but I did think about my test cases beforehand and make some notes so that I could do some manual testing as I wrote the first version of the game.  I added in a couple of extras, which are the replay feature and the difficulty-level feature, then double-checked the project requirements to figure out where to put my attention next.  I created the install instructions, then refactored my solution to make it a bit more modular and readable, because the code was messy.  My general approach to solving problems is make it work and then make it beautiful.  I'd say it's cute at this point, but not beautiful yet.  

## Installation Instructions for Mac:
1. Install VS Code using these instructions: [Mac](https://code.visualstudio.com/docs/setup/mac) 
2. Press the Command key and the space bar to open Spotlight
3. Type `terminal` in the Spotlight Searchbox that appears, then click on the Terminal application
4. Next, install Homebrew using their instructions found [here](https://brew.sh/)
5. In the terminal, run the command `brew install python@3.9 git`
6. Install the virtualenv tool by running this command in the terminal:
    - `sudo -H pip3 install virtualenv`
7. Configure Git by running these commands in the terminal:
    - `git config --global user.name "YOUR_NAME"`
    - `git config --global user.email "YOUR_EMAIL"`
8. Configure Git to use VS Code as its default editor by running this command in the terminal:
    - `git config --global core.editor "code --wait"`
9. Create a directory on your computer for this repository by running these commands in the terminal
    - `mkdir megamind`
    - `cd megamind`
10. Clone this repository following the instructions found [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
11. Open the repo in VS Code, and use the terminal to run the following commands:
    - `virtualenv env`
    - `source env/bin/activate`
12. In the terminal, use this command to install the [requests](https://requests.readthedocs.io/en/latest/) library
    - `pip3 install -r requirements.txt`
13. Run the command `python3 mastermind.py` in the terminal to play the game
14. Snack break, you deserve it


## Installation Instructions for Windows:
1. Tell your boss you need a Mac for work
2. Follow the instructions for Mac, as seen above
3. I hear Windows computers make good gaming computers, use it for that from now on.  


## To Do:
- [x] Pseudocode game
- [x] Build command line version of game
- [x] Add extras
- [x] Add installation instructions
- [x] Refactor, make it nice

## Ideas for Technical Interview
- Set up basic webpage version of game
- Add win/loss tracking
- Hell mode, uses letters instead of numbers (Is this just wordle?)
- Cheat mode, endless guesses until you solve it
- Hint modes
- Display rules
- Allow player to quit whenever