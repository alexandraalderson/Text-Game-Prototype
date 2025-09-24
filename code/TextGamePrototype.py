#Prototype Game Title

#Game Summary

#Variables

# ----------------------------
# Game State Variables
# ----------------------------
# userHealth and userDamage can go up or down.
# If you change these with = inside a function,
# add:   global userHealth, userDamage
# at the top of that function.
# inventory is a list of items. You can append/remove
# without adding global, but it's okay if you leave
# global inventory there.

#----------------------------
#DATA
#----------------------------
#Direction the user is going
d = ""
#Is the user still playing
gameOn = True
# --------------------------
# ROOM DATA
# --------------------------
waiting_area_name = "Waiting Area Name"
waiting_area_description = "Waiting Area description."
waiting_area_item = "Waiting Area item"

room1_name = "Room 1 Name"
room1_description = "Room 1 description."
room1_item = "Room 1 item - Key"

room2_name = "Room 2 Name"
room2_description = "Room 2 description."
room2_item = "Room 2 Item - Hard Puzzle Treasure"
room2_monster = "Room 2 Monster"

room3_name = "Room 3 name"
room3_description = "Room 3 description."
room3_item = "Room 3 Item 1 - Easy Puzzle Weapon"
room3_item2 = "Room 3 Item 2 - Locked Box"

room4_name = "Room 4 Name - Store"
room4_description = "Room 4 description."
room4_item = "Room 4 item - Purchasable"

room5_name = "Room 5 name"
room5_description = "Room 5 description."
room5_item = "Room 5 Item Weapon"

room6_name = "Room 6 Name"
room6_description = "Room 6 description."
room6_item = "Room 6 Item - Stun Weapon"

# --------------------------
# DIRECTION LISTS
# --------------------------
north = ["n","N","north","North"]
south = ["s","S","south","South"]
east  = ["e","E","east","East"]
west  = ["w","W","west","West"]
up = ["u","U","up","Up"]
down = ["d","D","down","Down"]
left = ["l","L","left","Left"]
right = ["r","R","right","Right"]
forward = ["f","F","forward","Forward"]
backward = ["b","B","backward","Backward"]
quit = ["q","Q","quit","Quit"]


def start_game():

    #User  features, they are global so multiple functions can change them
    global userHealth, userDamage, inventory, gameOn

    inventory = []
    userHealth = 0
    userDamage = 0
    gameOn = True

    #User's name
    userName = "" #Will you ask what their name is or give them one?

    #Opening scene explanation
    print("Opening scene.\n")

    # Decision A – player chooses 1 or 2
    decision_a()

def decision_a():
    #User  features, they are global so multiple functions can change them
    global userHealth, userDamage, inventory, gameOn

    #Decision A
    print("Decision A explanation.")
    print("Choice 1")
    print("Choice 2")
    print("Choice 3 to enter the room code")
    print("Choose q to quit.")
    choice = input("Choose 1 or 2 or 3 or q: ")

    #Choice A1
    if choice == "1":
        branch_a1()
    #Choice A2
    elif choice == "2":
        branch_a2()

    #Choice A3 - Room Code
    elif choice == "3":
        branch_a3_room()

    #Choice q to Quit
    elif choice == "q":
        print("Thanks for playing! Goodbye.")
        gameOn = False
        return  #return to quit the game

   #Invalid Entry
    else:
        print("Please enter 1 or 2 or 3 or q.")
        decision_a()  # ask again if input is invalid

def branch_a1():
    #User  features, they are global so multiple functions can change them
    global userHealth, userDamage, inventory

    #Branch A1 Explanation
    print("\nBranch A1 Explanation.")

    #Decision A1
    decision_a1()

def decision_a1():
    #User  features, they are global so multiple functions can change them
    global userHealth, userDamage, inventory

    #Decision A1
    print("Decision A1 explanation.")
    print("Choice A1.B1 - Choose 1")
    print("Choice A1.B2 - Choose 2")
    choice = input("Choose 1 or 2: ")

    #Choice A1.B1
    if choice == "1":
        path_a1b1()
    #Choice A1.B2
    elif choice == "2":
        path_a1b2()
    #Invalid entry
    else:
        print("Please enter 1 or 2.")
        decision_a1() # ask again if input is invalid

def path_a1b1():
    #User  features, they are global so multiple functions can change them
    global userHealth, userDamage, inventory

    #Path A1.B1
    print("\nPath A1.B1 explanation.")

    #Decision A1.B1
    decision_a1b1()

