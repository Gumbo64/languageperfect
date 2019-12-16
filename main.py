from googletrans import Translator
import pytesseract
import pyautogui
import time

#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
translator = Translator()
newtext = ''
oldtext = ''
checktext = ''
dictionary = {}
check = False
time.sleep(4)
while True:
    time.sleep(1.5)
    image = pyautogui.screenshot(region=(12, 398, 1382, 140))#region=(748,752, 1800, 200)
    image.save("epic.png")
    oldtext= newtext
    newtext = pytesseract.image_to_string(image)
    if newtext[:11:] == 'Your answer':
        if check == True:
            try:
                dictionary.pop(checktext)
                check == False
            except:
                pass
        image = pyautogui.screenshot(region=(455, 359, 600, 95))#region=(1024,696, 928, 75)
        image.save("epic1.png")
        answer = pytesseract.image_to_string(image)
        dictionary[oldtext] = answer
    else:
        try:
            translated = dictionary[newtext]
            check = True
            checktext = newtext
        except:
            translated = str(translator.translate(newtext).text)
        if translated == '':
            translated = 'a'
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.typewrite(translated)
    pyautogui.press('enter')