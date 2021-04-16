#!/usr/bin/python3
 
import sys
import socket
import queue
import threading
import time
 
q = queue.Queue()
 
class PorScanner(threading.Thread):
    def __init__(self,host):
        super().__init__()
        self.host = host
    def run(self) -> None:
        while True:
            port = q.get()
            self.scanner(port)
            q.task_done()
    def scanner(self,port):
        conn = socket.socket()
        try:
            conn.connect((self.host,port))
            print(f"[+] {port} is Open")
        except:
            pass
def main():
    if len(sys.argv) == 5:
        host = sys.argv[1]
        ip = socket.gethostbyname(host)
        startPort = sys.argv[2]
        endPort = sys.argv[3]
        threadNum = sys.argv[4]
        for i in range(int(threadNum)):
            t = PorScanner(ip)
            t.setDaemon(True)
            t.start()
        for i in range(int(startPort),int(endPort)):
            q.put(i)
        q.join() 
    else:
        print("Tips：python3 port_scan.py <ip> <port1> <port2> <thread>")
if __name__ == '__main__':
    try:
        main()
    except:
        pass
