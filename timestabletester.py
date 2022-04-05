#
from tkinter import *
import random

class TimesTableTester:
    def __init__(self, parent):
        '''Create the labels and buttons'''
        self.Question = Label(parent, text="")
        self.Question.grid(column=0,row=0,sticky=NW, padx=50, pady=10)

        self.CheckAnsBtn = Button(parent, text="Check Answer", command = self.check)
        self.CheckAnsBtn.grid(column=0,row=1, sticky=SW, padx=40)

        self.InputAns = Entry(parent, width=5)
        self.InputAns.grid(column=1,row=0,sticky=NE, pady=10)

        self.Next = Button(parent, text="Next", command=self.change)
        self.Next.grid(column=1,row=1, sticky=SE)

        self.CheckAns = Label(parent, text="")
        self.CheckAns.grid(column=1,row=2)

        self.rand1 = (random.randint(1,10))
        self.rand2 = (random.randint(1,10))
        self.Question.configure(text="{} * {} =".format(str(self.rand1), str(self.rand2)))

    def change(self):
        '''Create two numbers between 1 to 9'''
        self.rand1 = (random.randint(1,10))
        self.rand2 = (random.randint(1,10))
        self.Question.configure(text="{} * {} =".format(str(self.rand1), str(self.rand2)))
    
    def check(self):
        '''Checks if the input is valid'''
        AnswerQtns = self.rand1 * self.rand2 
        if int(self.InputAns.get()) == AnswerQtns:
            self.CheckAns.configure(text="Correct")
        else:
            self.CheckAns.configure(text="Incorrect")            

#main rountine
root = Tk()
root.geometry("250x100")
timestable=(TimesTableTester(root))
root.mainloop()