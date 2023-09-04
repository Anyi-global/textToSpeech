import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
import PyPDF2
import threading

##The window frame
root=Tk()
root.title("Text to speech")
root.geometry("900x500+200+200")
root.resizable(False,False)
root.configure(bg="#305065")


engine = pyttsx3.init()

def speaknow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()

    if (text):
        if (speed =="Fast"):
            engine.setProperty('rate', 250)
            setvoice()
        elif (speed == 'Normal'):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()


def download():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text ,'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text ,'text.mp3')
            engine.runAndWait()

    if (text):
        if (speed =="Fast"):
            engine.setProperty('rate', 250)
            setvoice()
        elif (speed == 'Normal'):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()


def upload():
    file_path = filedialog.askopenfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
    with open(file_path, 'rb') as file:
        pdf_text = ""
        for page in PyPDF2.PdfReader(file).pages:
            pdf_text += page.extract_text()
        text_area.insert(END, pdf_text)


def exit_app():
    root.destroy()

#icon
image_icon=PhotoImage(file="mic.png")
root.iconphoto(False,image_icon)

#Top Frame
Top_frame=Frame(root,bg="white",width=900,height=100)
Top_frame.place(x=0,y=0)

Logo=PhotoImage(file="speech_r.png")
Label(Top_frame,image=Logo,width=100,height=100,bg="white").place(x=5,y=1)

Label(Top_frame,text="TEXT TO SPEECH",font="arial 20 bold",bg="white",fg="black").place(x=100,y=30)


##create a scrollbar
scrollbar = Scrollbar(root)
scrollbar.place(x=510, y=150, height=250)

text_area=Text(root,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD, yscrollcommand=scrollbar.set)
text_area.place(x=10,y=150,width=500,height=250)

##attach the scrollbar to the text area
scrollbar.config(command=text_area.yview)

Label(root,text="VOICE",font="arial 15 bold",bg="#305065",fg="white").place(x=580,y=160)
Label(root,text="SPEED",font="arial 15 bold",bg="#305065",fg="white").place(x=760,y=160)

gender_combobox=Combobox(root,values=['Male','Female'],font="arial 14",state='r',width=10)
gender_combobox.place(x=550,y=200)
gender_combobox.set('Male')


speed_combobox=Combobox(root,values=['Fast','Normal','Slow'],font="arial 14",state='r',width=10)
speed_combobox.place(x=730,y=200)
speed_combobox.set('Normal')

imageicon=PhotoImage(file="")
speak_btn=Button(root,text="Speak",compound=LEFT,image=imageicon,width=130,bg="#39c790",font="arial 14 bold",command=speaknow)
speak_btn.place(x=550,y=280)

imageicon2=PhotoImage(file="")
save=Button(root,text="Save",compound=LEFT,image=imageicon2,width=130,bg="#39c790",font="arial 14 bold",command=download)
save.place(x=730,y=280)

upload_icon = PhotoImage(file="")
upload_btn = Button(root,text="Upload pdf",compound=LEFT,image=upload_icon,width=130,bg="#d3ff8f",font="arial 14 bold",command=upload)
upload_btn.place(x=550, y=360)

exit_icon = PhotoImage(file="")
exit_btn = Button(root,text="Cancel",compound=LEFT,image=exit_icon,width=130,bg="red",font="arial 14 bold",command=exit_app)
exit_btn.place(x=730, y=360)



root.mainloop()
