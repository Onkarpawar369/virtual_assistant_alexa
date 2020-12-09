import speech_recognition as sr
import pyaudio
import pywhatkit
import pyttsx3
import datetime
import wikipedia
import pyjokes
listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
voices=engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening.....')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
                print(command)
    except:
        pass
    return command

def run_alexa():
    statement=take_command()
    if 'play' in statement:
        song=statement.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    if 'time' in statement:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is'+time)
    if 'who is' in statement:
        person=statement.replace('who is','')
        info=wikipedia.summary(person,1)
        talk(info)
    if 'joke' in statement:
        jokes=pyjokes.get_joke()
        talk(jokes)
run_alexa()