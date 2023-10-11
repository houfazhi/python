import speech
from gtts import gTTS
import pyttsx3
import speech_recognition as sr

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save('output.mp3')

def speech_to_text():
   while True:
       recognizer = sr.Recognizer()
       with sr.Microphone() as source:
           print("请说点什么")
           speech.say("请说点什么")
           audio = recognizer.listen(source, timeout=5)  # 设置5秒的超时时间
       try:
           text = recognizer.recognize_google(audio, language='zh-CN')  # 使用中文进行语音识别
           print("你说的是: " + text + "吗？")
           speech.say("你说的是: " + text + "吗？")
           speech.say("请回答：")
           text1 = recognizer.recognize_google(audio, language='zh-CN')  # 使用中文进行语音识别
           if text1  == "是":
               break
           return text
       except sr.UnknownValueError:
           print("抱歉，我无法理解你说的话。")
           return ""
       except sr.RequestError:
           print("抱歉，语音识别服务出现错误。")
           return ""
if __name__ == "__main__":
    # Speech to Text
    recognized_text = speech_to_text()
    # Text to Speech
    if recognized_text:
        print("Recognized text: " + recognized_text)
        text_to_speech(recognized_text)

    engine = pyttsx3.init()
    engine.say("Task completed")
    engine.runAndWait()
