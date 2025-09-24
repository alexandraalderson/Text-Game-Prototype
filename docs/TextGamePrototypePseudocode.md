#===========================================
#PROTOTYPE TEXT ADVENTURE GAME – EDEXCEL PSEUDOCODE
#===========================================

#--------------------------------------------------------------
# GLOBAL VARIABLE DECLARATIONS
# Each variable is declared separately so students see
# exactly what type of data each holds.
#--------------------------------------------------------------
# player’s health points
DECLARE userHealth : INTEGER      
# damage player has taken
DECLARE userDamage : INTEGER      
# TRUE while the game is running
DECLARE gameOn : BOOLEAN          
# last direction entered
DECLARE d : STRING                
# optional player name
DECLARE userName : STRING         
# stores latest menu choice
DECLARE choice : STRING           
# stores chosen weapon name
DECLARE weapon : STRING           
# list of collected items
DECLARE inventory : ARRAY OF STRING  
# example room item
DECLARE room1_item : STRING       

#===========================================
# START_GAME – initialises the game
#===========================================
PROCEDURE START_GAME()
BEGIN PROCEDURE
    # reset the game state
    SET inventory TO []
    SET userHealth TO 0
    SET userDamage TO 0
    SET gameOn TO TRUE
    SET userName TO ""

    # show introduction text
    SEND "Opening scene." TO DISPLAY

    # jump to the first decision point
    CALL DECISION_A()
END PROCEDURE


#===========================================
# DECISION_A – first main menu of the story
#===========================================
PROCEDURE DECISION_A()
BEGIN PROCEDURE
    # describe available choices
    SEND "Decision A explanation." TO DISPLAY
    SEND "Choice 1" TO DISPLAY
    SEND "Choice 2" TO DISPLAY
    SEND "Choice 3 to enter the room code" TO DISPLAY
    SEND "Choose q to quit." TO DISPLAY

    # get player input
    RECEIVE choice FROM (STRING) KEYBOARD

    # branch according to input
    IF choice = "1" THEN
        CALL BRANCH_A1()
    ELSE IF choice = "2" THEN
        CALL BRANCH_A2()
    ELSE IF choice = "3" THEN
        CALL BRANCH_A3_ROOM()
    ELSE IF choice = "q" THEN
        SEND "Thanks for playing! Goodbye." TO DISPLAY
        SET gameOn TO FALSE
        RETURN
    ELSE
        # re-ask if invalid input
        SEND "Please enter 1 or 2 or 3 or q." TO DISPLAY
        CALL DECISION_A()
    END IF
END PROCEDURE


#===========================================
# BRANCH_A1 – story path leading to Endings 1–4
#===========================================
PROCEDURE BRANCH_A1()
BEGIN PROCEDURE
    SEND "Branch A1 Explanation." TO DISPLAY
    CALL DECISION_A1()
END PROCEDURE

PROCEDURE DECISION_A1()
BEGIN PROCEDURE
    # second-level choice inside Branch A1
    SEND "Decision A1 explanation." TO DISPLAY
    SEND "Choice A1.B1 - Choose 1" TO DISPLAY
    SEND "Choice A1.B2 - Choose 2" TO DISPLAY
    RECEIVE choice FROM (STRING) KEYBOARD

    IF choice = "1" THEN
        CALL PATH_A1B1()
    ELSE IF choice = "2" THEN
        CALL PATH_A1B2()
    ELSE
        SEND "Please enter 1 or 2." TO DISPLAY
        CALL DECISION_A1()
    END IF
END PROCEDURE

PROCEDURE PATH_A1B1()
BEGIN PROCEDURE
    # continues Branch A1 down B1 path
    SEND "Path A1.B1 explanation." TO DISPLAY
    CALL DECISION_A1B1()
END PROCEDURE

