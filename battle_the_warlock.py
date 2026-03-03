"""
Battle the Warlock — Python Text Adventure (CLI)

Author: April Radcliff
Project Type: Portfolio Demonstration

Description:
A command-line text adventure game where the player must
collect magical items and defeat the Warlock.
"""

ROOMS = {
    "Great Hall": {"south": "Chamber", "north": "Library", "east": "Chapel", "west": "Garderobe"},
    "Chamber": {"north": "Great Hall", "east": "Larder", "item": "Wand"},
    "Larder": {"west": "Chamber", "item": "Potion"},
    "Garderobe": {"east": "Great Hall", "item": "Staff"},
    "Chapel": {"north": "Icehouse", "west": "Great Hall", "item": "Hat"},
    "Icehouse": {"south": "Chapel", "item": "Cloak"},
    "Library": {"south": "Great Hall", "east": "Gatehouse", "item": "Spellbook"},
    "Gatehouse": {"west": "Library"}
}

REQUIRED_ITEMS = {"Wand", "Potion", "Staff", "Hat", "Cloak", "Spellbook"}


def instructions():
    print("Welcome to Battle the Warlock — Text Adventure Game\n")
    print("Collect all six magical items before entering the Gatehouse.")
    print("Commands:")
    print(" - north, south, east, west (movement)")
    print(" - get <item>")
    print(" - exit\n")


def show_status(current_room, inventory):
    print("\n" + "-" * 50)
    print(f"Current Room: {current_room}")
    print("Inventory:", ", ".join(inventory) if inventory else "Empty")

    exits = [d for d in ROOMS[current_room] if d in {"north", "south", "east", "west"}]
    print("Exits:", ", ".join(exits))

    if "item" in ROOMS[current_room]:
        item = ROOMS[current_room]["item"]
        if item not in inventory:
            print(f"Item available: {item}")


def move(current_room, direction):
    if direction in ROOMS[current_room]:
        return ROOMS[current_room][direction]
    print("Invalid direction.")
    return current_room


def get_item(current_room, inventory, item_name):
    item_in_room = ROOMS[current_room].get("item")

    if not item_in_room:
        print("No item in this room.")
        return

    if item_name.lower() != item_in_room.lower():
        print("That item is not here.")
        return

    if item_in_room in inventory:
        print("Item already collected.")
        return

    inventory.append(item_in_room)
    print(f"{item_in_room} added to inventory.")


def main():
    current_room = "Great Hall"
    inventory = []

    instructions()

    while True:
        show_status(current_room, inventory)

        command = input("\nEnter command: ").strip().lower()

        if command == "exit":
            print("Game exited.")
            break

        elif command in {"north", "south", "east", "west"}:
            current_room = move(current_room, command)

        elif command.startswith("get "):
            item_name = command[4:]
            get_item(current_room, inventory, item_name)

        else:
            print("Invalid command.")

        if current_room == "Gatehouse":
            if set(inventory) == REQUIRED_ITEMS:
                print("\nYou defeated the Warlock. You WIN!")
            else:
                print("\nThe Warlock defeated you. Game Over.")
            break


if __name__ == "__main__":
    main()

# Minor formatting update
