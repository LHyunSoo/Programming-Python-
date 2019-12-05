import pyautogui as pag

if __name__ == '__main__':
    pag.moveTo(37,237,duration=2)

    # 더블 클릭 (크롬 실행)
    # pag.click()
    # pag.click()
    # pag.click(clicks=2)
    # pag.doubleClick()

    # 크롬 실행후 페북 실행
    # pag.move(380,534,duration=2)
    # pag.click()

    #드레그
    pag.drag(1110,200,duration=2)