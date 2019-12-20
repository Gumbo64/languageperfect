from googletrans import Translator
import pytesseract
import pyautogui
import time
import clipboard

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
translator = Translator()
newtext = ''
oldtext = ''
checktext = ''

app = Flask(__name__)
app.config['SECRET_KEY'] = 'zbnjlbrkns'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
engine = sqlalchemy.create_engine('sqlite:///db.sqlite3',connect_args={'check_same_thread': False})
session = sessionmaker(bind=engine)()
base = declarative_base()

class Words(db.Model):
    id = id = db.Column(db.Integer, primary_key=True)
    german = db.Column(db.String(999), unique=True, nullable=False)
    english = db.Column(db.String(999), nullable=False)

check = False
verticalline = True

if __name__ == '__main__':
    time.sleep(4)
    while True:
        time.sleep(1.5)
        image = pyautogui.screenshot(region=(12, 398, 1382, 140))#region=(748,752, 1800, 200)
        image.save("epic.png")
        oldtext= newtext
        newtext = pytesseract.image_to_string(image)
        if newtext.find('Your answer') != -1:
            try:
                remove = Words.query.filter_by(german=oldtext).first()
                db.session.delete(remove)
                db.session.commit
            except:
                pass

            #image = pyautogui.screenshot(region=(477, 354, 600, 95))#region=(1024,696, 928, 75)
            #image.save("epic1.png")
            x, y = pyautogui.locateCenterOnScreen('line.png')
            pyautogui.click(button='left', clicks=3, interval=0.25, x=x, y=y)
            pyautogui.hotkey('ctrl', 'c')
            answer = clipboard.paste()
            if verticalline:
                    if answer.find('|') != -1:
                        position = answer.find('|')
                        answer = answer[:position:]
                    else:
                        pass
            else:
                pass

            find = Words.query.filter_by(german = oldtext).first()
            if find is None:
                answer = Words(german = oldtext, english = answer)
                db.session.add(answer)
            else:
                find.english = answer
            db.session.commit()
        else:
            try:
                translated = Words.query.filter_by(german = newtext).first().english
            except:
                pos = newtext.find('(')
                translatext = newtext
                if pos != -1:
                    translatext = newtext[:pos:]
                if verticalline:
                    if translatext.find('|') != -1:
                        position = translatext.find('|')
                        translatext = translatext[:position:]
                    else:
                        pass
                print("translatext: " + translatext)
                translated = str(translator.translate(translatext).text)
            if translated == '':
                translated = 'it'
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.typewrite(translated)
            print("translated: " + translated)
        pyautogui.press('enter')