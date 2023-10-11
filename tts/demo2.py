# 开发时间：2023/9/18 19:07
import speech
import speech_recognition as sr
speech.say("hello here is speech function test ")
speech.say("你的名字是什么")
# 初始化语音识别器
recognizer = sr.Recognizer()
# 使用麦克风录音
with sr.Microphone() as source:
    speech.say("please say")
    audio = recognizer.listen(source)
try:
    # 通过Google Web Speech API将语音转文本
    text = recognizer.recognize_google(audio)
    print("您说的是：" + text)
except sr.UnknownValueError:
    print("无法理解音频")
except sr.RequestError as e:
    print("无法请求Google Web Speech API; {0}".format(e))
