energy = 5
inventory = []
current_location = "Beach"


# 1. Welcome the player
def welcome_player():
    name = input("Enter your name: ")

    print(f"\nWelcome, {name}!")
    print("You are stranded on a mysterious island.")
    print("Your mission is to restore the lighthouse.")


# 2. Display player energy
def player_energy():
    print(f"Your energy: {energy}")


# 3. Check whether the player can cross the bridge
def check_bridge():
    has_rope = "Rope" in inventory
    has_energy = energy > 0

    if current_location == "Old Bridge":

      if has_rope and has_energy:
        print("You can cross the bridge!")
        return True
      else:
        print("You cannot cross the bridge.")
        return False

    else:
        print("Bridge can't be crossed from your current location.")
        return False

# 4. Reduce player energy

def reduce_energy():
    global energy

    if energy > 0:
        energy -= 1
        print(f"Energy remaining: {energy}")

# 5. Check player energy
def check_energy():
    if energy <= 0:
        print("Game over!")
        return False

    return True


# 6. Explore the island
def explore():
    print("You are exploring the island!")
    reduce_energy()


# 7. Collect items
def collect_items(location):

    if location == "Beach" and "Rope" not in inventory:
        inventory.append("Rope")
        print("You collected a Rope!")

    if location == "Cave" and "Lantern" not in inventory:
        inventory.append("Lantern")
        print("You collected a Lantern!")


# 8. Move player between locations
def move_player(location):
    choice = input("Where do you want to go?: ").strip().title()

    if choice == "q":
        print("Goodbye!")
        return location

    if location == "Beach" and choice == "Jungle":
        location = "Jungle"

    elif location == "Jungle" and choice == "Cave":
        location = "Cave"

    elif location == "Cave" and choice == "Old Bridge":
        location = "Old Bridge"

    elif location == "Old Bridge" and choice == "Lighthouse":

        if check_bridge():
            location = "Lighthouse"

    else:
        print("You cannot move from here.")

    return location


# 9. Show current location
def show_location(location):
    print(f"Current location: {location}")


# 10. Main game menu
def loop_practice():
    global current_location

    while True:

        print("\n===== MYSTERY ISLAND =====")
        print("1. Explore")
        print("2. Check inventory")
        print("3. Move")
        print("4. Check bridge")
        print("q. Quit")

        choice = input("Enter your choice: ").strip()

        if choice == "q":
            print("Thanks for playing!")
            break

        elif choice == "1":
            explore()

            if not check_energy():
                break

        elif choice == "2":
            print("Your inventory:", inventory)

        elif choice == "3":
            current_location = move_player(current_location)

            collect_items(current_location)

            show_location(current_location)

            if current_location == "Lighthouse":
                print("\nCongratulations! You restored the lighthouse!")
                break

        elif choice == "4":
            check_bridge()

        else:
            print("Invalid choice.")


# =================================
# START THE GAME
# =================================

welcome_player()

player_energy()

collect_items(current_location)

loop_practice()

