import os
import tkinter as tk
from PIL import ImageTk, Image

Window = tk.Tk()
Window.title("Hello World")
Window.geometry("800x800")

DifficultyFrame = tk.Frame(Window,
                            width="20",
                            height="15",
                            border="1",
                            highlightbackground="blue")
DifficultyFrame.rowconfigure(0, weight=1)

def closeWindow(event):
  # Close the Window
  Window.destroy()

def printText(event):
  Txt = Entry.get()
  Label.config(text=Txt)

def byeBye(event):
  Easy.destroy()
  Moderate.destroy()
  Hard.destroy()

Button = tk.Button(Window, text="Click Me!")
Button.bind("<Button-1>", closeWindow)
Button.pack()

global Easy
Easy = tk.Button(DifficultyFrame,
                text="Easy",
                width="7",
                height="3",
                fg="red",
                font="18"
                )
Easy.bind("<Button-1>", byeBye)
Easy.grid(row=0, column=0, sticky="news")

global Moderate
Moderate = tk.Button(DifficultyFrame,
                text="Moderate",
                width="7",
                height="3",
                fg="red",
                font="18"
                )
Moderate.bind("<Button-1>", byeBye)
Moderate.grid(row=0, column=1, sticky="news")

global Hard
Hard = tk.Button(DifficultyFrame,
                text="Hard",
                width="7",
                height="3",
                fg="red",
                font="18"
                )
Hard.bind("<Button-1>", byeBye)
Hard.grid(row=0, column=2, sticky="news")

DifficultyFrame.place(y=5)
DifficultyFrame.pack(padx=10, pady=10)

Entry = tk.Entry(Window)
Entry.bind("<Return>", printText)
Entry.pack()

# Label = tk.Label(Window)
Label = tk.Label(
    # Window,
    text="Hello, Tkinter",
    fg="white",  # Set the text color to white
    bg="black"  # Set the background color to black
)
Label.pack()

CascadeImage = Image.open("C:/Users/miles/Documents/Python/firstgame/image_files/Mario.png")
CascadeImage.thumbnail((480, 360))
CascadeImageCreate = ImageTk.PhotoImage(CascadeImage)
CascadeImageLabel = tk.Label(Window, image=CascadeImageCreate)
CascadeImageLabel.pack()
# ImagePath = os.path.normpath("C:/Users/miles/Documents/Python/firstgame/image_files/mario.png")#os.path.join(os.path.split(__file__)[0], "mario.png")
# img = tk.Image("photo", file=pint.pintk.plk.icon_img)
# Image = tk.Image("photo", file=ImagePath)

Window.mainloop()


# label1 = tk.Label(image=test)
# # label1.image = test

# # Position image
# label1.place(x=1, y=1)
# root.mainloop()