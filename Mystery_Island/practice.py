# def player_energy():
#     energy = 5
#     print(energy)

# player_energy()

# def check_bridge():
#     has_rope = True
#     has_energy = False

#     if has_rope and has_energy:
#         print("You can cross")
#     else:
#         print("You cannot cross")

# check_bridge()

# def loop_practice():
#     running = True

#     while True:
#         print("1. explore: ")
#         print("2. check inventory: ")
#         print("q. quit: ")

#         choice = input("Enter your choice: ")

#         if choice == "q":
#             print("Good bye 👋")
#             break

#         elif choice == "1":
#             print("You are exploring the island!: ")
#         elif choice == "2":
#             print("Your inventory is empty: ")
#         else:
#             print("Invalid choice")

# loop_practice()

# def welcome_player():
#     name = input("Player enter your name: ")
#     print(f"Welcome {name}")
#     print("You are stranded on a mysterious island.")
#     print("Your mission is to restore the lighthouse.")

# welcome_player()

# def reduce_energy():
#     energy = 5
#     for count in range(3):
#         energy = energy -1
#         print(energy)

# def check_energy():
#     energy = 3
#     if energy == 0:
#         print("Game over")
#     else:
#         print("You are still alive!")

# check_energy()


# def explore():
#     energy = 1
#     energy = energy -1
#     if energy == 0:
#         print("Game over")
#     else:
#         print("you are still alive!")

# explore()

# def move_player():
#     location = "Cave"
#     choice = input("Where do you want to go?: ")

#     if location == "Beach" and  choice == "Jungle":
#         location = "Jungle"
#     elif location == "Jungle" and choice == "Cave":
#         location = "Cave"
#     elif  location == "Cave" and choice == "Old Bridge":
#         location = "Old Bridge"
#     elif location == "Old Bridge" and choice == "Lighthouse":
#         location = "Lighthouse"
#     else:
#         print("You cannot move from here.")

#     print(location)

# move_player()

def show_location(location):
    print(location)
show_location("Jungle")