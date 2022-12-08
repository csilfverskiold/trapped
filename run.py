def game_intro():
    """
    Game introduction and opening scene requesting data input
    """
    print("-^-^-^- Trapped! -^-^-^-")
    print(">>> This placeholder text will introduce the player")
    print("to the game and let them start the game by requested")
    print("input data. <<<\n")

    input("Hit 1 and press ENTER to move forward: ")

    while True:
        move_forward = input()
        try:
            if int(move_forward) == 1:
                print("")
                print("Moving FORWARD")
                break
            else:
                print("Invalid number, hit 1 and ENTER")
        except ValueError:
            print("Value must be whole number, hit 1 and ENTER")


game_intro()
