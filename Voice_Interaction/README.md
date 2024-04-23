Voice_Interaction封装功能介绍及调用说明：

1.tts(text) 

该函数实现文本转语音功能，text为输入参数

2.my_record(rate=16000, max_attempts=3, record_seconds=5) 


该函数实现录音功能，按照给的格式调用，之后调用下面给出的stt函数得到语音转文字的结果

3.GetSaying()

该函数实现将录音文件转化为文本，返回文本内容。

4.TalkToTuLing()

该函数实现智能语音对话交流等功能，直接按照给出的格式调用即可
