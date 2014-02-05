import win32com.client as comclt
import win32api, win32con
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
from time import sleep
wsh= comclt.Dispatch("WScript.Shell")
def choose():
    #wsh.AppActivate(5020) # select another application
    #sleep(.2)
    #wsh.SendKeys("{BACKSPACE}") # send the keys you want
    #click(50,20)
    pass
def press_up():
    choose()
    wsh.SendKeys("{UP}")

def press_down():
    choose()
    wsh.SendKeys("{DOWN}")

def press_left():
    choose()
    wsh.SendKeys("{LEFT}")

def press_right():
    choose()
    wsh.SendKeys("{RIGHT}")