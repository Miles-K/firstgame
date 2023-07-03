import tkinter as tk
import Tts
import UserInput

def selectionPrompt():
    msg = "Select a Difficulty:"
    # print(msg)
    # print("1 = Easy")
    # print("2 = Moderate")
    # print("3 = Hard")
    Tts.tts(msg)

def setGuessNum(num):
    global GuessNum
    GuessNum = num

def getGuessNum():
    global GuessNum
    return GuessNum

def setGuessStr(str):
    global GuessStr
    GuessStr = str

def getGuessStr():
    global GuessStr
    return GuessStr

def difficultySelector(difficulty):
    global GuessNum
    DifficultyStr = ""
    DifficultyMode = ""
    # selectionPrompt()
    # difficulty = UserInput.getUserInput()
    # cont = True
    if difficulty == "1":
        setGuessNum(10)
        setGuessStr("ten")
        DifficultyStr = "one"
        DifficultyMode = "easy mode"
    elif difficulty == "2":
        setGuessNum(50)
        setGuessStr("fifty")
        DifficultyStr = "two"
        DifficultyMode = "moderate mode"
    elif difficulty == "3":
        setGuessNum(100)
        setGuessStr("one hundred")
        DifficultyStr = "three"
        DifficultyMode = "hard mode"
    # else:
    #     cont = False
    #     # print("now false")
    
    # if cont == False:
    #     msg = "please select an appropriate difficulty"
    #     # print(msg)
    #     Tts.tts(msg)
    #     difficultySelector()
    # else:
    msg = "difficulty level " + difficulty + " chosen"
    msg_tts = "difficulty level " + DifficultyStr + " chosen"
    # print(msg)
    Tts.tts(msg_tts)
    msg = DifficultyMode
    # print(msg)
    Tts.tts(msg)
