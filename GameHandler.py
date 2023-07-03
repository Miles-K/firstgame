import Tts
import UserInput
import Difficulty
import RandomNum
import PlaySound

def game_question_start():
    global guess_num
    global guess_str
    global ran_num
    global msg
    guess_num = Difficulty.get_guess_num()
    guess_str = Difficulty.get_guess_str()
    ran_num = RandomNum.random_int(guess_num)
    # msg = "I am thinking of a number between 1 and " + str(guess_num) + ". Try to guess what it is."
    msg_tts = msg
    # print(msg)
    Tts.tts(msg_tts)

def game_question_ask():
    msg = "What number would you like to guess? "
    Tts.tts(msg)

def game_question(user_input: int):
    global msg
    global cont
    cont = False
    # msg = "What number would you like to guess? "
    # GameGUI.updateGuessLabel()
    # print(msg)
    # Tts.tts(msg)
    # user_input = int(UserInput.get_user_input())
    if user_input == ran_num:
        msg = "Congradulations, you won!"
        # GameGUI.updateGuessLabel()
        cont = True
    elif user_input < ran_num:
        msg = "Darn, try again. The number is bigger than your last guess"
        # GameGUI.updateGuessLabel()
        # cont = False
    else:
        msg = "Darn, try again. The number is smaller than your last guess"
        # GameGUI.updateGuessLabel()
        # cont = False
    # print(msg)

def win_check():
    Tts.tts(msg)
    if cont == True:
        # game_question()
        PlaySound.winning_sound()
    else:
        return cont

def setMsg(message):
    global msg
    msg = message

def getMsg():
    return msg
# def set_guess_num(num):
# def get_guess_num():
#     return guess_num