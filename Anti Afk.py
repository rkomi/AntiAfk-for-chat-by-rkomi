#Anti Afk by rkomi

import pyautogui, time

time.sleep(float(5))

b = int(1)

while 0 == 0:
    f = open('Text.txt', 'r')
    for word in f:
        a = word
        word = (str(a) * int(b))
        pyautogui.typewrite(word)
        time.sleep(float(30))