PROCEDURE DECISION_A1B1()
BEGIN PROCEDURE
    # final choice for this path -> End1 or End2
    SEND "Choice A1.B1 end decision explanation." TO DISPLAY
    SEND "End1 - Choose 1" TO DISPLAY
    SEND "End2 - Choose 2" TO DISPLAY
    RECEIVE choice FROM (STRING) KEYBOARD

    IF choice = "1" THEN
        CALL END1()
    ELSE IF choice = "2" THEN
        CALL END2()
    ELSE
        SEND "Please enter 1 or 2." TO DISPLAY
        CALL DECISION_A1B1()
    END IF
END PROCEDURE

PROCEDURE PATH_A1B2()
BEGIN PROCEDURE
    # continues Branch A1 down B2 path
    SEND "Path A1.B2 explanation." TO DISPLAY
    CALL DECISION_A1B2()
END PROCEDURE

PROCEDURE DECISION_A1B2()
BEGIN PROCEDURE
    # final choice for this path -> End3 or End4
    SEND "A1.B2 end decision explanation." TO DISPLAY
    SEND "End3 - Choose 1" TO DISPLAY
    SEND "End4 - Choose 2" TO DISPLAY
    RECEIVE choice FROM (STRING) KEYBOARD

    IF choice = "1" THEN
        CALL END3()
    ELSE IF choice = "2" THEN
        CALL END4()
    ELSE
        SEND "Please enter 1 or 2." TO DISPLAY
        CALL DECISION_A1B2()
    END IF
END PROCEDURE


#===========================================
# BRANCH_A2 – story path leading to Endings 3,5,6
#===========================================
PROCEDURE BRANCH_A2()
BEGIN PROCEDURE
    SEND "Branch A2 explanation." TO DISPLAY
    CALL DECISION_A2()
END PROCEDURE

PROCEDURE DECISION_A2()
BEGIN PROCEDURE
    # second-level choice inside Branch A2
    SEND "Decision A2 explanation" TO DISPLAY
    SEND "End5 - Choose 1" TO DISPLAY
    SEND "A2.B3 - Choose 2" TO DISPLAY
    RECEIVE choice FROM (STRING) KEYBOARD

    IF choice = "1" THEN
        CALL END5()
    ELSE IF choice = "2" THEN
        CALL PATH_A2B3()
    ELSE
        SEND "Please enter 1 or 2." TO DISPLAY
        CALL DECISION_A2()
    END IF
END PROCEDURE

PROCEDURE PATH_A2B3()
BEGIN PROCEDURE
    # continues Branch A2 down B3 path
    SEND "A2.B3 Explanation." TO DISPLAY
    CALL DECISION_A2B3()
END PROCEDURE

PROCEDURE DECISION_A2B3()
BEGIN PROCEDURE
    # final choice for this path -> End3 or End6
    SEND "A2.B3 decision explanation." TO DISPLAY
    SEND "End3 - Choose 1" TO DISPLAY
    SEND "End6 - Choose 2" TO DISPLAY
    RECEIVE choice FROM (STRING) KEYBOARD

    IF choice = "1" THEN
        CALL END3()
    ELSE IF choice = "2" THEN
        CALL END6()
    ELSE
        SEND "Please enter 1 or 2." TO DISPLAY
        CALL DECISION_A2B3()
    END IF
END PROCEDURE


#===========================================
# BRANCH_A3_ROOM – optional exploration mini-game
# demonstrates loops and function calls with return values.
#===========================================
PROCEDURE BRANCH_A3_ROOM()
BEGIN PROCEDURE
    SEND "Room game loop description." TO DISPLAY
    SEND "Directions: n,e,s,w,u,d or b to return to story." TO DISPLAY

    # call function to get validated direction input
    SET d TO GET_DIRECTION()

    WHILE gameOn = TRUE
        # choose a room based on direction
        IF d = "north" THEN
            CALL ROOM1()
        ELSE IF d = "east" THEN
            CALL ROOM2()
        ELSE IF d = "south" THEN
            CALL ROOM3()
        ELSE IF d = "west" THEN
            CALL ROOM4()
        ELSE IF d = "down" THEN
            CALL ROOM5()
        ELSE IF d = "up" THEN
            CALL ROOM6()
        ELSE IF d = "backward" THEN
            CALL DECISION_A()
            IF gameOn = FALSE THEN
                RETURN
            END IF
        ELSE
            SEND "You can't go that way yet." TO DISPLAY
        END IF

        # check if player has ended the game
        IF gameOn = FALSE THEN
            EXIT WHILE
        ELSE
            SEND "Current inventory: " & inventory TO DISPLAY
            SET d TO GET_DIRECTION()
        END IF
    END WHILE
