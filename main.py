import requests, json, re, os

session = requests.session()
email = os.environ.get('EMAIL')
passwd = os.environ.get('PASSWD')

GOTIFY_TOKEN = 'ALYjipELUpgTydf'
GOTIFY_URL = 'https://ysewsxzmhzws.us-east-1.clawcloudrun.com/message'  # 你的Gotify服务地址

def push(content):
    headers = {
        'X-Gotify-Key': GOTIFY_TOKEN,
        'Content-Type': 'application/json'
    }
    data = {
        "title": "ikuuu签到",
        "message": content,
        "priority": 5
    }
    resp = requests.post(GOTIFY_URL, headers=headers, data=json.dumps(data))
    if resp.status_code == 200:
        print("Gotify 推送成功")
    else:
        print(f"Gotify 推送失败: {resp.text}")

login_url = 'https://ikuuu.de/auth/login'
check_url = 'https://ikuuu.de/user/checkin'
info_url = 'https://ikuuu.de/user/profile'

header = {
    'origin': 'https://ikuuu.de',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
data = {
    'email': email,
    'passwd': passwd
}

try:
    print('进行登录...')
    response = session.post(url=login_url, headers=header, data=data).json()
    print(response['msg'])

    info_html = session.get(url=info_url, headers=header).text

    result = session.post(url=check_url, headers=header).json()
    print(result['msg'])
    content = result['msg']
    push(content)
except Exception as e:
    content = f'签到失败: {e}'
    print(content)
    push(content)

