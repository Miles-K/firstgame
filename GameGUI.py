import tkinter as tk
import Difficulty
import GameHandler
import Tts

def run():
    Tts.voice_selection(0)
    defineWindow()
    createPlayButton()
    spawnWindow()
    

def defineWindow():
    global GameWindow
    global GWwidth
    global GWheight
    GWwidth = 1000
    GWheight = 800
    GameWindow = tk.Tk()
    GameWindow.title("First Game")
    GameWindow.geometry("1000x800")

def spawnWindow():
    GameWindow.mainloop()

def closeWindow(event):
    GameWindow.destroy()

def createPlayButton():
    global PlayBtn
    global PBwidth
    global PBheight
    PBwidth=10
    PBheight=5
    PlayBtn = tk.Button(
        GameWindow, justify="center", text="play",
        width=str(PBwidth), height=str(PBheight)
    )
    PlayBtn.bind("<Button-1>", (screen2))
    PlayBtn.place(
                  x=((GWwidth / 2) - (PBwidth / 2) - 21),
                  y=((GWheight / 2) - (PBheight / 2) - 80)
    )

def defineDifficultyFrame():
    global DFwidth
    global DFheight
    DFwidth = 400
    DFheight = 50
    global DifficultyFrame
    DifficultyFrame = tk.Frame(
        GameWindow, width=str(DFwidth), height=str(DFheight),
        border="1", bg="light green"
    )
    DifficultyFrame.rowconfigure(0, weight=1)

def spawnDifficultyFrame():
    DifficultyFrame.place(
                          x=((GWwidth / 2) - (DFwidth / 2)),
                          y=((GWheight / 2) - (DFheight / 2) - 65)
    )

def createDifficultyButtons():
    global EasyBtn
    global ModerateBtn
    global HardBtn
    BTNwidth = 12
    BTNheight = 4
    EasyBtn = tk.Button(
        DifficultyFrame, text="Easy", font="16",
        width=str(BTNwidth), height=str(BTNheight), bg="brown",
        fg="light green")
    EasyBtn.bind("<Button-1>", difficultySelectionEasy)
    EasyBtn.grid(row=0, column=0, sticky="news")
    ModerateBtn = tk.Button(
        DifficultyFrame, text="Moderate", font="16",
        width=str(BTNwidth), height=str(BTNheight), bg="brown",
        fg="yellow")
    ModerateBtn.bind("<Button-1>", difficultySelectionModerate)
    ModerateBtn.grid(row=0, column=1, sticky="news")
    HardBtn = tk.Button(
        DifficultyFrame, text="Hard", font="16",
        width=str(BTNwidth), height=str(BTNheight), bg="brown",
        fg="pink")
    HardBtn.bind("<Button-1>", difficultySelectionHard)
    HardBtn.grid(row=0, column=2, sticky="news")
    
def createGuessLabel():
    global GLtxt
    global GuessLabel
    GLwidth = 100
    GLtxt = GameHandler.getMsg()
    GuessLabel = tk.Label(
        GameWindow, text=str(GLtxt), justify="center", width=str(GLwidth)
    )
    GuessLabel.place(
                     x=((GWwidth / 2) - (GLwidth * 3.5) + 10),
                     y=((GWheight / 2) - 50)
    )

def updateGuessLabel():
    global GLtxt
    global GuessLabel
    GLtxt = GameHandler.getMsg()
    GuessLabel.update()

def createGuessEntry():
    GEwidth = 16
    global GuessEntry
    GuessEntry = tk.Entry(
        GameWindow, textvariable="[Answer Here]",
        borderwidth="2", justify="center", width=str(GEwidth)
    )
    GuessEntry.bind("<Return>", entryPassed)
    GuessEntry.place(
                     x=((GWwidth / 2) - (GEwidth * 2)),
                     y=((GWheight / 2) - 31)
    )



def screen2(event):
    PlayBtn.destroy()
    defineDifficultyFrame()
    createDifficultyButtons()
    spawnDifficultyFrame()
    GameWindow.update()
    Difficulty.selection_prompt()

def screen3o1():
    global first
    first = True
    clearDifficultyButtons()
    GameHandler.setMsg("I am thinking of a number between one and " + Difficulty.get_guess_str() + ". Try to guess what it is.")
    createGuessLabel()
    GameWindow.update()


def screen3o2():
    global first
    GameHandler.game_question_start()
    if first == True:
        createGuessEntry()
        first = False

def clearDifficultyButtons():
    EasyBtn.destroy()
    ModerateBtn.destroy()
    HardBtn.destroy()
    DifficultyFrame.destroy()

def difficultySelectionEasy(event):
    Difficulty.difficulty_selector("1")
    screen3o1()
    screen3o2()

def difficultySelectionModerate(event):
    Difficulty.difficulty_selector("2")
    screen3o1()
    screen3o2()

def difficultySelectionHard(event):
    Difficulty.difficulty_selector("3")
    screen3o1()
    screen3o2()

def entryPassed(event):
    global GEtext
    GEtext = int(GuessEntry.get())
    GuessEntry.delete(0, tk.END)
    GameWindow.update()
    GameHandler.game_question(GEtext)
    if GameHandler.win_check() == False:
        screen3o2

run()
