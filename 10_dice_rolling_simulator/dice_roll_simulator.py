import random

dice_drawing = {
    1: (
        "-----",
        "|   |",
        "| o |",
        "|   |",
        "-----",
    ),
    2: (
        "-----",
        "|o  |",
        "|   |",
        "|  o|",
        "-----",
    ),
    3: (
        "-----",
        "|o  |",
        "| o |",
        "|  o|",
        "-----",
    ),
    4: (
        "-----",
        "|o o|",
        "|   |",
        "|o o|",
        "-----",
    ),
    5: (
        "-----",
        "|o o|",
        "| o |",
        "|o o|",
        "-----",
    ),
    6: (
        "-----",
        "|o o|",
        "|o o|",
        "|o o|",
        "-----",
    ),

}


def roll_dice():
    roll = input('Roll the dice? (Y/N): ')

    while roll.lower() == 'Y'.lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print(f'dice rolled: {dice1} and {dice2}')
        print('\n'.join(dice_drawing[dice1]))
        print('\n'.join(dice_drawing[dice2]))
        roll = input('Roll the dice? (Y/N): ')


roll_dice()
