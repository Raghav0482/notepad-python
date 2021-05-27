from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox

# basic tkinter commands

main = Tk()
main.title("NotepadByRaghav")

# main functions used in programs
def NewFile():
    writingArea.delete(1.0, END)

def OpenFile():
    f_in = askopenfile(title="Open File")
    if f_in is not None:
        # deleting from listbox
        writingArea.delete(1.0, END)

        # reading items from file
        items = f_in.readlines()

        # inserting line by line in listbox
        for item in items:
            writingArea.insert(END, item)
def SaveFile():
    f_out = asksaveasfile(defaultextension=".txt")
    if f_out is not None:
        print(writingArea.get(1.0, END), file=f_out)

        writingArea.delete(1.0, END)

def About():
    messagebox.showinfo("About Notepad", "This NotePad is created by Raghav Kumar.\nIt was created in python")

# main buttons
OpenButton = Button(main, text = "Open", command = OpenFile, width = 10)
SaveButton = Button(main, text = "Save", command = SaveFile, width = 10)
AboutButton = Button(main, text = "About Us", command = About, width = 10)
NewButton = Button(main, text = "New", command = NewFile, width = 10)
# placement of main buttons

NewButton.grid(row = 0, column = 0, padx = 10, pady = 10)
SaveButton.grid(row = 0, column = 1, padx = 10, pady = 10)
OpenButton.grid(row = 0, column = 2, padx = 10, pady = 10)
AboutButton.grid(row = 0, column = 3, padx = 10, pady = 10)

# main area
writingArea = Text(main, wrap = WORD, font = "Calibri 16")
# main area placement
writingArea.grid( row = 1,  column= 0, padx = 5, pady = 5, columnspan = 4)
main.mainloop()

