import os

def hand_choice():
    cmd = 'python3 morpion_2.py'
    cmd_hand = 'python3 morpion_1.py'

    print("\n JEU DU MORPION\n")

    input_hand_choice = input("Voulez vous prendre la main ? 'o' oui 'n' non : ")
    print('\n')
    if input_hand_choice == 'o':
        os.system(cmd_hand)
    else:
        os.system(cmd)

hand_choice()
