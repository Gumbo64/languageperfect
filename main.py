import pyautogui
import time
import clipboard
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
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
screenx, screeny = pyautogui.size()
ypos = 163 

if __name__ == '__main__':
    time.sleep(4)
    while True:
        pyautogui.moveTo(0,ypos)
        pyautogui.click(screenx,ypos)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        oldtext = newtext
        newtext = clipboard.paste()
        if newtext.find('Correct answer') != -1:
            try:
                remove = Words.query.filter_by(german=oldtext).first()
                db.session.delete(remove)
                db.session.commit
            except:
                pass     
            pyautogui.hotkey('ctrl', 'c')
            unfiltered = clipboard.paste()
            start = unfiltered.find('Correct answer') + 14
            end = unfiltered.find('Your answer')
            unfiltered = unfiltered[start:end:]
            answer = unfiltered
            if verticalline:
                    if answer.find('|') != -1:
                        position = answer.find('|')
                        answer = answer[:position:]
                    else:
                        pass
            else:
                pass
            answer.replace('\n', '')
            answer.replace('\t','')
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
                translated = 'it'
            else:
                pyautogui.click(150, ypos+30, button='left')
            clipboard.copy(translated)
            pyautogui.hotkey('ctrl','v')
        pyautogui.press('enter')