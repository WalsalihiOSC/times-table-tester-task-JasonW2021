#
from tkinter import *

class TimesTableTester:
    def __init__(self, parent):
        Question = Label(parent, text="9 * 3 = ")
        Question.grid(column=0,row=0,sticky=NW, padx=50, pady=10)

        CheckAnsBtn = Button(parent, text="Check Answer")
        CheckAnsBtn.grid(column=0,row=1, sticky=SW, padx=40)

        InputAns = Entry(parent, width=5)
        InputAns.grid(column=1,row=0,sticky=NE, pady=10)

        Next = Button(parent, text="Next")
        Next.grid(column=1,row=1, sticky=SE)

#main rountine
root = Tk()
root.geometry("250x100")
timestable=(TimesTableTester(root))
root.mainloop()