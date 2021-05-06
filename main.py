import speech_recognition as sr
import pyttsx3
import DesktopFunctions

listener = sr.Recognizer()
iris = pyttsx3.init()
voices = iris.getProperty('voices')
iris.setProperty('voice', voices[1].id)

def talk(response):
    iris.say(response)
    iris.runAndWait()

"""currently figuring out how to open programs on my desktop and do arithmatic"""
try:
    with sr.Microphone() as source:
        talk("hi, my name is iris, how can i assist you today? spotyfy ")
        print("listening...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice).lower()
        if 'iris' in command:
            command = command.replace('iris ', '')
            print(command)
            talk(command)
            if 'calculate' in command:
                command = command.replace('calculate ', '')
                if '*' in command:
                    talk('multiplying...')
                    command = command.replace('*', 'times')
                    parcedCommand = command.split(' ')
                    print(parcedCommand[0])
                    print(parcedCommand[-1])
                    result = int(parcedCommand[0]) * int(parcedCommand[-1])
                    print(result)
                    resultPrime = command + ' is ' + str(result)

                    talk(resultPrime)
            if 'open' in command:
                command = command.replace('open ', '')
                talk('openning ' + command)
                DesktopFunctions.openApp(command)
except:
    pass