def decision_a1b1():
    #User  features, they are global so multiple functions can change them
    global userHealth, userDamage, inventory

    #Decision A1.B1
    print("Choice A1.B1 end decision explanation.")
    print("End1 - Choose 1")
    print("End2 - Choose 2")
    choice = input("Choose 1 or 2: ")

    #End1
    if choice == "1":
        end1()
    #End2
    elif choice == "2":
        end2()
    #Invalid Entry
    else:
        print("Please enter 1 or 2.")
        decision_a1b1() # ask again if input is invalid

def path_a1b2():
    #User  features, they are global so multiple functions can change them
    global userHealth, userDamage, inventory

    #Path A1.B2
    print("\nPath A1.B2 explanation.")

    #Decision A1.B2
    decision_a1b2()

def decision_a1b2():
    #User  features, they are global so multiple functions can change them
    global userHealth, userDamage, inventory

    #Decision A1.B2
    print("A1.B2 end decision explanation.")
    print("End3 - Choose 1")
    print("End4 - Choose 2")
    choice = input("Choose 1 or 2: ")

    #End3
    if choice == "1":
        end3()
    #End4
    elif choice == "2":
        end4()
    #Invalid Entry
    else:
        print("Please enter 1 or 2.")
        decision_a1b2() # ask again if input is invalid

def branch_a2():
    #User  features, they are global so multiple functions can change them
    global userHealth, userDamage, inventory

    #Branch A2 explanation
    print("\nBranch A2 explanation.")

    #Decision A2
    decision_a2()

def decision_a2():
    #User  features, they are global so multiple functions can change them
    global userHealth, userDamage, inventory

    #Decision A2 explanation
    print("Decision A2 explanation")
    print("End5 - Choose 1")
    print("A2.B3 - Choose 2")
    choice = input("Choose 1 or 2: ")

    #End5 Hide and Wait
    if choice == "1":
        end5()
    #A2.B3 Decoy
    elif choice == "2":
        path_a2b3()
    #Invalid Entry
    else:
        print("Please enter 1 or 2.")
        decision_a2() # ask again if input is invalid

def path_a2b3():
    #User  features, they are global so multiple functions can change them
    global userHealth, userDamage, inventory

    #A2.B3 Explanation
    print("\nA2.B3 Explanation.")

    #Decision A2.B3
    decision_a2b3()

def decision_a2b3():
    #User  features, they are global so multiple functions can change them
    global userHealth, userDamage, inventory

    #A2.B3 decision explanation
    print("A2.B3 decision explanation.")
    print("End3 - Choose 1")
    print("End6 - Choose 2")
    choice = input("Choose 1 or 2: ")

    #End3 Fight
    if choice == "1":
        end3()
    #End6 Surrender
    elif choice == "2":
        end6()
    #Invalid Entry
    else:
        print("Please enter 1 or 2.")
        decision_a2b3() # ask again if input is invalid

#A3 ROOM CODE
def branch_a3_room():
    #User  features, they are global so multiple functions can change them
    global userHealth, userDamage, inventory, gameOn

    # --------------------------
    # A3 ROOM GAME LOOP
    # --------------------------
    print("Room game loop description.")
    print(f"To the north is a {room1_name}.")
    print(f"To the east is a {room2_name}.")
    print(f"To the south is a {room3_name}.")
    print(f"To the west is an {room4_name}.")
    print(f"You can also see a {room5_name}...")
    print(f"Above you is {room6_name}.")
    print("Commands: enter a direction like n, e, s, w, d, or u.\nType b to return to the main story.")

    d = get_direction()

    while gameOn: #Loop while gameOn is True - they are still playing
        if d == "north":
            room1()
        elif d == "east":
            room2()
        elif d == "south":
            room3()
        elif d == "west":
            room4()
        elif d == "down":
            room5()
        elif d == "up":
            room6()
        elif d == "backward":
            decision_a() #Return to the main story
            if not gameOn: #They asked to quit in decision_a()
                return #ensures immediate stop
        else:
            print("You can't go that way yet.")

        if not gameOn: #They asked to quit
            break #exit while loop
        else:
            print("\nCurrent inventory:", inventory)
            d = get_direction()

