import os
import time
import tkinter as tk
from idlelib.EditorWindow import EditorWindow

def autosave():
    root = tk.Tk()
    root.withdraw()
    windows = EditorWindow.GetOpenWindows()
    for window in windows:
        if window.edit_modified():
            window.text.save()
            window.edit_modified(False)
    root.destroy()

while True:
    autosave()
    time.sleep(300) # 5 minutes in seconds
