# Curse of the Golden Beast

A text-based adventure game I wrote in Python while learning scripting.

## The story
A Golden Beast is under a curse. Explore 9 locations, from the Cozy Cabin to the Echoing Cave, and collect all 6 enchanted items before you enter the Beast's Den. Make it in with every item and you break the curse. Go in without them and it's game over.

There's also a hidden bonus item. It isn't required, but it helps with the Beast's smell.

## How to play
- Move: type `North`, `South`, `East`, or `West`
- Pick up an item: type `get`
- Quit: type `exit` (works at the start prompt or during the game)

## How to run it
1. Install [Python 3](https://www.python.org/downloads/)
2. Download `TextBasedGame.py` from this repository
3. Open a terminal in that folder and run:

```
python TextBasedGame.py
```

## What I practiced
- Dictionaries to build a map of connected rooms
- `while` loops for the main game loop
- `if` / `elif` / `else` logic for commands and win/lose conditions
- Lists to track the player's inventory
- Input cleanup with `.strip()`, `.lower()`, and `.title()`