#-------------------
#Endings Functions
#--------------------
def end1():
    #User  features, they are global so multiple functions can change them
    global userHealth, userDamage, inventory, gameOn

    gameOn = False #Game over

    #End1 – Success ending.
    print("\nSUCCESS!")
    print("End 1.")
    print(f"Your health was: {userHealth}.")
    print(f"Your damage was: {userDamage}.")
    print("Your inventory was:", inventory)
    print("Game Over.")
    input("\nPress Enter to exit.") #Pause to let them read before exit
    return #ensures immediate stop

def end2():
    #User  features, they are global so multiple functions can change them
    global userHealth, userDamage, inventory, gameOn

    gameOn = False #Game over

    #End2 – Failure: ???
    print("\nFAILURE.")
    print("End 2.")
    print(f"Your health was: {userHealth}.")
    print(f"Your damage was: {userDamage}.")
    print("Your inventory was:", inventory)
    print("Game Over.")
    input("\nPress Enter to exit.") #Pause to let them read before exit
    return #ensures immediate stop

def end3():
    #User  features, they are global so multiple functions can change them
    global userHealth, userDamage, inventory, gameOn

    gameOn = False #Game over

    #End3 – Failure: ???
    print("\nFAILURE.")
    print("End 3.")
    print(f"Your health was: {userHealth}.")
    print(f"Your damage was: {userDamage}.")
    print("Your inventory was:", inventory)
    print("Game Over.")
    input("\nPress Enter to exit.") #Pause to let them read before exit
    return #ensures immediate stop

def end4():
    #User  features, they are global so multiple functions can change them
    global userHealth, userDamage, inventory, gameOn

    gameOn = False #Game over

    #End4 – Failure: ???
    print("\nFAILURE.")
    print("End 4.")
    print(f"Your health was: {userHealth}.")
    print(f"Your damage was: {userDamage}.")
    print("Your inventory was:", inventory)
    print("Game Over.")
    input("\nPress Enter to exit.") #Pause to let them read before exit
    return #ensures immediate stop


def end5():
    #User  features, they are global so multiple functions can change them
    global userHealth, userDamage, inventory, gameOn

    gameOn = False #Game over

    #End5 – Failure: ???
    print("\nFAILURE.")
    print("End 5.")
    print(f"Your health was: {userHealth}.")
    print(f"Your damage was: {userDamage}.")
    print("Your inventory was:", inventory)
    print("Game Over.")
    input("\nPress Enter to exit.") #Pause to let them read before exit
    return #ensures immediate stop

def end6():
    #User  features, they are global so multiple functions can change them
    global userHealth, userDamage, inventory, gameOn

    gameOn = False #Game over

    #End6 – Failure: ???
    print("\nFAILURE.")
    print("End 6.")
    print(f"Your health was: {userHealth}.")
    print(f"Your damage was: {userDamage}.")
    print("Your inventory was:", inventory)
    print("Game Over.")
    input("\nPress Enter to exit.") #Pause to let them read before exit
    return    #ensures immediate stop

#Directions Function
def get_direction():
    while True:
        d = input("Direction: ")
        if d in north: return "north"
        if d in south: return "south"
        if d in east:  return "east"
        if d in west:  return "west"
        if d in up:    return "up"
        if d in down:  return "down"
        if d in left:  return "left"
        if d in right: return "right"
        if d in forward: return "forward"
        if d in backward: return "backward"
        if d in quit: return "quit"
        print("Not a valid direction. Try again.")

# --------------------------
# ROOM FUNCTIONS
# --------------------------
def room1():
    #User  features, they are global so multiple functions can change them
    global userHealth, userDamage, inventory

    print(f"\n{room1_name}")
    print(room1_description)
    if room1_item not in inventory:
        while True:
            choice = input(f"Do you want to take the {room1_item}? (y or n): ").lower()
            if choice == "y":
                inventory.append(room1_item)
                print(f"You pick up the {room1_item}.")
                break
            elif choice == "n":
                print(f"You leave the {room1_item} where it is.")
                break
            else:
                print("Please type y or n.")
        print("Your inventory is now:", inventory)
        print(f"You head back to the {waiting_area_name}.")
    else:
        print("There's nothing else to take here.")
        print(f"You head back to the {waiting_area_name}.")

