from tkinter import *
import datetime
import time
from playsound import playsound
import threading

# Function to play alarm sound
def play_alarm_sound():
    playsound("alarm_sound.mp3")  # Replace with path to your sound file

# Function to check the alarm time
def alarm(set_alarm_time):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == set_alarm_time:
            print("Wake up!")
            play_alarm_sound()
            break

# Function to get time from user and start alarm
def set_alarm():
    alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
    print(f"Alarm set for {alarm_time}")
    # Use threading to prevent GUI from freezing
    t1 = threading.Thread(target=alarm, args=(alarm_time,))
    t1.start()

# GUI setup
root = Tk()
root.title("Alarm Clock")
root.geometry("400x200")
root.config(bg="lightblue")

Label(root, text="Set Alarm Time", font=("Helvetica", 14), bg="lightblue").pack(pady=10)

frame = Frame(root, bg="lightblue")
frame.pack()

# Hour, Minute, Second dropdowns
hour = StringVar(root)
hour.set("00")
hours = [f"{i:02d}" for i in range(24)]
OptionMenu(frame, hour, *hours).pack(side=LEFT)

minute = StringVar(root)
minute.set("00")
minutes = [f"{i:02d}" for i in range(60)]
OptionMenu(frame, minute, *minutes).pack(side=LEFT)

second = StringVar(root)
second.set("00")
seconds = [f"{i:02d}" for i in range(60)]
OptionMenu(frame, second, *seconds).pack(side=LEFT)

Button(root, text="Set Alarm", command=set_alarm, bg="green", fg="white", font=("Helvetica", 12)).pack(pady=20)

root.mainloop()
