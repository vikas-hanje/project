import speech_recognition

recognizer = speech_recognition.Recognizer()
i = 1

while (i<=1):
    try:
        with speech_recognition.Microphone() as mic:
            print("Say something..")
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            text = text.lower()
            print(f"Recognized: {text}")
            i=i+1
    except speech_recognition.UnknownValueError:
        print("Sorry, could not understand the audio.")
        continue
    except speech_recognition.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")