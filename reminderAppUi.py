from plyer import notification
from tkinter import *
from tkinter.messagebox import showinfo, showwarning
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
import time

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

         # Window parameters
        winWidth = 1000
        winHeight = 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width/2) - (winWidth/2)
        y = (screen_height/2) - (winHeight/2)
        self.title("To-Do/Reminder App")
        self.geometry("%dx%d" % (winWidth, winHeight))
        self["background"] = '#49BEAA'

        lbl = Label(self, text = "To-Do/Reminder App", fg = "black", bg = "#49BEAA", font = ("Fira Sans", 40))
        lbl.pack(side = TOP, pady = 5)

        # Buttons to access new windows
        self.toDoList = Button(self, text = "Open To-Do List", font = ("Fira Sans, Thin", 16), fg = "black", bg = "#3C91E6", 
        height = 13, width = 20, activebackground = "#5EFC8D", highlightthickness = 0, borderwidth = 1)

        self.toDoList.place(relx = 0.25, rely = 0.5, anchor = CENTER)

        self.reminders = Button(self, text = "Reminders", font = ("Fira Sans, Thin", 16), fg = "black", bg = "#3C91E6", 
        height = 13, width = 20, activebackground = "#5EFC8D", highlightthickness = 0, borderwidth = 1)

        self.reminders['command'] = self.ReminderApp
        self.reminders.place(relx = 0.75, rely = 0.5, anchor = CENTER)

        self.closeApp = Button(self, text = "Close",  font = ("Fira Sans, Thin", 12), bg = "#EF767A", activebackground = "#5EFC8D", 
        height = 2, width = 10, bd = 0, highlightthickness = 0)
        self.closeApp.pack(side = BOTTOM, pady = 20)
        self.closeApp['command'] = self.quit

    # Reminder class to create reminder
    class ReminderApp(tk.Tk):
        def __init__(self):
            super().__init__()

            global reminderTxt
            global timeTxt

            self.geometry('600x400')
            self.title("Reminder App")
            self["background"] = '#49BEAA'

            lbl = Label(self, text = "Reminder App", fg = "black", bg = "#49BEAA", font = ("Fira Sans", 30))
            lbl.pack(side = TOP, pady = 5)

            # Set reminder to give a message after
            lbl = Label(self, text = "Reminder:", bg = "#49BEAA", font = ("Fira Sans, Thin", 20))
            lbl.place(relx = 0.25, rely = 0.44, anchor = CENTER)
            reminderTxt = Text(self, bg = "white", height = 1, width = 15, font = ("Fira Sans, Thin", 14), bd = 0)
            reminderTxt.place(relx = 0.25, rely = 0.5, anchor = CENTER)

            lbl = Label(self, text = "in", bg = "#49BEAA", font = ("Fira Sans, Thin", 18))
            lbl.place(relx = 0.5, rely = 0.5, anchor = CENTER)

            # Set reminder to go off at a certain time
            lbl = Label(self, text = "Time (minutes):", bg = "#49BEAA", font = ("Fira Sans, Thin", 18))
            lbl.place(relx = 0.72, rely = 0.44, anchor = CENTER)
            timeTxt = Text(self, bg = "white", height = 1, width = 7, font = ("Fira Sans, Thin", 14), bd = 0)
            timeTxt.place(relx = 0.72, rely = 0.5, anchor = CENTER)

            # Close the whole app
            self.button = Button(self, text = "Set Reminder",  font = ("Fira Sans, Thin", 16), bg = "#3C91E6", activebackground = "#5EFC8D", bd = 0, highlightthickness = 0)
            self.button['command'] = self.set_reminder
            self.button.place(relx = 0.5, rely = 0.75, anchor = CENTER)

        # Get the input from reminder text
        def retrieve_reminder(self):
            inputValue=reminderTxt.get("1.0","end-1c")
            return inputValue

        # Get the input from timer text
        def retrieve_time(self):
            inputValue = timeTxt.get("1.0","end-1c")
            
            # Error input if no value is set
            if(inputValue == ''):
                self.destroy()
                showwarning(title = "Error", message = "You must enter a number")
                raise Exception("You must enter a number")
                    
            else:
                timeFloat = float(inputValue)
                type(timeFloat)
                # Error catching for incorrect input
                if(timeFloat < 0):
                    self.destroy()
                    showwarning(title = "Error", message = "You must enter a number greater than 0")
                    raise ValueError("You must enter a number greater than 0")
                else:
                    print("Time set is to", inputValue, "minutes")
                    return timeFloat

        # Function to set reminders
        def set_reminder(self):
            reminder = self.retrieve_reminder()
            timer = self.retrieve_time()

            notification.notify(
            title = "REMINDER",
            message = "Reminder set!",
            timeout = 1
            )

            showinfo(title = "Reminder", message = "Reminder set!")
            self.destroy()

            time.sleep(timer * 60)
            notification.notify(
            title = "REMINDER",
            message = reminder,
            timeout = 10
            )
            print("TIMER OFF")
                        

    class ToDo(tk.Tk):
        def __init__(self):
            super().__init__()

            self.geometry('600x400')
            self.title("To-Do App")
            self["background"] = '#EFD09E'

if __name__ == "__main__":

    main = MainApp()
    mainloop()

# root=Tk()

# textBox=Text(root, height=2, width=10)
# textBox.pack()
# buttonCommit=Button(root, height=1, width=10, text="Commit", 
#                     command=lambda: retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button
# buttonCommit.pack()

# mainloop()

