import tkinter as tk
import Tts
import UserInput

def selection_prompt():
    msg = "Select a Difficulty:"
    # print(msg)
    # print("1 = Easy")
    # print("2 = Moderate")
    # print("3 = Hard")
    Tts.tts(msg)

def set_guess_num(num):
    global guess_num
    guess_num = num

def get_guess_num():
    global guess_num
    return guess_num

def set_guess_str(str):
    global guess_str
    guess_str = str

def get_guess_str():
    global guess_str
    return guess_str

def difficulty_selector(difficulty):
    global guess_num
    difficulty_str = ""
    difficulty_mode = ""
    # selection_prompt()
    # difficulty = UserInput.get_user_input()
    # cont = True
    if difficulty == "1":
        set_guess_num(10)
        set_guess_str("ten")
        difficulty_str = "one"
        difficulty_mode = "easy mode"
    elif difficulty == "2":
        set_guess_num(50)
        set_guess_str("fifty")
        difficulty_str = "two"
        difficulty_mode = "moderate mode"
    elif difficulty == "3":
        set_guess_num(100)
        set_guess_str("one hundred")
        difficulty_str = "three"
        difficulty_mode = "hard mode"
    # else:
    #     cont = False
    #     # print("now false")
    
    # if cont == False:
    #     msg = "please select an appropriate difficulty"
    #     # print(msg)
    #     Tts.tts(msg)
    #     difficulty_selector()
    # else:
    msg = "difficulty level " + difficulty + " chosen"
    msg_tts = "difficulty level " + difficulty_str + " chosen"
    # print(msg)
    Tts.tts(msg_tts)
    msg = difficulty_mode
    # print(msg)
    Tts.tts(msg)
