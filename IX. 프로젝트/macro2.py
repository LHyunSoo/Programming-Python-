import pyautogui as pag
import time     #sleep

if __name__ == '__main__':
    pag.moveTo(200,200,2)
    pag.click()
    pag.typewrite("happy birth day to HyunSoo", interval=0.2)     #한글은 안돼연...
    pag.press("enter")
    pag.typewrite("happy birth day to me")
    pag.press("enter")
    pag.press("hangul")
    pag.typewrite("gustn toddlf djfak dksskadma")
    pag.press("hangul")