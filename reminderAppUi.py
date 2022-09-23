from plyer import notification
from tkinter import *
from tkinter.messagebox import showinfo, showwarning
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
import time
import datetime
import threading

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

         # Window parameters
        winWidth = 600
        winHeight = 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width/2) - (winWidth/2)
        y = (screen_height/2) - (winHeight/2)
        self.title("To-Do/Reminder App")
        self.geometry("%dx%d" % (winWidth, winHeight))
        self["background"] = '#44E5E7'

        lbl = Label(self, text = "Reminder App", fg = "black", bg = "#44E5E7", font = ("Fira Sans", 40))
        lbl.pack(side = TOP, pady = 5)

        self.reminders = Button(self, text = "Create Reminder", font = ("Fira Sans, Thin", 16), fg = "black", bg = "#1E96FC", 
        height = 13, width = 20, activebackground = "#5EFC8D", highlightthickness = 0, borderwidth = 1)
        self.reminders['command'] = self.ReminderApp
        self.reminders.place(relx = .5, rely = 0.5, anchor = CENTER)

        

        self.closeApp = Button(self, text = "Close",  font = ("Fira Sans, Thin", 12), bg = "#EF767A", activebackground = "#5EFC8D", 
        height = 2, width = 10, bd = 0, highlightthickness = 0)
        self.closeApp.pack(side = BOTTOM, pady = 20)
        self.closeApp['command'] = self.quit
    

        self.protocol("WM_DELETE_WINDOW", self.iconify)


    # Reminder class to create reminder
    class ReminderApp(tk.Tk):
        def __init__(self):
            super().__init__()

            global reminderTxt
            global timeTxt

            self.geometry('600x400')
            self.title("Reminder App")
            self["background"] = '#FAFF81'

            lbl = Label(self, text = "Reminder App", fg = "black", bg = "#FAFF81", font = ("Fira Sans", 30))
            lbl.pack(side = TOP, pady = 5)

            # Set reminder to give a message after
            lbl = Label(self, text = "Reminder:", bg = "#FAFF81", font = ("Fira Sans, Thin", 20))
            lbl.place(relx = 0.25, rely = 0.44, anchor = CENTER)
            reminderTxt = Text(self, bg = "white", height = 1, width = 15, font = ("Fira Sans, Thin", 14), bd = 0)
            reminderTxt.place(relx = 0.25, rely = 0.5, anchor = CENTER)

            lbl = Label(self, text = "in", bg = "#FAFF81", font = ("Fira Sans, Thin", 18))
            lbl.place(relx = 0.5, rely = 0.5, anchor = CENTER)

            # Set reminder to go off at a certain time
            lbl = Label(self, text = "Time(minutes):", bg = "#FAFF81", font = ("Fira Sans, Thin", 18))
            lbl.place(relx = 0.72, rely = 0.44, anchor = CENTER)
            timeTxt = Text(self, bg = "white", height = 1, width = 7, font = ("Fira Sans, Thin", 14), bd = 0)
            timeTxt.place(relx = 0.72, rely = 0.5, anchor = CENTER)

            # Close the whole app
            self.button = Button(self, text = "Set Reminder",  font = ("Fira Sans, Thin", 16), bg = "#1E96FC", activebackground = "#5EFC8D", bd = 0, highlightthickness = 0)
            self.button['command'] = self.set_reminder
            self.button.place(relx = 0.5, rely = 0.75, anchor = CENTER)

        # Get the input from reminder text
        def retrieve_reminder(self):
            inputValue=reminderTxt.get("1.0","end-1c")
            
            if(inputValue == ''):
                inputValue = "DEFAULT_REMINDER"
                return inputValue
            else:
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
                    print("Timer set is to", inputValue, "minutes")
                    return timeFloat

        # Function to set reminders
        def set_reminder(self):
            reminder = self.retrieve_reminder()
            timer = self.retrieve_time()

            notification.notify(
            title = "REMINDER",
            message = "Reminder set!",
            timeout = 5
            )

            def secondNotif():
                notification.notify(
                title = "REMINDER",
                message = reminder,
                timeout = 10
                )
                print(time.strftime("%H:%M:%S", time.localtime()))
                print("TIMER OFF")

            showinfo(title = "Reminder", message = "Reminder set!")
            self.destroy()

            print(time.strftime("%H:%M:%S", time.localtime()))
            threading.Timer(timer * 60, secondNotif).start()
                            

if __name__ == "__main__":

    main = MainApp()
    mainloop()


