import tkinter as tk

window = tk.Tk()
window.title("Hello World")
window.geometry("800x800")

def close_window(event):
  # Close the window
  window.destroy()

def print_text(event):
  txt = entry.get()
  label.config(text=txt)

def byebye(event):
  bye.destroy()

button = tk.Button(window, text="Click Me!")
button.bind("<Button-1>", close_window)
button.pack()

global bye
bye = tk.Button(window, text="bye")
bye.bind("<Button-1>", byebye)
bye.pack()

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