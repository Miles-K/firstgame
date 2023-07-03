import Tts
import UserInput
import Difficulty
import RandomNum
import PlaySound

def gameQuestionStart():
    global GuessNum
    global GuessStr
    global RanNum
    global Msg
    GuessNum = Difficulty.getGuessNum()
    GuessStr = Difficulty.getGuessStr()
    RanNum = RandomNum.randomInt(GuessNum)
    # Msg = "I am thinking of a number between 1 and " + str(GuessNum) + ". Try to guess what it is."
    MsgTts = Msg
    # print(Msg)
    Tts.tts(MsgTts)

def gameQuestionAsk():
    Msg = "What number would you like to guess? "
    Tts.tts(Msg)

def gameQuestion(user_input: int):
    global Msg
    global Cont
    Cont = False
    # Msg = "What number would you like to guess? "
    # GameGUI.updateGuessLabel()
    # print(Msg)
    # Tts.tts(Msg)
    # user_input = int(UserInput.getUserInput())
    if user_input == RanNum:
        Msg = "Congradulations, you won!"
        # GameGUI.updateGuessLabel()
        Cont = True
    elif user_input < RanNum:
        Msg = "Darn, try again. The number is bigger than your last guess"
        # GameGUI.updateGuessLabel()
        # Cont = False
    else:
        Msg = "Darn, try again. The number is smaller than your last guess"
        # GameGUI.updateGuessLabel()
        # Cont = False
    # print(Msg)

# def sayMsg():
#     global Msg
#     Tts.tts(Msg)

def winCheck():
    Tts.tts(Msg)
    if Cont == True:
        # gameQuestion()
        PlaySound.winningSound()
    else:
        return Cont

def setMsg(message):
    global Msg
    Msg = message

def getMsg():
    return Msg
# def setGuessNum(num):
# def getGuessNum():
#     return GuessNum