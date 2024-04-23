# 开发时间：2024/2/17 13:25
import pyttsx3


def tts(text):
    # 初始化语音
    engine = pyttsx3.init()  # 初始化语音库
    # 设置语速
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    # 输出语音
    engine.say(text)  # 合成语音
    engine.runAndWait()

# if __name__=='__main__':
#     text = "hello，请问你叫什么!"
#     tts(text)


