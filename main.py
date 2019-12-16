from googletrans import Translator
import pytesseract
import pyautogui
import time

#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
translator = Translator()
newtext = ''
oldtext = ''
dictionary = {}
time.sleep(4)
while True:
    time.sleep(1.5)
    image = pyautogui.screenshot(region=(288, 420, 1000, 200))#region=(748,752, 1800, 200)
    image.save("epic.png")
    oldtext= newtext
    newtext = pytesseract.image_to_string(image)
    if newtext[:11:] == 'Your answer':
        image = pyautogui.screenshot(region=(480, 369, 928, 75))#region=(1024,696, 928, 75)
        image.save("epic.png")
        answer = pytesseract.image_to_string(image)
        dictionary[oldtext] = answer
    else:
        try:
            translated = dictionary[newtext]
        except:
            translated = str(translator.translate(newtext).text)
        if translated == '':
            translated = 'a'
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.typewrite(translated)
    pyautogui.press('enter')