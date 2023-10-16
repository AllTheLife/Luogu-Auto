import requests
import json
import sys


def post_benben(cookie, content="test"):
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://www.luogu.com.cn",
        "Referer": "https://www.luogu.com.cn/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46",
        "Cookie": cookie
    }

    data = {
        "content": content
    }

    return requests.post('https://www.luogu.com.cn/api/feed/postBenben', headers=headers, data=data).text


if __name__ == "__main__":
    print(f"Script Name: {sys.argv[0]}")
    for i in range(1, len(sys.argv)):
        response = post_benben(sys.argv[i])
        print(f"No. {i}: {response}")
        try:
            tmp = json.loads(response)
            if tmp['code'] == 200:
                print('code =', tmp['code'], 'message =', tmp['more']['html'])
            else:
                print('code =', tmp['code'], 'message =', tmp['message'])
        except Exception as err:
            print(f"<{err}>")
