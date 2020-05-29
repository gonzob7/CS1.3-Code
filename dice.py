import random

def main():
    d1 = rollDie()
    d2 = rollDie()
    d3 = rollDie()
    d4 = rollDie()
    d5 = rollDie()
    print("Full House?: ", isFullHouse(d1,d2,d3,d4,d5))
    print("Yahtzee?: ", isYahtzee(d1,d2,d3,d4,d5))
    print("")

def rollDie():
    roll = random.randint(1,6)
    return roll

def isFullHouse(d1,d2,d3,d4,d5):
    allDie = [d1,d2,d3,d4,d5]
    allDieString = ""

    for die in allDie:
        allDieString += str(die)
        allDieString += " "

    print("You rolled: ", allDieString)
    allDie.sort()


    if allDie[0] == allDie[1] == allDie[2] and allDie[3] == allDie[4] or allDie[0] == allDie[1] and allDie[2] == allDie[3] == allDie[4]:
        return True
    else:
        return False

def isYahtzee(d1,d2,d3,d4,d5):
    allDie = [d1,d2,d3,d4,d5]
    allDie.sort()


    if allDie[0] == allDie[1] == allDie[2] == allDie[3] == allDie[4]:
        return True
    else:
        return False

if __name__ == '__main__':
    main()
    main()
    main()
