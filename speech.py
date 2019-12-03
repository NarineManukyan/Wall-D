import pyttsx3


def speak(toSpeak):
    print("help")
    engine = pyttsx3.init()
    engine.say('Good morning.')
    engine.runAndWait()