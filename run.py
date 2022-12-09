import time


def game_intro():
    """
    Game introduction and opening scene requesting data input
    """
    print("-^-^-^- Trapped! -^-^-^-")
    print(">>> This placeholder text will introduce the player")
    print("to the game and let them start the game by requested")
    print("input data. <<<\n")

    while True:
        move_forward = input("Press 1 and hit ENTER to move forward:\n")
        # Input data to start game
        try:
            if int(move_forward) == 1:
                print("")
                print("Moving FORWARD")
                trap_1()
            else:
                print("")
                print("Invalid number, hit 1 and ENTER")
                print("")
        except ValueError:
            print("")
            print("Value must be whole number, hit 1 and ENTER")
            print("")


def validate_data():
    """
    Validates player data input
    """
    while True:
        choice = input("Enter choice:\n")
        try:
            if int(choice) == 1:
                print("")
                print("Player chose option 1")
                return 1
            elif int(choice) == 2:
                print("")
                print("Player chose option 2")
                return 2
            else:
                print("")
                print("Invalid number, 1 or 2")
                print("")
        except ValueError:
            print("")
            print("Value must be a whole number, 1 or 2")
            print("")


def trap_1():
    """
    DOCSTRING for TRAP 1
    """
    print("")
    print(">>> Placeholder text for TRAP 1 telling player about two")
    print("options to choose. <<<\n")
    time.sleep(2)
    print("1 - Choose this option")
    print("2 - Choose that option")
    print("")

    choice = validate_data()

    if choice == 1:
        trap_2()
    else:
        print("")
        print("Oh no, wrong choice! You died, restarting game.")
        print("")
        game_intro()


def trap_2():
    """
    DOCSTRING for TRAP 2
    """
    print("")
    print(">>> Placeholder text for TRAP 2 telling player about two")
    print("options to choose. <<<\n")
    time.sleep(2)
    print("1 - Choose this option")
    print("2 - Choose that option")
    print("")

    choice = validate_data()

    if choice == 1:
        trap_3()
    else:
        print("")
        print("Oh no, wrong choice! You died, restarting game.")
        print("")
        game_intro()


def trap_3():
    """
    DOCSTRING for TRAP 3
    """
    print("")
    print(">>> Placeholder text for TRAP 3 telling player about two")
    print("options to choose. <<<\n")
    time.sleep(2)
    print("1 - Choose this option")
    print("2 - Choose that option")
    print("")

    choice = validate_data()

    if choice == 2:
        trap_4()
    else:
        print("")
        print("Oh no, wrong choice! You died, restarting game.")
        print("")
        game_intro()


def trap_4():
    """
    DOCSTRING for TRAP 4
    """
    print("")
    print(">>> Placeholder text for TRAP 4 telling player about two")
    print("options to choose. <<<\n")
    time.sleep(2)
    print("1 - Choose this option")
    print("2 - Choose that option")
    print("")

    choice = validate_data()

    if choice == 2:
        trap_5()
    else:
        print("")
        print("Oh no, wrong choice! You died, restarting game.")
        print("")
        game_intro()


def trap_5():
    """
    DOCSTRING for TRAP 5
    """
    print("")
    print(">>> Placeholder text for TRAP 5 telling player about two")
    print("options to choose. <<<\n")
    time.sleep(2)
    print("1 - Choose this option")
    print("2 - Choose that option")
    print("")

    choice = validate_data()

    if choice == 2:
        game_end()
    else:
        print("")
        print("Oh no, wrong choice! You died, restarting game.")
        print("")
        game_intro()


def game_end():
    """
    DOCSTRING for GAME_END
    """
    print("")
    print(">>> Placeholder text for GAME_END telling player they")
    print("escaped. <<<\n")
    time.sleep(2)
    print("1 - Choose this option")
    print("2 - Choose that option")
    print("")

    choice = validate_data()

    if choice == 1:
        game_intro()
    else:
        print("")
        print("Goodbye!")
        exit()


game_intro()
