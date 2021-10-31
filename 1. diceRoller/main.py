import random

def main():
    diceRoll1 = random.randint(1,9)
    diceRoll2 = random.randint(1,9)
    diceRoll3 = random.randint(1,9)
    diceRoll4 = random.randint(1,9)
    print("This week's winning lottery number is: ")
    print(f'{diceRoll1}{diceRoll2}{diceRoll3}{diceRoll4}') 

main()    