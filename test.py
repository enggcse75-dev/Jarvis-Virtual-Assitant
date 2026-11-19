import speech_recognition as sr
r = sr.Recognizer()
print(sr.__version__)
print(hasattr(r, "recognize_google"))