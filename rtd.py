import random
def rtd():
    dice_drawing = {
        1: "┍---------┑\n|         |\n|    O    |\n|         |\n┕---------┙\n",
        2: "┍---------┑\n|  O      |\n|         |\n|      O  |\n┕---------┙\n",
        3: "┍---------┑\n| O       |\n|    O    |\n|       O |\n┕---------┙\n",
        4: "┍---------┑\n| O     O |\n|         |\n| O     O |\n┕---------┙\n",
        5: "┍---------┑\n| O     O |\n|    O    |\n| O     O |\n┕---------┙\n",
        6: "┍---------┑\n| O     O |\n| O     O |\n| O     O |\n┕---------┙\n"
    }
    roll = int(input("How many dice would you like to roll? "))
    dice_list = []
    rolls = ""
    index = 0
    for x in range(roll):
        dice = random.randint(1,6)
        dice_list.append(dice)
        print(dice_drawing[dice])
    for i in dice_list:
        if index == len(dice_list) - 1:
            rolls += str(i)
        else:
            rolls = rolls + str(i) + ", "
        index += 1
    print("Your rolls:", rolls)
def rolling():
    play = input("Would you like to roll some dice? \n(y/n): ")
    while play.lower() == "y":
        rtd()
        play = input("\nRoll again?\n (y/n): ")

rolling()
