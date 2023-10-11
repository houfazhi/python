# 开发时间：2023/9/18 19:48
#文字转化为梅尔频谱音频再将音频输出
import zhtts
import sounddevice as sd

tts = zhtts.TTS()  # use fastspeech2 by default
text1 = "2020年，这是一个开源的端到端中文语音合成系统"

# 下面是自带的函数，借助Pycharm查看出来的。audio为numpy数组可直接传入播放器。
mel = tts.text2mel(text1)
print(mel.shape, type(mel))
audio = tts.mel2audio(mel)
print(audio, type(audio))
# 下面这里可以先看【6.sounddevice播放音频】
sd.play(audio, samplerate=24000) # samplerate=24000为通过其他包转换为.wav文件，再读取该文件获取的
sd.wait()
