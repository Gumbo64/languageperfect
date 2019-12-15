from googletrans import Translator
import pytesseract
import pyautogui
import time
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
translator = Translator()
time.sleep(5)
image = pyautogui.screenshot(region=(748,752, 1800, 200))#
image.save("epic.png")
text = pytesseract.image_to_string(image)
print(text)
translated = str(translator.translate(text).text)
print(translated)
pyautogui.typewrite(translated)
print('done')