from thermostat import init, set_temp, finish, get_temp
import speech_recognition as sr
import pyttsx3
import datetime


def to_int(s):
    try:
        if len(s) <= 0:
            return None
        return int(s)
    except ValueError:
        return to_int(s[:-1])


init("will set the temperature to what you tell it to")

engine = pyttsx3.init()
r = sr.Recognizer()

with sr.Microphone() as source:
    try:
        while True:
            t = datetime.datetime.now()
            audio = r.listen(source)

            try:
                text = str(r.recognize_google(audio)).lower()
                print(text)
                i = text.index("temperature to")
                set_temp(to_int(text[i + 14:]))
                engine.say("I'm setting the temperature to {}".format(to_int(text[i + 14:])))
                engine.runAndWait()
            except ValueError:
                if text.find("what's the temperature") >= 0 or text.find("what is the temperature") >= 0\
                        or text.find("tell me the temperature") > 0:
                    engine.say("The temperature is {}.".format(get_temp()))
                    engine.runAndWait()
                elif text.find("thank") >= 0:
                    engine.say("You are very welcome")
                    engine.runAndWait()
            except sr.UnknownValueError:
                pass
    except KeyboardInterrupt:
        finish()
