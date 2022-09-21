import time
import schedule
from plyer import notification

def school_Reminder30():  
    notification.notify(
        title = "REMINDER",
        message = "Class in 30 Minutes",
        timeout = 10
    )

def school_Reminder5():
    notification.notify(
    title = "REMINDER",
    message = "CLASS IN 5 MINUTES",
    timeout = 10
    )

def running():
    print("Running school reminder app")

# Main
# os.system("gnome-terminal 'bash -c'")
running()

schedule.every().monday.at("10:30").do(school_Reminder30)

schedule.every().monday.at("10:55").do(school_Reminder5)

while True:
    schedule.run_pending()
    time.sleep(1)

# Desktop notification for class start times