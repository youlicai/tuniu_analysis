import socket
import urllib.request,re,time,random,gzip
import urllib
import os

class IPPool:

	proxy_url='http://www.ip181.com/daili/1.html'
	ip_folder='files'
	ip_files='files/ips.txt'

	def getip():
		with open(IPPool.ip_files, 'r') as f:
			ips=f.readlines()
		f.close()
		ip=ips[random.randint(0,len(ips)-1)]
		print("在IP:"+ip+"访问")
		return ip

	def delete_ip():
		pass
		# with open('ip.txt','a',encoding='utf8') as f:
		# 	f.write(item+'\n')
		# 	f.close()

	# 生成ip名单
	def make_ippool(ips):
		for ip in ips:
			try:
				if IPPool.checkip(ip[0]+':'+ip[1])==True:
					if not os.path.exists(IPPool.ip_folder):
						os.makedirs(IPPool.ip_folder)
					with open(IPPool.ip_files,'a',encoding='utf8') as f:
						f.write(ip[0]+':'+ip[1]+'\n')
					f.close()
				# time.sleep(5)
			except Exception as e:
					print(e)		

	# 测试ip是否可用
	def checkip(ip):
		print("*******************checking  "+ip+"  ********************")
		timeout = 6
		socket.setdefaulttimeout(timeout)
		url='http://www.baidu.com'
		# print(proxy)
		proxy={'http':ip}
		#创建ProxyHandler
		proxy_support = urllib.request.ProxyHandler(proxy)
		#创建Opener
		opener = urllib.request.build_opener(proxy_support)
		#添加User Angent
		# opener.addheaders = [('User-Agent',NetWorkAccess.get_user_agent())]
		#安装OPener
		urllib.request.install_opener(opener)
		try:
			req=urllib.request.Request(url)
			res = urllib.request.urlopen(req)
			res.read()
			print(ip+" is OK")
			return True
		except Exception as e:
			print(ip+"is ERROR")
			return False
		return False

	def getipsources():
		url=IPPool.proxy_url
		try:
			req=urllib.request.Request(url)
			res = urllib.request.urlopen(req)
			data=res.read().decode('gbk')
			regular=r"<tr(?:[^>]*?)>[^<]*?<td>(.*?)<\/td>(?:[^<]*?<td>(.*?)<\/td>)"
			pattern = re.compile(regular, re.S)
			data=re.findall(pattern,data)
			IPPool.make_ippool(data)
			# print(data)
		except Exception as e:
			print(e)
		return None

# IPPool.getip()
# IPPool.getipsources()





