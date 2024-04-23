import os
import speech_recognition as sr
import pyttsx3


def my_record(rate=16000, max_attempts=3, record_seconds=5):
    r = sr.Recognizer()
    attempts = 0
    engine = pyttsx3.init()

    while attempts < max_attempts:
        with sr.Microphone(sample_rate=rate) as source:
            print("请说些什么")
            engine.say("请说些什么")
            engine.runAndWait()
            try:
                audio = r.listen(source, timeout=record_seconds)
                directory = "voices"
                if not os.path.exists(directory):
                    os.makedirs(directory)

                file_path = os.path.join(directory, "myvoices.wav")
                with open(file_path, "wb") as f:
                    f.write(audio.get_wav_data())
                print("录音完成！")
                engine.say("录音完成！")
                engine.runAndWait()
                return  # 录音成功，退出函数
            except sr.WaitTimeoutError:
                attempts += 1
                if attempts < max_attempts:
                    print(f"录音超时，尝试重新录音 ({attempts}/{max_attempts})")
                    engine.say("录音超时尝试重新录音")
                    engine.runAndWait()
                else:
                    print("录音超时，已达到最大尝试次数")
                    engine.say("录音超时，已达到最大尝试次数")
                    engine.runAndWait()

    print("无法录音，请检查麦克风设置或稍后重试")
    engine.say("无法录音，请检查麦克风设置或稍后重试")
    engine.runAndWait()


# if __name__ == '__main__':
#     my_record(record_seconds=5, max_attempts=3)  # 设置录音时长为5秒，最大尝试次数为3次
