import pyttsx3
if __name__ == "__main__":
    with open("../file/a.txt", 'r', encoding='utf-8') as rfile:
            lyric = rfile.read()
    engine = pyttsx3.init()
    if lyric:
        engine.say(lyric)
        engine.runAndWait()
        engine.stop()
