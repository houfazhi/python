# 开发时间：2023/9/13 20:30
#tts实现语音播报
from gtts import gTTS
from playsound import playsound
import os
# filepath = "../file/a.txt"
# if os.path.exists(filepath):
#     with open(filepath,"r",encoding="UTF-8") as file:
#         lyric = file.read()
# else:
#     print("file not found")
#     exit()
with open("../file/a.txt", 'r', encoding='utf-8') as rfile:
    lyric = rfile.read()

if lyric:
    # lyric = "They say that life is always easier"
    # 创建gTTS对象
    tts = gTTS(text=lyric, lang='en', slow=False)

    # output_file = os.path.expanduser("~/Documents/lyric.mp3")
    output_file = "lyric.mp3"

    # 保存音频文件
    tts.save(output_file)

#    os.system("start " + output_file)
    os.system(output_file)
    # 播放音频文件
    # playsound(output_file)
else:
    print("lyric is empty")

