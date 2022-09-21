from plyer import notification
from tkinter import *
from tkinter.messagebox import showinfo
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
        self["background"] = '#EFD09E'

        lbl = Label(self, text = "To-Do/Reminder App", fg = "black", bg = "#EFD09E", font = ("Fira Sans", 30))
        lbl.pack(side = TOP, pady = 5)

        # Buttons to access new windows
        self.toDoList = Button(self, text = "Open To-Do List", fg = "black", bg = "#3C91E6", height = 20, width = 40, activebackground = "#5EFC8D", highlightthickness = 0, borderwidth = 1)
        self.toDoList.place(relx = 0.25, rely = 0.5, anchor = CENTER)

        self.reminders = Button(self, text = "Reminders", fg = "black", bg = "#3C91E6", height = 20, width = 40, activebackground = "#5EFC8D", highlightthickness = 0, borderwidth = 1)
        self.reminders['command'] = self.ReminderApp
        self.reminders.place(relx = 0.75, rely = 0.5, anchor = CENTER)

    # Reminder class to create reminder
    class ReminderApp(tk.Tk):
        def __init__(self):
            super().__init__()

            self.geometry('600x400')
            self.title("Reminder App")
            self["background"] = '#EFD09E'



            lbl = Label(self, text = "Reminder App", fg = "black", bg = "#EFD09E", font = ("Fira Sans", 30))
            lbl.pack(side = TOP, pady = 5)

            # Set reminder to give a message after
            lbl = Label(self, text = "Reminder:", bg = "#EFD09E", font = ("Fira Sans, Thin", 20))
            lbl.place(relx = 0.25, rely = 0.44, anchor = CENTER)
            reminderTxt = Entry(self, bg = "white", width = 15, font = ("Fira Sans, Thin", 14), bd = 0)
            reminderTxt.place(relx = 0.25, rely = 0.5, anchor = CENTER)

            lbl = Label(self, text = "in", bg = "#EFD09E", font = ("Fira Sans, Thin", 18))
            lbl.place(relx = 0.5, rely = 0.5, anchor = CENTER)

            # Set reminder to go off at a certain time
            lbl = Label(self, text = "Time (minutes):", bg = "#EFD09E", font = ("Fira Sans, Thin", 18))
            lbl.place(relx = 0.72, rely = 0.44, anchor = CENTER)
            timeText = Entry(self, bg = "white", width = 7, font = ("Fira Sans, Thin", 14), bd = 0)
            timeText.place(relx = 0.72, rely = 0.5, anchor = CENTER)

            self.button = Button(self, text = "Set Reminder",  font = ("Fira Sans, Thin", 16), bg = "#3C91E6", activebackground = "#5EFC8D", bd = 0, highlightthickness = 0)
            self.button['command'] = self.set_reminder
            self.button.place(relx = 0.5, rely = 0.75, anchor = CENTER)

        def set_reminder(self):
            notification.notify(
            title = "REMINDER",
            message = "Reminder set!",
            timeout = 10
            )
            # notification.notify(
            # title = "REMINDER",
            # message = "Reminder set!",
            # timeout = 10
            # )
            showinfo(title = "Reminder", message = "Reminder set!")
            self.destroy()

        # def retrieve_input():
        #     txtInput = self.reminderTxt.get("1.0", END)
        #     print(str(txtInput))

    class ToDo(tk.Tk):
        def __init__(self):
            super().__init__()

            self.geometry('600x400')
            self.title("To-Do App")
            self["background"] = '#EFD09E'

if __name__ == "__main__":

    main = MainApp()
    main.mainloop()