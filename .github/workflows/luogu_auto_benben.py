name: 洛谷自动发犇

on:
  schedule:
    - cron: "00 22 * * *"
  workflow_dispatch:

jobs:
  Luogu_Auto_Punch:
    runs-on: windows-latest
    steps:
      - name: 下载发犇Python文件
        run: Invoke-WebRequest https://github.com/CodingOIer/Luogu-Auto/releases/download/Luogu-Auto-GPT-Benben/auto_luogu_gpt_benben.py -OutFile auto_luogu_gpt_benben.py
      - name: 安装库文件
        run: pip install requests
      - name: 运行发犇
        run: python .\auto_luogu_gpt_benben.py $Env:COOKIE $Env:GPT_KEY
        env:
          COOKIE: ${{ secrets.COOKIE }}
          GPT_KEY: ${{ secrets.GPT_KEY}}
