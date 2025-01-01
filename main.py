import tkinter as tk


def display_message():
    #Given a string sets the text of a label to the given parameter
    label.config(text="Hello, welcome to Python GUI!")
    label.config(highlightbackground="blue", highlightthickness=2)

window = tk.Tk()
window.title("Simple Python GUI")
window.geometry("300x200")

label = tk.Label(window, text="Click the button below", font=("Arial", 14), 
                 highlightbackground="green", highlightthickness=2)
label.pack(pady=20)

button = tk.Button(window, text="Click Me", command=display_message)
button.pack()

window.mainloop()



