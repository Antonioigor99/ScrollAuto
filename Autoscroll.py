import pyautogui;
from tkinter import *;
import threading

global AutoScrollActive;

def scrollAutoOn():
    global AutoScrollActive;
    AutoScrollActive = True;
    threading.Thread(target=scrollAuto).start()
    
def scrollAutoOff():
    global AutoScrollActive;
    AutoScrollActive = False;
    

def scrollAuto():
    if AutoScrollActive is True:
        pyautogui.click(x=100, y=200);
        for _ in range(100):
            pyautogui.scroll(-10);
            break
        for _ in range(100):
            pyautogui.scroll(10);
            break

janela = Tk();
janela.title("Autoscroll");
texto = Label(janela, text="Clique Start para começar o Autoscroll");
texto.grid(column=0, row=0, padx=10, pady=10);

start = Button(janela, text="Start", command=scrollAutoOn);
start.grid(column=0, row=1, padx=10, pady=10);

stop = Button(janela, text="Stop", command=scrollAutoOff);
stop.grid(column=0, row=2, padx=10, pady=10);

janela.mainloop();
