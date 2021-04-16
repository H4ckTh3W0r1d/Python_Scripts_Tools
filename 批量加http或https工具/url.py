import requests
import sys
import os
import random
from requests.packages.urllib3.exceptions import InsecureRequestWarning

#随机ua
def get_ua():
    first_num = random.randint(55, 62)
    third_num = random.randint(0, 3200)
    fourth_num = random.randint(0, 140)
    os_type = [
        '(Windows NT 6.1; WOW64)', '(Windows NT 10.0; WOW64)',
        '(Macintosh; Intel Mac OS X 10_12_6)'
    ]
    chrome_version = 'Chrome/{}.0.{}.{}'.format(first_num, third_num, fourth_num)

    ua = ' '.join(['Mozilla/5.0', random.choice(os_type), 'AppleWebKit/537.36',
                   '(KHTML, like Gecko)', chrome_version, 'Safari/537.36']
                  )
    return ua


def Scan(file_name):

    headers = {"User-Agent" : get_ua(),}
    with open(file_name, "r", encoding='utf8') as scan_url:
        for url in scan_url:
            if url[:4] != "http":
                url = "http://" + url
                url = url.strip('\n')
            try:
                requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                httpError = False
                try:
                    req = requests.get(url=url,headers=headers,verify=False,timeout=5)
                except Exception as e:
                    httpError = True
                if not httpError and req.status_code == 200:
                    print("\033[32m[+] 正在请求{} \033[0m".format(url))
                    with open(file_path, 'a', encoding='utf8') as res:
                        res.write(url+'\n')
                else:
                    url = url.replace("http","https")
                    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                    req = requests.get(url=url, headers=headers, verify=False, timeout=5)
                    if req.status_code == 200:
                        print("\033[32m[+] 正在请求{} \033[0m".format(url))
                        with open(file_path, 'a', encoding='utf8') as res:
                            res.write(url+'\n')
                    else:
                        pass
            except Exception as e:
                print("\033[31m[x] "+url+"访问失败 \033[0m".format(e))
                continue
if __name__ == '__main__':
    file_name = str(input("\033[35m Please input IP Address File\nFile >>> \033[0m"))
    file_path = os.getcwd()+"/result.txt"
    Scan(file_name)