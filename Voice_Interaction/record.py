# 开发时间：2024/2/17 12:53
import os
import speech_recognition as sr


# Use SpeechRecognition to record 使用语音识别包录制音频
def my_record(rate=16000):
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=rate) as source:
        print("请说些什么")
        audio = r.listen(source)

    directory = "voices"
    # 如果目录不存在，则创建目录
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_path = os.path.join(directory, "myvoices.wav")
    with open(file_path, "wb") as f:
        f.write(audio.get_wav_data())
    print("录音完成！")


if __name__ == '__main__':
    my_record()
