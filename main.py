import serial
import time
import pyautogui

ser = serial.Serial('COM4', 115200, timeout = 1);
while 1:
    try:
        res = ser.read()
        res = res.decode("utf-8");
        resINT = ord(res);
        if resINT == 49:
            print(res);
            pyautogui.press('D');
        elif resINT == 50:
            print(res);
            pyautogui.press('A');
    except:
        print("Cant read");
        time.sleep(.5);


'''for i in range(0,3):
    pyautogui.press('A');
    time.sleep(1);'''