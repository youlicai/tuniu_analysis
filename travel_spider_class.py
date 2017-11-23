import urllib.request,re,time,random,gzip
import urllib
import threading
import _thread
import os
from time import ctime,sleep
import socket

class TravelSpider:
	baseurl='http://s.tuniu.com/search_complex/whole-sh-0-'
	# 获得特定城市当前页码的旅游人数
	def  get_travel_amount(self,current_page,current_city):
		url=TravelSpider.baseurl+urllib.parse.quote(current_city)+'/'+current_page+'/'
		req=urllib.request.Request(url,headers=self.getheaders())
		res = urllib.request.urlopen(req)
		before_data1=res.read()
		before_data=before_data1.decode('utf-8')
		regular=r'<p class="person-num">[^<]*<i>(.*?)</i>'
		pattern = re.compile(regular, re.S)
		data=re.findall(pattern,before_data)
		if len(data)>0:
			self.save_to_file(data,current_city)
		print(data)

	# 获得特定城市旅游产品页数
	def get_city_pages(self,city):
		url=self.baseurl+urllib.parse.quote(city)+'/'
		req=urllib.request.Request(url,headers=self.getheaders())
		res = urllib.request.urlopen(req)
		before_data1=res.read()
		# print(before_data1)
		before_data=before_data1.decode('utf-8')
		regular=r'<span class="page-break" >[^>]*?>[^<]*<a href[^>]*>(.*?)</a>(?=<a href=[^=]*?class="page-next" >)'
		pattern = re.compile(regular, re.S)
		page=re.findall(pattern,before_data)
		if len(page)>0:
			return page[0]
		return 0

	# 获得所有旅游城市
	def get_totle_citys(self):
		url=self.baseurl+'%E4%B8%89%E4%BA%9A/'
		req=urllib.request.Request(url)
		res = urllib.request.urlopen(req)
		before_data1=res.read()
		before_data=before_data1.decode('utf-8')
		# print(before_data1)
		regular=r'<input[\s\S]*?name="startcity"[\s\S]*?/>[^<]*?<a[^>]*>([^>]*?)</a>[^<]*?</li>'
		pattern = re.compile(regular, re.S)
		citys=re.findall(pattern,before_data)
		return citys

	#获得某个城市总旅游人数
	def get_totle_travel_amount(self,total_pages,city):
		for i in range(1,int(total_pages)):
			try:
				_thread.start_new_thread(self.get_travel_amount,(str(i),city,))
				time.sleep(20)
			except Exception as e:
				print(e)

	def save_to_file(self,data,city):
		with open(city+'.txt','a',encoding='utf8') as f:
			for item in data:  
	   			f.write(item+'-')
		f.close()
		
	# 获得某个城市旅游人数
	def get_city_totle_peoples(self,city):
		try:
			f = open(city+'.txt', 'r', encoding='utf-8')
			content=f.read()
			f.close()
			regular=r'([\d\w\.]+)-'
			pattern = re.compile(regular, re.S)
			people_nums=re.findall(pattern,content)
			sum=0
			for i in range(len(people_nums)):
				people_nums[i]=self.convert(people_nums[i])
				sum=sum+int(people_nums[i])
		except Exception as e:
			sum=0
		return sum

	# 万转换10000
	def convert(self,str):
		if '万' in str:
			str=str.replace('万','')
			str=float(str)*10000
		return str

	def getheaders(self):
		headers1 = {'Accept': '*/*',
	               'Accept-Language': 'en-US,en;q=0.8',
	               'Cache-Control': 'max-age=0',
	               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
	               'Connection': 'keep-alive',
	               'Referer': 'http://www.baidu.com/'
	               }
		headers2 = {'Accept': '*/*',
	               'Accept-Language': 'en-US,en;q=0.8',
	               'Cache-Control': 'max-age=0',
	               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
	               'Connection': 'keep-alive',
	               'Referer': 'http://www.csdn.com/'
	               }
		headers3 = {'Accept': '*/*',
	               'Accept-Language': 'en-US,en;q=0.8',
	               'Cache-Control': 'max-age=0',
	               'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) App leWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53',
	               'Connection': 'keep-alive',
	               'Referer': 'http://www.qq.com/'
	               }
		headers4 = {'Accept': '*/*',
	               'Accept-Language': 'en-US,en;q=0.8',
	               'Cache-Control': 'max-age=0',
	               'User-Agent': 'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
	               'Connection': 'keep-alive',
	               'Referer': 'http://www.taobao.com/'
	               }
		headers=[]
		headers.append(headers1)
		headers.append(headers2)
		headers.append(headers3)
		headers.append(headers4)
		return headers[random.randint(0, 3)]

	# 获取数据
	def get_data(self):
		citys=self.get_citys()
		a=[]
		for city in citys:
			d=dict()
			d["name"]=city
			d["value"]=self.sum(city)/5000
			a.append(d)
		return a

	# 开始爬取数据
	def start(self):
		citys=self.get_totle_citys()
		for city in citys:
			try:
				pages=self.get_city_pages(city)
				print("开始城市："+city+"【总共"+pages+"页】")
				self.get_totle_travel_amount(pages,city)
			except Exception as e:
				print(e)


if __name__=="__main__":
	sp=TravelSpider()
	sp.start()
