import tkinter as tk

window = tk.Tk()
window.title("Hello World")
window.geometry("800x800")

difficulty_frame = tk.Frame(window,
                            width="20",
                            height="15",
                            border="1",
                            highlightbackground="blue")
difficulty_frame.rowconfigure(0, weight=1)

def close_window(event):
  # Close the window
  window.destroy()

def print_text(event):
  txt = entry.get()
  label.config(text=txt)

def byebye(event):
  easy.destroy()
  moderate.destroy()
  hard.destroy()

button = tk.Button(window, text="Click Me!")
button.bind("<Button-1>", close_window)
button.pack()

global easy
easy = tk.Button(difficulty_frame,
                text="Easy",
                width="7",
                height="3",
                fg="red",
                font="18"
                )
easy.bind("<Button-1>", byebye)
easy.grid(row=0, column=0, sticky="news")

global moderate
moderate = tk.Button(difficulty_frame,
                text="Moderate",
                width="7",
                height="3",
                fg="red",
                font="18"
                )
moderate.bind("<Button-1>", byebye)
moderate.grid(row=0, column=1, sticky="news")

global hard
hard = tk.Button(difficulty_frame,
                text="Hard",
                width="7",
                height="3",
                fg="red",
                font="18"
                )
hard.bind("<Button-1>", byebye)
hard.grid(row=0, column=2, sticky="news")

difficulty_frame.place(y=5)
difficulty_frame.pack(padx=10, pady=10)

entry = tk.Entry(window)
entry.bind("<Return>", print_text)
entry.pack()

# label = tk.Label(window)
label = tk.Label(
    # window,
    text="Hello, Tkinter",
    fg="white",  # Set the text color to white
    bg="black"  # Set the background color to black
)
label.pack()

window.mainloop()