def room2():
    #User  features, they are global so multiple functions can change them
    global userHealth, userDamage, inventory

    print(f"\n{room2_name}")
    print(room2_description)
    # check for any usable item
    if room3_item in inventory or room5_item in inventory or room6_item in inventory:
        weapon = (
            room6_item if room6_item in inventory
            else room3_item if room3_item in inventory
            else room5_item
        )
        # special spaceship message
        if weapon == room6_item:
            print(f"Congratulations, you kept yourself and the {room2_monster} calm with a {room6_item}. +1 health")
            userHealth = userHealth + 1
        else:
            print(f"Using a {weapon}, you defeat the {room2_monster}. Shame you didn't have a {room6_item}. -1 health +2 damage")
            userHealth = userHealth - 1
            userDamage = userDamage + 2
        if room2_item not in inventory:
            while True:
                choice = input(f"Do you want to take the {room2_item}? (y or n): ").lower()
                if choice == "y":
                    inventory.append(room2_item)
                    print(f"You pick up the {room2_item}.")
                    break
                elif choice == "n":
                    print(f"You leave the {room2_item} where it is.")
                    break
                else:
                    print("Please type y or n.")
            print("Your inventory is now:", inventory)
            print(f"You head back to the {waiting_area_name}.")
        else:
            print(f"There's no more {room2_monster} treasure.")
            print(f"You head back to the {waiting_area_name}.")
    else:
        print(f"You can't defeat the {room2_monster} unarmed.")
        print(f"You head back to the {waiting_area_name}.")

def room3():
    #User  features, they are global so multiple functions can change them
    global userHealth, userDamage, inventory

    print(f"\n{room3_name}")
    print(room3_description)
    if room1_item in inventory:
        print(f"Using the {room1_item}, you unlock the {room3_item2}.")
        if room3_item not in inventory:
            while True:
                choice = input(f"Do you want to take the {room3_item}? (y or n): ").lower()
                if choice == "y":
                    inventory.append(room3_item)
                    print(f"You pick up the {room3_item}.")
                    break
                elif choice == "n":
                    print(f"You leave the {room3_item} where it is.")
                    break
                else:
                    print("Please type y or n.")
            print("Your inventory is now:", inventory)
            print(f"You head back to the {waiting_area_name}.")
        else:
            print(f"There's nothing else to take in the {room3_item2}.")
            print(f"You head back to the {waiting_area_name}.")
    else:
        print("The chest is locked tight.")
        print(f"You head back to the {waiting_area_name}.")

def room4():
    #User  features, they are global so multiple functions can change them
    global userHealth, userDamage, inventory

    print(f"\n{room4_name}")
    print(room4_description)
    if room2_item in inventory:
        print(f"Using the {room2_item}, you have enough money to buy something.")
        if room4_item not in inventory:
            while True:
                choice = input(f"Do you want to buy the {room4_item}? (y or n): ").lower()
                if choice == "y":
                    inventory.append(room4_item)
                    print(f"You pick up the {room4_item}.")
                    break
                elif choice == "n":
                    print(f"You leave the {room4_item} where it is.")
                    break
                else:
                    print("Please type y or n.")
            print("Your inventory is now:", inventory)
            print(f"You head back to the {waiting_area_name}.")
        else:
            print("There's nothing else to buy of interest.")
            print(f"You head back to the {waiting_area_name}.")
    else:
        print("You can't go shopping without money.")
        print(f"You head back to the {waiting_area_name}.")

def room5():
    #User  features, they are global so multiple functions can change them
    global userHealth, userDamage, inventory

    print(f"\n{room5_name}")
    print(room5_description)
    if room5_item not in inventory:
        while True:
            choice = input(f"Do you want to take the {room5_item}? (y or n): ").lower()
            if choice == "y":
                inventory.append(room5_item)
                print(f"You pick up the {room5_item}.")
                print(f"You head back to the {waiting_area_name}.")
                break
            elif choice == "n":
                print(f"You leave the {room5_item} where it is. You feel sad.")
                print(f"You head back to the {waiting_area_name}.")
                break
            else:
                print("Please type y or n.")
        print("Your inventory is now:", inventory)
    else:
        print("There's nothing else to take here.")
        print(f"You head back to the {waiting_area_name}.")

def room6():
    #User  features, they are global so multiple functions can change them
    global userHealth, userDamage, inventory

    print(f"\n{room6_name}")
    print(room6_description)
    if room6_item not in inventory:
        while True:
            choice = input(f"Do you want to take the {room6_item}? (y or n): ").lower()
            if choice == "y":
                inventory.append(room6_item)
                print(f"You pick up the {room6_item}.")
                print(f"You head back to the {waiting_area_name}.")
                break
            elif choice == "n":
                print(f"You leave the {room6_item} where it is. You panic.")
                print(f"You head back to the {waiting_area_name}.")
                break
            else:
                print("Please type y or n.")
        print("Your inventory is now:", inventory)
    else:
        print("There's nothing else to take here.")
        print(f"You head back to the {waiting_area_name}.")

