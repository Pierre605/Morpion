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
                                                    \n\n''')

def hand_choice():
    cmd = 'python3 morpion_2.py'
    cmd_hand = 'python3 morpion_1.py'

    input_hand_choice = input("Voulez vous prendre la main ? 'o' oui 'n' non : ")
    print('\n')
    if input_hand_choice == 'o':
        os.system(cmd_hand)
    else:
        os.system(cmd)

hand_choice()
