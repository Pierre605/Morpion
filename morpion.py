import os

print('''\n
   ___                  _        ___  ___     ______       _       _   _ 
  |_  |                | |       |  \/  |     | ___ \     (_)     | \ | |
    | | ___ _   _    __| |_   _  | .  . | ___ | |_/ /_ __  _  ___ |  \| |
    | |/ _ \ | | |  / _` | | | | | |\/| |/ _ \|    /| '_ \| |/ _ \| . ` |
/\__/ /  __/ |_| | | (_| | |_| | | |  | | (_) | |\ \| |_) | | (_) | |\  |
\____/ \___|\__,_|  \__,_|\__,_| \_|  |_/\___/\_| \_| .__/|_|\___/\_| \_/
                                                    | |                  
                                                    |_|
                                                                    \x1B[3mpar Pierre LUCIANI\x1B[0m
                                                    \n\n''')

def hand_choice():
    cmd = 'python3 morpion_2.py'
    cmd_hand = 'python3 morpion_1.py'

    input_hand_choice = input("Voulez vous prendre la main ? 'o' oui 'n' non : ")
    print('\n')
    while True:
        if input_hand_choice == 'o':
            return os.system(cmd_hand)
        elif input_hand_choice == 'n':
            return os.system(cmd)
        
        print("Erreur! ('o' oui, 'n' non)")
        input_hand_choice = input("Voulez vous prendre la main ? 'o' oui 'n' non : ")

hand_choice()