# Run the game if the file is executed directly.
if __name__ == "__main__":
    start_game()

# RUN THE GAME CELL ONCE BEFORE RUNNING THIS TEST CELL

# TESTS FOR ALL ENDINGS of the Prototype Game
# --------------------------------------------
# Each test feeds choices to reach a specific ending and includes an
# extra '' input to satisfy the final "Press Enter to exit." prompt.

import unittest
from unittest.mock import patch
from io import StringIO


# ========== TEST FOR ENDING 1 (SUCCESS) ==========
class TestPrototypeGame_End1(unittest.TestCase):
    def test_success_path(self):
        """
        Check that choosing A1 -> B1 -> 1 produces the SUCCESS! ending.
        """
        test_inputs = ['1', '1', '1', '']   # extra '' for final input()
        expected_text = "SUCCESS!"
        with patch('builtins.input', side_effect=test_inputs):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                start_game()
                output = fake_out.getvalue()
        print("\nEnd1 test path:", test_inputs)
        print("End1 captured output:\n", output)
        self.assertIn(expected_text, output)


# ========== TEST FOR ENDING 2 ==========
class TestPrototypeGame_End2(unittest.TestCase):
    def test_end2_path(self):
        """
        Check that choosing A1 -> B1 -> 2 produces the FAILURE ending (End2).
        """
        test_inputs = ['1', '1', '2', ''] # extra '' for final input()
        expected_text = "FAILURE."
        with patch('builtins.input', side_effect=test_inputs):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                start_game()
                output = fake_out.getvalue()
        print("\nEnd2 test path:", test_inputs)
        print("End2 captured output:\n", output)
        self.assertIn(expected_text, output)


# ========== TEST FOR ENDING 3 ==========
class TestPrototypeGame_End3(unittest.TestCase):
    def test_end3_path(self):
        """
        Check that choosing A1 -> B2 -> 1 produces the FAILURE ending (End3).
        """
        test_inputs = ['1', '2', '1', ''] # extra '' for final input()
        expected_text = "FAILURE."
        with patch('builtins.input', side_effect=test_inputs):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                start_game()
                output = fake_out.getvalue()
        print("\nEnd3 test path:", test_inputs)
        print("End3 captured output:\n", output)
        self.assertIn(expected_text, output)


# ========== TEST FOR ENDING 4 ==========
class TestPrototypeGame_End4(unittest.TestCase):
    def test_end4_path(self):
        """
        Check that choosing A1 -> B2 -> 2 produces the FAILURE ending (End4).
        """
        test_inputs = ['1', '2', '2', ''] # extra '' for final input()
        expected_text = "FAILURE."
        with patch('builtins.input', side_effect=test_inputs):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                start_game()
                output = fake_out.getvalue()
        print("\nEnd4 test path:", test_inputs)
        print("End4 captured output:\n", output)
        self.assertIn(expected_text, output)


# ========== TEST FOR ENDING 5 ==========
class TestPrototypeGame_End5(unittest.TestCase):
    def test_end5_path(self):
        """
        Check that choosing A2 -> 1 produces the FAILURE ending (End5).
        """
        test_inputs = ['2', '1', ''] # extra '' for final input()
        expected_text = "FAILURE."
        with patch('builtins.input', side_effect=test_inputs):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                start_game()
                output = fake_out.getvalue()
        print("\nEnd5 test path:", test_inputs)
        print("End5 captured output:\n", output)
        self.assertIn(expected_text, output)


# ========== TEST FOR ENDING 6 ==========
class TestPrototypeGame_End6(unittest.TestCase):
    def test_end6_path(self):
        """
        Check that choosing A2 -> 2 -> 2 produces the FAILURE ending (End6).
        """
        test_inputs = ['2', '2', '2', ''] # extra '' for final input()
        expected_text = "FAILURE."
        with patch('builtins.input', side_effect=test_inputs):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                start_game()
                output = fake_out.getvalue()
        print("\nEnd6 test path:", test_inputs)
        print("End6 captured output:\n", output)
        self.assertIn(expected_text, output)


# ----- Run all tests -----
unittest.main(argv=[''], exit=False)
