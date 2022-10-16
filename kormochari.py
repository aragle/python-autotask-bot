import pyautogui


def amar_jaiga_dekhao(n_second_pore):
    pyautogui.time.sleep(n_second_pore)
    return pyautogui.position()


def jao(x, y, n_second_pore):
    pyautogui.moveTo(x, y, duration=n_second_pore)


def lekho(kotha):
    pyautogui.typewrite(kotha)


def chapo():
    pyautogui.click()


def dan_button_chapo():
    pyautogui.rightClick()


def bam_button_chapo():
    pyautogui.leftClick()


def button_chapo(button):
    pyautogui.press(button)


def dui_bar_chapo():
    pyautogui.doubleClick()
