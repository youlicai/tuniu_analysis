import urllib.request,re,time,random,gzip
import urllib
import socket
from ippool import IPPool
from log import Log

class NetWorkAccess:

	# 获取user-anget
	def get_user_agent():
		user_agent=['Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
					'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
					'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
					'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
					'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
					'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
					'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
					'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
					'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
					'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
					'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
					'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
					'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
					'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
					'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
					'Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13',
					'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10',
					'MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
					'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
					'Mozilla/5.0 (Androdi; Linux armv7l; rv:5.0) Gecko/ Firefox/5.0 fennec/5.0',
					'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
					'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
					'Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; m1 metal Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36',
					'Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Redmi 3X Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.2 Mobile Safari/537.36'
	    			]
		return user_agent[random.randint(0,len(user_agent)-1)]
	# 访问延迟时间（s）
	def get_request_time():
		return random.randint(15,30)

	# 发起访问
	def network_access_proxy(url):
		timeout = 6
		socket.setdefaulttimeout(timeout)

		proxy={'http':IPPool.getip()}
		#创建ProxyHandler
		proxy_support = urllib.request.ProxyHandler(proxy)
		#创建Opener
		opener = urllib.request.build_opener(proxy_support)
		#添加User Angent
		opener.addheaders = [('User-Agent',NetWorkAccess.get_user_agent())]
		#安装OPener
		urllib.request.install_opener(opener)

		try:
			req=urllib.request.Request(url)
			res = urllib.request.urlopen(req)
			# print(res.read())
			return res.read()
		except Exception as e:
			print(proxy['http']+"出现问题")
			Log.save_log2('error_url',url)
		return b''


	def network_access(url):
		try:
			req=urllib.request.Request(url)
			req.add_header('User-Agent',NetWorkAccess.get_user_agent())
			res = urllib.request.urlopen(req)
			return res.read()
		except Exception as e:
			print("error")
		return None



