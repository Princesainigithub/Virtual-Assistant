from distutils.cmd import Command
from distutils.log import info
from multiprocessing.connection import Listener
from multiprocessing.spawn import import_main_path
import speech_recognition as sr
import pyaudio
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

Listener = sr.Recognizer()
engine =pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
  engine.say(text)
  engine.runAndWait()

def take_command():
  try:
    with sr.Microphone() as source:
      print('listening...')
      voice=Listener.listen(source)
      Command=Listener.recognize_google(voice)
      Command=Command.lower()
      if 'alexa' in Command:
        Command = Command.replace('alexa')
        print(Command)
  except:
    pass
  return Command


def run_alexa():
  Command=take_command()
  print(Command)
  if 'play' in Command:
    song= Command.replace('play', '')
    talk('playing' + song)
    pywhatkit.playonyt(song)
  elif 'time' in Command:
    time=datetime.datetime.now().strftime('%I:%M')
    talk('current time is '+ time)
  elif 'who the heck is ' in Command:
    person=Command.replace('who the heck is')
    info=wikipedia.summary(person,1)
    print(info)
    talk(info)
  elif 'date' in Command:
    talk('sorry,  I have a headache')
  elif 'are you single' in Command:
    talk('I am in a relationship with wifi')
  elif 'joke'in Command:
    talk(pyjokes.get_joke())
  else:
    talk('please say the command again')


while True:
  run_alexa()


