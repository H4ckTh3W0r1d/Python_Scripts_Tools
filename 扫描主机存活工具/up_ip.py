# -*- coding: utf-8 -*-

import platform
import os
import threading
import time
import sys
 
def my_os():
    return platform.system()
#判断当前系统
def ping_ip(ip):
    if my_os() == 'Windows':
        p_w = 'n'
    elif my_os() == 'Linux':
        p_w = 'c'
    else:
        print('不支持此操作系统')
        sys.exit()
    output = os.popen('ping -%s 1 %s'%(p_w,ip)).readlines()
    for w in output:
        if str(w).upper().find('TTL')>=0:
            print(f"[+] {ip}")
            result = open('result.txt','a+')
            result.write(ip)
            result.write('\r')
            result.close()
#构造扫描ip段
def ping_all():
        f = open('./ip.txt','r')
        for i in f:
            add = (i.rstrip('\n'))
            threading._start_new_thread(ping_ip,(add,))
            time.sleep(0.03)
 
if __name__ == '__main__':
    try:
        ping_all()
    except:
        pass