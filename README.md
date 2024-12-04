## Installation Instructions for Mac:
1. Install VS Code using these instructions: [Mac](https://code.visualstudio.com/docs/setup/mac) 
2. Press the Command key and the space bar to open Spotlight
3. Type 'terminal' in the Spotlight Searchbox that appears, then click on the Terminal application.
4. Next, install Homebrew using their instructions found [here](https://brew.sh/)
5. In the terminal, run the command `brew install python@3.9 git`
6. Install the virtualenv tool by running this command in the terminal:
    - `sudo -H pip3 install virtualenv`
7. Configure Git by running these commands in the terminal:
    - `git config --global user.name "YOUR_NAME"`
    - `git config --global user.email "YOUR_EMAIL"`
8. Configure Git to use VS Code as its default editor by running this command in the terminal:
    - `git config --global core.editor "code --wait"`
9. Create a directory on your computer to clone this repository into `mkdir megamind`
10. Clone this repository following the instructions found [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
11. Open the repo in VS Code, and use the terminal to run the following commands:
    - `virtualenv env`
    - `source env/bin/activate`
12. In the terminal, use this command to install the [requests](https://requests.readthedocs.io/en/latest/) library
    - `pip3 install -r requirements.txt`
13. Run the command `python3 mastermind.py` in the terminal to run the game
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
- [ ] Set up basic HTML
- [ ] Create server
- [ ] Web page version of game