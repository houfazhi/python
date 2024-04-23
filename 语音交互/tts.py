# 开发时间：2024/2/17 13:25
import pyttsx3
import win32com.client

if __name__ == '__main__':
    if "退出。".__contains__("退出"):
        print("kyishiyog")
    # 初始化语音
    engine = pyttsx3.init()  # 初始化语音库
    # 设置语速
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    # 输出语音
    engine.say("你好，很高兴认识你！")  # 合成语音
    engine.runAndWait()


# if __name__ == '__main__':
#     speaker = win32com.client.Dispatch("SAPI.SpVoice")
#     speaker.Speak("我是语音助手，小灵！")