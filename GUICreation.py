import tkinter as tk

window = tk.Tk()
window.title("Hello World")
window.geometry("300x200")

def close_window(event):
  # Close the window
  window.destroy()

def print_text(event):
  txt = entry.get()
  label.config(text=txt)

button = tk.Button(window, text="Click Me!")
button.bind("<Button-1>", close_window)
button.pack()

entry = tk.Entry(window)
entry.bind("<Return>", print_text)
entry.pack()

# label = tk.Label(window)
label = tk.Label(
    # window,
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
)

label.pack()
window.mainloop()