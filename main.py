from tkinter import*

window = Tk
window.title("event handler")
window.geometry("100x100")

def handle_keypress(event):
    """print the charecter asociated to the key pressed"""
    print(event.char)
    
window.bind("<key>", handle_keypress)

def handle_click(event):
    print("\nthe button was clicked!")
    
button=Button(text="click me!")
button.pack()

button.bind("<Button-1>",handle_click)

window.mainloop()