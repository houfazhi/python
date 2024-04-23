# 开发时间：2024/2/17 13:19
# 与机器人对话：调用的是图灵机器人
import requests
import json

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
                    "street": "车公庄西大街"
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