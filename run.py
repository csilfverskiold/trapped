def game_intro():
    """
    Game introduction and opening scene requesting data input
    """
    print("-^-^-^- Trapped! -^-^-^-")
    print(">>> This placeholder text will introduce the player")
    print("to the game and let them start the game by requested")
    print("input data. <<<\n")

    while True:
        move_forward = input("Hit 1 and press ENTER to move forward: ")
        try:
            if int(move_forward) == 1:
                print("")
                print("Moving FORWARD")
                break
            else:
                print("Invalid number, hit 1 and ENTER")
        except ValueError:
            print("Value must be whole number, hit 1 and ENTER")


def validate_data():
    """
    Validates player data input
    """
    while True:
        choice = input("Enter choice: ")
        try:
            if int(choice) == 1:
                print("")
                print("Player chose option 1")
                break
            elif int(choice) == 2:
                print("")
                print("Player chose option 2")
                break
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
    print("1 - Choose this option")
    print("2 - Choose that option")
    print("")

    validate_data()


def trap_2():
    """
    DOCSTRING for TRAP 2
    """
    print("")
    print(">>> Placeholder text for TRAP 2 telling player about two")
    print("options to choose. <<<\n")
    print("1 - Choose this option")
    print("2 - Choose that option")
    print("")

    validate_data()


def trap_3():
    """
    DOCSTRING for TRAP 3
    """
    print("")
    print(">>> Placeholder text for TRAP 3 telling player about two")
    print("options to choose. <<<\n")
    print("1 - Choose this option")
    print("2 - Choose that option")
    print("")

    validate_data()


def trap_4():
    """
    DOCSTRING for TRAP 4
    """
    print("")
    print(">>> Placeholder text for TRAP 4 telling player about two")
    print("options to choose. <<<\n")
    print("1 - Choose this option")
    print("2 - Choose that option")
    print("")

    validate_data()


def trap_5():
    """
    DOCSTRING for TRAP 5
    """
    print("")
    print(">>> Placeholder text for TRAP 5 telling player about two")
    print("options to choose. <<<\n")
    print("1 - Choose this option")
    print("2 - Choose that option")
    print("")

    validate_data()


game_intro()
trap_1()
trap_2()
trap_3()
trap_4()
trap_5()


"""
- Write function that validates data in each trap -
- Write function that knows which options are CORRECT and INCORRECT -
- Write function that loops if player chooses CORRECT or INCORRECT -
- Write function with dictionary that collects other functions -
"""
