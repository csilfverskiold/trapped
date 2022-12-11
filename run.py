import time


def game_intro():
    """
    Game introduction and opening scene requesting data input.
    """
    print("")
    print("--^-^-^-^-^------^-^-^-^-^-- TRAPPED! --^-^-^-^-^------^-^-^-^-^--")
    print("")
    print("""
    ... The bearded man said the old tomb contained endless riches
    in a sea of gold, just waiting to be found. You, a hungry fortune seeker
    with nothing to lose but everything to gain, descend into the dark den.
    Under flickering torchlight you find the old mans words were true.\n
    Every. Single. Word.\n
    As you excitedly stuff your pockets and fill your hands with as
    much gold as you can carry, you notice how the walls suddenly begin to
    close in. What he didn't tell you was that the accursed crypt is actually
    nothing but a house of death and despair. Greed brought you here. And now
    it seems you're paying for it.\n
    Quick! Forget about your ill-gotten gains and make a run for the exit.
    But remember, watch out for the traps!\n
    """)

    while True:
        move_forward = input("Press 1 and hit ENTER to run:\n")
        # Input data to start game
        try:
            if int(move_forward) == 1:
                print("")
                print("You drop everything and begin to run.")
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
    Validates player data input.
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
    First scenario player encounters. Sets the scene.
    Based on input, player either advances to next scenario
    or game over and restart game.
    """
    print("")
    print("""
    You immediately stop as you find a bottomless pit has appeared
    in the corridor you previously came through. You notice a few spots you
    could carefully place your feet and hug the right side of the wall to
    pass. Risky but maybe. It's either that or swing across with the old rope
    hanging by its threads from the ceiling, just above the pit.\n
    """)
    time.sleep(1)
    print("1 - Swing with rope")
    print("2 - Hug the wall")
    print("")

    choice = validate_data()

    if choice == 1:
        trap_2()
    else:
        print("")
        print("""
        You carefully position yourself against the wall but the
        ledge immediately breaks off and you fall screaming forever.
        You died. Restarting game.
        """)
        print("")
        game_intro()


def trap_2():
    """
    Second scenario player encounters. Sets the scene.
    Based on input, player either advances to next scenario
    or game over and restart game.
    """
    print("")
    print("""
    You grab the rope, close your eyes and swing across. The rope
    snaps and you land on the other side of the pit.\n
    You continue running and from out of nowhere, a basket full of venomous
    scorpions falls down on you. You feel them crawling both outside and
    inside your clothes.\n
    """)
    time.sleep(1)
    print("1 - Remove them slowly one by one")
    print("2 - Try to swat, smash and remove them quickly")
    print("")

    choice = validate_data()

    if choice == 1:
        trap_3()
    else:
        print("")
        print("""
        You panic and try to remove the aggressively. The scorpions
        are enraged by this and sting you a thousand times over.
        You died. Restarting game.
        """)
        print("")
        game_intro()


def trap_3():
    """
    Third scenario player encounters. Sets the scene.
    Based on input, player either advances to next scenario
    or game over and restart game.
    """
    print("")
    print("""
    You slow down, whisper in a hushed voice and gently pick the
    scorpions off you one by one. You've done this before, haven't you?\n
    You hear the stone walls grind and crack behind you as they close in. You
    pick up the pace and keep running toward the exit. You can see the corridor
    makes a sharp turn up ahead. Suddenly, you hear a single clinking sound
    and feel you've stepped onto some sort of pressure plate. Your gut tells
    you something is about to happen and to act immediately.\n
    """)
    time.sleep(1)
    print("1 - Dodge forward")
    print("2 - Dodge to the side")
    print("")

    choice = validate_data()

    if choice == 2:
        trap_4()
    else:
        print("")
        print("""
        You dodge forward but catch eight arrows in your chest and
        face as they're are shot from the wall infront of you in the corridor
        turn. You died. Restarting game.
        """)
        print("")
        game_intro()


def trap_4():
    """
    Fourth scenario player encounters. Sets the scene.
    Based on input, player either advances to next scenario
    or game over and restart game.
    """
    print("")
    print("""
    You quickly dodge to the side and see a barrage of arrows shot at
    where you just stood. Close call.\n
    You follow the corridor as it turns. It opens up to a mostly empty room
    with the corridor continuing on the other side. Strange, you recognize the
    body of someone you know laying on the floor in the middle of the
    room.\n
    """)
    time.sleep(1)
    print("1 - Inspect the body")
    print("2 - Ignore the body, keep running")
    print("")

    choice = validate_data()

    if choice == 2:
        trap_5()
    else:
        print("")
        print("""
        You reach down to inspect the body and notice in the last
        second it's booby-trapped. The body explodes and you along with it.
        You died. Restarting game.
        """)
        print("")
        game_intro()


def trap_5():
    """
    Fifth scenario player encounters. Sets the scene.
    Based on input, player either advances to next scenario
    or game over and restart game.
    """
    print("")
    print("""
    No, it cannot be. That person is dead and buried since years ago.
    The stress of the situation is obviously clouding your judgement.
    No matter, the tomb is caving in and you need to get out.\n
    You press on and remember the exit being close. As you run the final
    stretch, you enter a section of the corridor with urns placed along the
    walls. The urns begin to crack, emanating an ominous glow followed by
    the wailing of a thousand lost souls. You hear a distorted, raspy voice
    whisper "You will never..."
    """)
    time.sleep(1)
    print('1 - "You will never" what? You must know before leaving the tomb!')
    print("2 - Don't care, leg it!")
    print("")

    choice = validate_data()

    if choice == 2:
        game_end()
    else:
        print("")
        print("""
        Like a madman, you call out to the ominous glow, demanding
        to know the rest of the whispers. Allowing your escape to halt for a
        moment too long, you hear the voice again "You will never...
        Leave this prison...". Your body falls limp to the floor as your soul
        rips from it and is dragged into the void.
        You died. Restarting game.
        """)
        print("")
        game_intro()


def game_end():
    """
    Game ending. Based on input, player either restarts or exits game.
    """
    print("")
    print("""
    Sweat dripping, lungs burning and heart pounding as you run for
    your life. You feel as something has a tight grip around you from the
    inside, pulling at your very soul, keeping you in this accursed den.
    But your will is stronger.\n
    With a loud crumbling crack, you burst of the exit as the tomb caves in
    on itself behind you. Despite emerging empty-handed, you escaped the tomb
    and live to die another day.
    Well done, fortune seeker.
    """)
    time.sleep(1)
    print("1 - Play again")
    print("2 - Exit game")
    print("")

    choice = validate_data()

    if choice == 1:
        game_intro()
    else:
        print("")
        print("Farewell, fortune seeker.")
        exit()


game_intro()
