import tkinter

# create window and give it a title
window = tkinter.Tk()
window.title("Test")

# window size
window.geometry("800x600")

# add text to window and adjust font and size
lbl = tkinter.Label(window, text="Press to get Testing Started", font=("Arial Bold", 20), bg="red")
lbl.grid(column=0, row=0)

# adding a button clicked event
def clicked():
    lbl.configure(text="You clicked the button!!!")

# adding a button widget
btn = tkinter.Button(window, text="Click Me", fg="orange", command=clicked)
btn.grid(column=1, row=0)

# make sure window is running constantly and waits for interaction
window.mainloop()
