import Tts
import UserInput
import Difficulty
import RandomNum
import PlaySound

def game_question_start():
    global guess_num
    global guess_str
    global ranNum
    guess_num = Difficulty.get_guess_num()
    guess_str = Difficulty.get_guess_str()
    ranNum = RandomNum.random_int(guess_num)
    msg = "I am thinking of a number between 1 and " + str(guess_num) + ". Try to guess what it is."
    msg_tts = "I am thinking of a number between one and " + guess_str + ". Try to guess what it is."
    print(msg)
    Tts.tts(msg_tts)

def game_question():
    cont = True
    msg = "What number would you like to guess? "
    print(msg)
    Tts.tts(msg)
    user_input = int(UserInput.get_user_input())
    if user_input == ranNum:
        msg = "Congradulations, you won!"
    elif user_input < ranNum:
        msg = "Darn, try again. The number is bigger than your last guess"
        cont = False
    else:
        msg = "Darn, try again. The number is smaller than your last guess"
        cont = False
    print(msg)
    Tts.tts(msg)
    if cont == False:
        game_question()
    PlaySound.winning_sound()

# def set_guess_num(num):
# def get_guess_num():
#     return guess_num