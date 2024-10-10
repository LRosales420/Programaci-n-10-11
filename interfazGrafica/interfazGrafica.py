import tkinter as tk

root = tk.Tk()

"""
root.title("Mi primera ventana :D")
root.geometry("300x200")
"""

root.geometry("500x200")

label = tk.Label(root, text="Cuando yo la ví Jujuju", font=("Comic Sans MS", 24), fg="green")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Borrar la cuenta", font=("Papyrus", 16), bg="red", fg="blue", anchor="se")
button.pack()



root.mainloop()