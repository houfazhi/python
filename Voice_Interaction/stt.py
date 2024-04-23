from aip import AipSpeech
import requests

APP_ID = '51777468'
API_KEY = 'xqegYUsSruduUouGVP5Udo8l'
SECRET_KEY = 'tVvfMAZ6o9E3AMqWvG9fsvVg0dGHRQnt'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
path = 'voices/myvoices.wav'


def get_access_token():
    url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={API_KEY}&client_secret={SECRET_KEY}"
    print("获取 access_token 的 URL:", url)
    response = requests.get(url)
    access_token = None
    if response.status_code == 200:
        access_token = response.json().get('access_token')
    return access_token


def GetSaying():
    try:
        # 获取 access_token
        access_token = get_access_token()
        if access_token:
            # 读取录音文件
            with open(path, 'rb') as fp:
                voices = fp.read()

            # 使用 access_token 进行语音识别
            result = client.asr(voices, 'wav', 16000,
                                {'dev_pid': 1536, 'cuid': 'baidu_speech_demo', 'token': access_token})

            if 'result' in result and result['result']:
                result_text = result["result"][0]
                print("识别结果: " + result_text)
                return result_text
            else:
                print("识别失败或未检测到语音")
                return None
        else:
            print("获取 access_token 失败")
            return None
    except Exception as e:
        print("百度语音识别出现异常:")
        print(e)
        return None


# if __name__ == '__main__':
#     GetSaying()
