import requests
import sys


def gpt35(ques):
    api_key = sys.argv[2]
    url = "https://api.openai-proxy.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": ques}]
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        ans = response.json()
        return ans['choices'][0]['message']['content']
    else:
        return "Error"


def getcsrf(login_cookie):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE',
        '_contentOnly': 'WoXiHuanFanQianXing',
        'x-luogu-type': 'content-only',
        'cookie': login_cookie,
        'x-requested-with': 'XMLHttpRequest',
    }
    res2 = requests.get("https://www.luogu.com.cn/", headers=headers)
    res2 = res2.text
    csrftoken = res2.split(
        "<meta name=\"csrf-token\" content=\"")[-1].split("\">")[0]
    return csrftoken


def postBenben(login_cookie, msg):
    csrf_token = getcsrf(login_cookie)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        '_contentOnly': 'WoXiHuanFanQianXing',
        'x-luogu-type': 'content-only',
        'cookie': login_cookie,
        'x-requested-with': 'XMLHttpRequest',
        'referer': 'https://www.luogu.com.cn/',
        'x-csrf-token': csrf_token,
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }
    data = {'content': msg}
    return requests.post(
        "https://www.luogu.com.cn/api/feed/postBenben", headers=headers, data=data).text


if __name__ == "__main__":
    ques = "Write an inspirational sentence"
    cookie = sys.argv[1]
    msg = gpt35(ques)
    postBenben(cookie, msg)
