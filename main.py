# A Tkinter GUI desktop application that tests your typing speed.

from tkinter import *
import time
from texts import text
import random

# prompt text
prompt_choice = random.choice(text)
# word list to compare answer against
words = prompt_choice.lower().split(" ")

class GUI:
    def __init__(self):
        # window set up
        self.window = Tk()
        # establish start & end time, wpm for later
        self.start_time = 0
        self.end_time = 0
        self.final_wpm = ""
        # window setup cont'd
        self.window.geometry("800x800")
        self.window.config(padx=10, pady=10)
        self.window.title("Typing Speed Test")

        # explanation of test
        explain_label = Label(self.window,
                              text="Hit 'Start', then begin typing the prompt text.\nPress the space bar after each"
                                   " word.\n When you finish, hit the 'Done' button.\n"
                                   "Remember to type carefully - misspellings count as a wrong answer!")
        explain_label.config(font=("Times New Roman", 16))
        explain_label.pack()

        # text to be typed window
        test = Text(self.window, height=9, width=76, wrap='word')

        # insert text before disabling edits
        test.insert(1.0, prompt_choice.lower())
        # disable edits
        test.config(state='disabled')
        testlabel = Label(self.window, text="Prompt Text")
        testlabel.config(font=("Times New Roman", 12))
        testlabel.pack()
        test.pack()

        self.answer = Text(self.window, height=9, width=76, wrap='word')
        answerlabel = Label(self.window, text="Typing Test")
        answerlabel.config(font=("Times New Roman", 12))
        answerlabel.pack()
        startbutton = Button(self.window, text="Start", command=self.start)
        startbutton.pack()
        self.answer.pack()

        # done button
        donebutton = Button(self.window, text="Done", command=self.check_answer)
        donebutton.pack()

        # exit button
        quitbutton = Button(self.window, text="Quit",
                            command=self.window.destroy)
        quitbutton.pack()
        print(self.final_wpm)
        self.window.mainloop()

    def check_answer(self):
        # establish the end time when user hits done
        self.end_time = time.time()
        # get the answer, split it into a list of the same format as words variable
        user_answer = self.answer.get(1.0, 'end')
        user_answer_as_list = user_answer.split(" ")
        # create a list of the correct words to calculate wpm
        wpm_list = [i for i, j in zip(words, user_answer_as_list) if i == j]
        # calculate minutes elapsed
        time_elapsed = self.end_time - self.start_time
        mins_elapsed = time_elapsed/60
        # calculate WPM
        self.final_wpm = str(len(wpm_list) / mins_elapsed)
        # wpm display
        wpm = Text(self.window, height=1, width=6)
        wpm.insert(1.0, self.final_wpm)
        wpm.config(state='disabled')
        self.answer.config(state='disabled')
        wpmlabel = Label(self.window, text="Your WPM:")
        wpmlabel.config(font=("Times New Roman", 12))
        wpmlabel.pack()
        wpm.pack()

    def start(self):
        # establish the start time when user hits start
        self.start_time = time.time()


GUI()
