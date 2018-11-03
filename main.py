import serial
import time
import pyautogui
import win32com.client as comclt


wsh= comclt.Dispatch("WScript.Shell")
wsh.AppActivate("Notepad") # select another application


ser = serial.Serial('COM4', 9600, timeout = 1);
while 1:
    try:
        res = ser.read()
        res = res.decode("utf-8");
        resINT = ord(res);
        if resINT == 49:
            print(res);
            #pyautogui.press('D');
            wsh.SendKeys("d"); # send the keys you want
        elif resINT == 50: # 2
            print(res);
            #pyauAtogui.press('A');
            wsh.SendKeys("a"); # send the keys you want
    except:
        print("Cant read");
        time.sleep(1);


'''for i in range(0,3):
    pyautogui.press('A');
    time.sleep(1);'''