import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:

    print('Start to talk')
    audio_data = r.record(source, duration=15)
    print("Recognizing...")
    text = r.recognize_google(audio_data)
    print(text)