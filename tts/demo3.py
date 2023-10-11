# 开发时间：2023/9/18 19:31
import win32com.client
speaker =  win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak('你好，这是中文')