END PROCEDURE


#===========================================
# GET_DIRECTION – FUNCTION
# shows how to return a validated value from a function.
#===========================================
FUNCTION GET_DIRECTION() RETURNS STRING
BEGIN FUNCTION
    # use a Boolean flag for Edexcel-style REPEAT loop
    DECLARE validDirection : BOOLEAN
    SET validDirection TO FALSE
    DECLARE d : STRING

    REPEAT
        SEND "Direction: " TO DISPLAY
        RECEIVE d FROM (STRING) KEYBOARD

        # match input to valid directions or quit
        IF d = "north" THEN
            SET validDirection TO TRUE
            RETURN "north"
        ELSE IF d = "south" THEN
            SET validDirection TO TRUE
            RETURN "south"
        ELSE IF d = "east" THEN
            SET validDirection TO TRUE
            RETURN "east"
        ELSE IF d = "west" THEN
            SET validDirection TO TRUE
            RETURN "west"
        ELSE IF d = "up" THEN
            SET validDirection TO TRUE
            RETURN "up"
        ELSE IF d = "down" THEN
            SET validDirection TO TRUE
            RETURN "down"
        ELSE IF d = "left" THEN
            SET validDirection TO TRUE
            RETURN "left"
        ELSE IF d = "right" THEN
            SET validDirection TO TRUE
            RETURN "right"
        ELSE IF d = "forward" THEN
            SET validDirection TO TRUE
            RETURN "forward"
        ELSE IF d = "backward" THEN
            SET validDirection TO TRUE
            RETURN "backward"
        ELSE IF d = "quit" THEN
            SET validDirection TO TRUE
            RETURN "quit"
        ELSE
            # keep asking until a valid input is given
            SEND "Not a valid direction. Try again." TO DISPLAY
        END IF
    UNTIL validDirection = TRUE
END FUNCTION


#===========================================
# ENDING PROCEDURES
# each displays final stats and stops the game.
#===========================================
PROCEDURE END1()
BEGIN PROCEDURE
    SET gameOn TO FALSE
    SEND "SUCCESS! End 1." TO DISPLAY
    SEND "Health: " & userHealth TO DISPLAY
    SEND "Damage: " & userDamage TO DISPLAY
    SEND "Inventory: " & inventory TO DISPLAY
    SEND "Game Over." TO DISPLAY
    RECEIVE dummy FROM (STRING) KEYBOARD
END PROCEDURE

# (END2 … END6 follow same pattern with different messages)


#===========================================
# ROOM1 – example of a room procedure
# shows nested input validation and inventory updates.
#===========================================
PROCEDURE ROOM1()
BEGIN PROCEDURE
    SEND "Room 1 description." TO DISPLAY
    IF room1_item NOT IN inventory THEN
        SEND "Do you want to take " & room1_item & "? (y/n)" TO DISPLAY
        RECEIVE choice FROM (STRING) KEYBOARD
        IF choice = "y" THEN
            APPEND inventory, room1_item
            SEND "You pick up the " & room1_item TO DISPLAY
        ELSE
            SEND "You leave the " & room1_item TO DISPLAY
        END IF
    ELSE
        SEND "There's nothing else to take." TO DISPLAY
    END IF
    SEND "You head back to the Waiting Area." TO DISPLAY
END PROCEDURE


#===========================================
# PROGRAM ENTRY POINT
# execution begins here when the file runs directly.
#===========================================
CALL START_GAME()
