import time
from tkinter import Tk, Label, Entry
import random

def typing_test(text):
    start_time = time.time()

    root = Tk()
    label = Label(root, text=text)
    label.pack()

    entry = Entry(root)
    entry.pack()

    root.mainloop()

    time_taken = time.time() - start_time

    typing_speed = len(text) / time_taken

    return typing_speed

texts = [
    "Diesmal schenken wir uns aber nichts.",
    "Das kann man ja auch noch kalt essen.",
    "Ihr wart dann auf einmal irgendwie weg.",
    "Das Jahr ist wieder irgendwie so schnell vergangen.",
    "Die sind doch auch schon ewig zusammen."
]

for text in texts:
    typing_speed = typing_test(text)
    print(f"Ihre Geschwindigkeit für '{text}' beträgt {typing_speed} Zeichen pro Sekunde.")