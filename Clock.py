import tkinter as tk
from tkinter import *
import os
from time import strftime

color_tipe_bckg = '#1d1d1d'
color_green = '#09B83D'
font_text = 'Tangerine'
font_size_text_up = 16
font_size_text_middle = 14
font_size_text_down = 64
root = tk.Tk()
root.title("Time")
root.geometry("600x320")
root.maxsize(600,320)
root.minsize(600,320)
root.configure(background= color_tipe_bckg)

def get_hello():
    name_user = os.getlogin()
    if os.getlogin() == 'rapha':
        name_user = 'Slytherin'
    hello.config( text = 'Hi, ' + name_user)
def get_data():
    data_now = strftime(' %a, %d %b %Y')
    data.config(text = data_now)
def get_hour():
    hour_now = strftime('%H:%M:%S')
    hour.config(text=hour_now)
    hour.after(1000, get_hour)
if os.getlogin() == 'rapha':
    font_size_text_up = 35
    font_size_text_middle = 25
    font_size_text_down = 60
tela = tk.Canvas(root, width=600, height=60, bg= color_tipe_bckg, bd=0, highlightthickness=0, relief='ridge')
tela.pack()
hello = Label(root, bg = color_tipe_bckg, fg= color_green, font = (font_text, font_size_text_up))
hello.pack()
data = Label(root, bg = color_tipe_bckg, fg= color_green, font = (font_text, font_size_text_middle))
data.pack(pady=2)
hour = Label(root, bg = color_tipe_bckg, fg= color_green, font = (font_text, font_size_text_down, 'bold'))
hour.pack(pady=2)
get_data()
get_hello()
get_hour()

# Run
root.mainloop()
