import tkinter as tk

def say_hello():
    label.config(
        text="Hello from VS Code!",
        fg="white",
        bg="green"
    )

window = tk.Tk()
window.title("Hello GUI")
window.geometry("300x200")
window.configure(bg="lightblue")

button = tk.Button(
    window,
    text="Click Me",
    font=("Arial", 12),
    bg="blue",
    fg="white",
    command=say_hello
)
button.pack(pady=20)

label = tk.Label(
    window,
    text="",
    font=("Arial", 14),
    bg="lightblue"
)
label.pack()

window.mainloop()


