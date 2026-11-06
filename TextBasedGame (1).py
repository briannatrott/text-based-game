# Curse of the Golden Beast text game

# A dictionary linking rooms to other rooms and items
rooms = {
    'Cozy Cabin': {'East': 'Moonlit Meadow'},
    'Moonlit Meadow': {
        'West': 'Cozy Cabin',
        'North': 'Whispering Woods',
        'East': 'Crystal Pond',
        'item': 'Squeaky Moon Amulet'},
    'Whispering Woods': {
        'South': 'Moonlit Meadow',
        'West': 'Forgotten Garden',
        'East': 'Ancient Shrine',
        'North': 'Echoing Cave',
        'item': 'Stick of Endless Fetch'},
    'Forgotten Garden': {
        'East': 'Whispering Woods',
        'item': 'Scroll of Belly Rubs'},
    'Crystal Pond': {
        'West': 'Moonlit Meadow',
        'item': 'Crystal Tennis Ball'},
    'Ancient Shrine': {
        'West': 'Whispering Woods',
        'North': 'Old Watchtower',
        'item': 'Enchanted Treat Bag'},
    'Old Watchtower': {
        'South': 'Ancient Shrine',
        'item': 'Golden Collar of Calm'},
    'Echoing Cave': {
        'South': 'Whispering Woods',
        'East': "Beast's Den",
        'bonus item': 'Perfume Brush'},
    "Beast's Den": {
        'West': 'Echoing Cave',
        'villain': 'Golden Beast'}
}


#Sample function showing the goal of the game and move commands
def show_instructions():
    print("Collect all 6 enchanted items before entering Beast's Den.")
    print("Move commands: type North, South, East, or West")
    print("Type 'get' to collect the item in the room.")
    print()

current_room = 'Cozy Cabin'
inventory = []

required_items = [
    'Squeaky Moon Amulet',
    'Stick of Endless Fetch',
    'Scroll of Belly Rubs',
    'Crystal Tennis Ball',
    'Enchanted Treat Bag',
    'Golden Collar of Calm',
]
# Show game instructions
print("Welcome to Curse of the Golden Beast text game!")

while True:
    start = input("Press Enter to start the game or type 'exit' to quit: ").strip().lower()

    if start == '':
        show_instructions()
        break
    elif start == 'exit':
        current_room = 'exit'
        print("Thanks for playing!")
        break

# Game loop
while current_room != 'exit':
    print()
    print("You are in the", current_room)
    print("Inventory:", inventory)

    if 'item' in rooms[current_room]:
        print("You see a", rooms[current_room]['item'])

    if 'bonus item' in rooms[current_room]:
        print("You see a", rooms[current_room]['bonus item'])
        print("This is a bonus item. It is not required, but it might help with the Beast's smell.")

    command = input("go>>").strip().lower()

    if command == 'exit':
        print("Thanks for playing!")
        current_room = 'exit'

    elif command in ['north', 'south', 'east', 'west']:
        direction = command.title()

        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]

            if current_room == "Beast's Den":
                if all(item in inventory for item in required_items):
                    if 'Perfume Brush' in inventory:
                        print(
                            "Congratulations! You collected all 6 enchanted items, broke the curse, and helped with the Beast's smell using the Perfume Brush!")
                    else:
                        print("Congratulations! You collected all 6 enchanted items and broke the Curse of the Golden Beast!")
                else:
                    print("UH OH!...GAME OVER! You entered Beast's Den without all 6 enchanted items.")

                current_room = 'exit'
        else:
            print("You can't go that way! Try again.")
    elif command == 'get':
        if 'item' in rooms[current_room]:
            inventory.append(rooms[current_room]['item'])
            print(rooms[current_room]['item'], "retrieved!")
            del rooms[current_room]['item']
        elif 'bonus item' in rooms[current_room]:
            inventory.append(rooms[current_room]['bonus item'])
            print(rooms[current_room]['bonus item'], "retrieved!")
            print("Bonus item collected! With this Perfume Brush and 6 enchanted items, the curse can be broken and the Golden Beast will smell much nicer.")
            del rooms[current_room]['bonus item']
        else:
            print("There is no item in this room.")
    else:
        print("Invalid command! Try again.")

input("Press Enter to close the game.")
