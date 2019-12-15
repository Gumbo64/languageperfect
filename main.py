from googletrans import Translator
import pytesseract
import pyautogui
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
translator = Translator()
newtext = ''
oldtext = ''
dictionary = {}
time.sleep(4)
while True:
    time.sleep(2)
    image = pyautogui.screenshot(region=(748,752, 1800, 200))#
    image.save("epic.png")
    oldtext= newtext
    newtext = pytesseract.image_to_string(image)
    if newtext[:11:] == 'Your answer':
        image = pyautogui.screenshot(region=(1024,696, 928, 75))#
        image.save("epic.png")
        answer = pytesseract.image_to_string(image)
        translated = dictionary[newtext]
        dictionary[oldtext] = answer
    else:
        try:
            translated = dictionary[newtext]
        except:
            translated = str(translator.translate(newtext).text)
        pyautogui.typewrite(translated)
    pyautogui.press('enter')