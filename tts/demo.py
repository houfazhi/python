import pyttsx3
with open("../file/a.txt", 'r', encoding='utf-8') as rfile:
        lyric = rfile.read()
engine = pyttsx3.init()
if lyric:
    engine.say(lyric)
    engine.runAndWait()
    engine.stop()
