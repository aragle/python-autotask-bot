import pyautogui


def amar_jaiga_dekhao(n_second_pore=1):
    pyautogui.time.sleep(n_second_pore)
    print(pyautogui.position())


def jao(x, y, n_second_pore):
    pyautogui.moveTo(x, y, duration=n_second_pore)


def lekho(kotha):
    pyautogui.typewrite(kotha)


def chapo():
    pyautogui.click()


def dan_button_chapo():
    pyautogui.rightClick()


def dui_bar_dan_button_chapo():
    pyautogui.doubleClick(button='left')


def key_chapo(key_name):
    pyautogui.press(key_name)


def dui_bar_chapo():
    pyautogui.doubleClick()


def ektu_thamo(n_second):
    pyautogui.time.sleep(n_second)


def thamo(n_second):
    pyautogui.PAUSE = n_second
