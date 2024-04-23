import speech_recognition as sr

# 初始化语音识别器并设置识别器为CMU Sphinx

# 下载PocketSphinx中文语言数据
sr.Microphone().list_microphone_names()
recognizer = sr.Recognizer()
recognizer.energy_threshold = 4000
recognizer.dynamic_energy_threshold = False

def listen():
    with sr.Microphone() as source:
        print("请说话...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("识别中...")
        text = recognizer.recognize_sphinx(audio, language='zh-CN')
        print("你说：", text)
        return text
    except sr.UnknownValueError:
        print("无法识别输入，请重试。")
        return ""
    except sr.RequestError as e:
        print("无法请求结果； {0}".format(e))
        return ""

if __name__ == "__main__":
    while True:
        user_input = listen()
        if user_input.lower() == "退出":
            print("再见！")
            break
        else:
            print("你说的是：" + user_input)
