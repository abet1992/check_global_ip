import requests
import os
import sys
sys.path.append(os.getcwd())

from sendLineNotify import MyLineNotify

FILENAME = "current_ip.txt"

res = requests.get('https://ifconfig.me')
current_ip = res.text.strip()

msg = """
自宅のグローバルIPが変更になりました。
旧：{0}
新：{1}
以下対応を行ってください。
・sakuraVPSのホワイトリスト登録
・zabbixの確認
・各種FQDNの確認
"""

if not os.path.isfile(FILENAME):
    open(FILENAME,"w").write(current_ip)
    sys.exit(0)
else:
    
    log_ip = open(FILENAME,"r").read().strip()
    
    if log_ip != current_ip:
        MyLineNotify().sendMessage(msg.format(log_ip,current_ip))