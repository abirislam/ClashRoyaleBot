import pyautogui
import os
import random
import time

def checkForBattleIcon():
    battleTag = pyautogui.locateOnScreen('icons/battleicon.png', confidence=0.8)
    homeTag = pyautogui.locateOnScreen('icons/homeicon.png', confidence=0.8)

    if battleTag != None:
        pyautogui.click(battleTag)
    else:
        pyautogui.click(homeTag)
    
def loadAllCards():
    activeCardList = []

    # set build here
    cards = ["minipekka", "hogrider", "bomber", "speargoblins", "archers", "prince", "babydragon", "goblins"]

    for filename in os.listdir('./cards'):
        baseString = './cards/' + filename
        if filename[:-4] in cards:
            currentCard = pyautogui.locateOnScreen(baseString, confidence=0.8, region =(110, 850, 560, 990))
            activeCardList.append(currentCard)

    return activeCardList

def useCard(card):
    pyautogui.click(card)
    time.sleep(0.25)

    # left box
    x = random.randint(80, 220)
    y = random.randint(483, 593)

    # right box
    a = random.randint(380, 470)
    b = random.randint(485, 575)

    # choose left or right box
    choice = random.randint(0,1)
    if choice == 0:
        pyautogui.click(x, y)
    else:
        pyautogui.click(a, b)


def battle():
    inBattle = True
    okayTag = pyautogui.locateOnScreen('icons/okayicon.png', confidence=0.8)
    elixirTag = pyautogui.locateOnScreen('icons/elixiricon.png', confidence=0.8, region=(110, 980, 165, 1030))

    while inBattle:
        if elixirTag != None:
            listOfCards = loadAllCards()
            for card in listOfCards:
                if card != None:
                    useCard(card)
                    print("Using a card")
                    time.sleep(1)
        else:
            inBattle = False
    
    if okayTag != None:
        pyautogui.click(okayTag)
        print("Found the exit button")

def main():

    while True:

        checkForBattleIcon()

        battle()
        print("Battle ending")
        time.sleep(5)

if __name__ == "__main__":
    main()
