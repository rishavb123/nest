from thermostat import init, set_temp
import speech_recognition as sr


def to_int(s):
    try:
        if len(s) <= 0:
            return None
        return int(s)
    except ValueError:
        return to_int(s[:-1])


init("will set the temperature to what you tell it to")


r = sr.Recognizer()

with sr.Microphone() as source:

    while True:
        audio = r.listen(source)
        try:
            text = str(r.recognize_google(audio)).lower()

            i = text.index("set the temperature to")
            set_temp(to_int(text[i + 22:]))

        except (ValueError, sr.UnknownValueError):
            pass
