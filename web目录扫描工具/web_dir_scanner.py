import requests
import sys
import queue
import threading
import user_agent_list
import optparse
 
class DirScanMain:
	def __init__(self, options):
		self.url = options.url
		self.filename = options.filename
		self.count = options.thread
		
	class DirScan(threading.Thread):
		def __init__(self, queue,total):
			threading.Thread.__init__(self)
			self._queue = queue
			self._total = total
				
		def run(self):
			while not self._queue.empty():
				url = self._queue.get()
 
				threading.Thread(target=self.msg).start()
                #判断请求状态码，把结果输出到result.html
				try:
					r = requests.get(url=url, headers=user_agent_list.get_user_agent(), timeout=8,)
					if r.status_code == 200:
						sys.stdout.write('\r' + '[+]%s\t\t\n' % (url))
						result = open('result.html','a+')
						result.write('<a href="' + url + '" target="_blank">' + url + '</a>')
						result.write('\r\n</br>')
						result.close()
				except Exception as e:
					pass
        #显示扫描进度
		def msg(self):
			per = 100 - float(self._queue.qsize())/float(self._total) * 100
			percentage = "%s Finished| %s All| Scan in %1.f %s"%((self._total - self._queue.qsize()),self._total,per,'%')
			sys.stdout.write('\r'+'[*]'+percentage)
 
	def start(self):
		result = open('result.html','w')
		result.close()
		q = queue.Queue()
        #字典路径，字典放在当前目录的file目录中
		f = open('./file/%s'%self.filename,'r')
		for i in f:
			q.put(self.url+i.rstrip('\n'))
		total = q.qsize()
		threads = []
		thread_count = int(self.count)
		for i in range(thread_count):
			threads.append(self.DirScan(q,total))
		for i in threads:
			i.start()
		for i in threads:
			i.join()
 
if __name__ == '__main__':
	parser = optparse.OptionParser('python3 web_dir_scanner.py -u <URL> -f <file> -t <thread>')
	parser.add_option('-u',dest='url',type='string',help='target url for scan')
	parser.add_option('-f',dest='filename',type='string',help='dictionary filename')
	parser.add_option('-t',dest='thread',type='int',default=10,help='scan thread_count')
	(options,args)=parser.parse_args()
 
	if options.url and options.filename:
		dirscan = DirScanMain(options)
		dirscan.start()
		sys.exit(1)
	else:
		parser.print_help()
		sys.exit(1)
