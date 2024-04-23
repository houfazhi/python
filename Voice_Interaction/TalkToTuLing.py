# 开发时间：2024/2/19 15:22

import pyttsx3
from aip import AipSpeech
import requests
import json
import speech_recognition as sr
import win32com.client

# 初始化语音
# speaker = win32com.client.Dispatch("SAPI.SpVoice")
engine = pyttsx3.init()

# 1、语音生成音频文件,录音并以当前时间戳保存到voices文件中
# Use SpeechRecognition to record 使用语音识别录制
def my_record(rate=16000):
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=rate) as source:
        print("please say something")
        engine.say("please say something")
        engine.runAndWait()
        audio = r.listen(source)

    # 创建文件夹
    import os
    os.makedirs("voices", exist_ok=True)  # 如果目录已存在，则不会引发异常

    with open("voices/myvoices.wav", "wb") as f:
        f.write(audio.get_wav_data())



# 2、音频文件转文字：采用百度的语音识别python-SDK
# 导入我们需要的模块名，然后将音频文件发送给出去，返回文字。
# 百度语音识别API配置参数
APP_ID = '51777468'
API_KEY = 'xqegYUsSruduUouGVP5Udo8l'
SECRET_KEY = 'tVvfMAZ6o9E3AMqWvG9fsvVg0dGHRQnt'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
path = 'voices/myvoices.wav'


# 将语音转文本STT
def listen():
    # 读取录音文件
    with open(path, 'rb') as fp:
        voices = fp.read()
    try:
        # 参数dev_pid：1536普通话(支持简单的英文识别)、1537普通话(纯中文识别)、1737英语、1637粤语、1837四川话、1936普通话远场
        result = client.asr(voices, 'wav', 16000, {'dev_pid': 1537, })
        # result = CLIENT.asr(get_file_content(path), 'wav', 16000, {'lan': 'zh', })
        # print(result)
        # print(result['result'][0])
        # print(result)
        result_text = result["result"][0]
        print("you said: " + result_text)
        return result_text
    except KeyError:
        print("KeyError")
        # speaker.Speak("我没有听清楚，请再说一遍...")
        engine.say("我没有听清楚，请再说一遍...")
        engine.runAndWait()


# 3、与机器人对话：调用的是图灵机器人
# 图灵机器人的API_KEY、API_URL
turing_api_key = "baa33154ff9c47ec9f0b7c4b632e3d08"
api_url = "http://openapi.turingapi.com/openapi/api/v2"  # 图灵机器人api网址
headers = {'Content-Type': 'application/json;charset=UTF-8'}


# 图灵机器人回复
def Turing(text_words=""):
    req = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": text_words
            },

            "selfInfo": {
                "location": {
                    "city": "北京",
                    "province": "北京",
                    "street": "车公庄"
                }
            }
        },
        "userInfo": {
            "apiKey": turing_api_key,  # 你的图灵机器人apiKey
            "userId": "Nieson"  # 用户唯一标识(随便填, 非密钥)
        }
    }

    req["perception"]["inputText"]["text"] = text_words
    response = requests.request("post", api_url, json=req, headers=headers)
    response_dict = json.loads(response.text)

    result = response_dict["results"][0]["values"]["text"]
    print("AI Robot said: " + result)
    return result


# 语音合成，输出机器人的回答

def TalkToTuLing():
    engine.say("欢迎使用图灵机器人，您可以与我对话，请问有什么可以帮您。需要退出请说‘退出’或者‘结束’")
    engine.say("hello")
    engine.runAndWait()
    while True:
        my_record()
        request = listen()
        if request.__contains__("退出") or request.__contains__("结束"):
            engine.say("好的已经退出，谢谢使用")
            engine.runAndWait()
            break
        response = Turing(request)
        # speaker.Speak(response)
        engine.say(response)
        engine.runAndWait()
