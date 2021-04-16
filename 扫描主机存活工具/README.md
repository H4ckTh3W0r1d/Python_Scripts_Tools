## 1.扫描存活主机

将要扫描的主机存在到同目录下的ip.txt中，

执行命令：

`python3 up_ip.py`

## 2.nmap扫描并导出结果

执行完毕后会将结果保存到result.txt中。

实用nmap扫描，并把结果导出到out.xml文件中。

`nmap -iL result.txt -F -oX out.xml`
