import urllib.request,re,time,random,gzip
import urllib
import threading
import _thread
import os
from time import ctime,sleep
import socket
from network_access import NetWorkAccess
from spider import Spider

class TravelSpider:
	baseurl='http://s.tuniu.com/search_complex/whole-sh-0-'
	# 获得特定城市当前页码的旅游人数
	def  get_travel_amount(self,current_page,current_city):
		url=TravelSpider.baseurl+urllib.parse.quote(current_city)+'/'+current_page+'/'
		data=Spider.spider(url,r'<p class="person-num">[^<]*<i>(.*?)</i>')
		if data:
			# resp_data=resp_data.decode('utf-8')
			# regular=r'<p class="person-num">[^<]*<i>(.*?)</i>'
			# pattern = re.compile(regular, re.S)
			# data=re.findall(pattern,resp_data)
			# if len(data)>0:
			self.save_to_file(data,current_city)
			print("*******************开始打印"+current_city+"第"+current_page+"页数据*****************")
		else:
			print(current_city+" 第 "+current_page+" 页数据找不到数据")


	# 获得特定城市旅游产品页数
	def get_city_pages(self,city):
		url=self.baseurl+urllib.parse.quote(city)+'/'
		# resp_data=NetWorkAccess.network_access_proxy(url)
		data=Spider.spider(url,r'<span class="page-break" >[^>]*?>[^<]*<a href[^>]*>(.*?)</a>(?=<a href=[^=]*?class="page-next" >)')
		if data:
			# resp_data=resp_data.decode('utf-8')
			# regular=r'<span class="page-break" >[^>]*?>[^<]*<a href[^>]*>(.*?)</a>(?=<a href=[^=]*?class="page-next" >)'
			# pattern = re.compile(regular, re.S)
			# page=re.findall(pattern,resp_data)
			# if len(page)>0:
			# 	return page[0]
			# return 0
			return data[0]
		else:
			return 0


	# 获得所有旅游城市
	def get_totle_citys(self):
		url=self.baseurl+'%E4%B8%89%E4%BA%9A/'
		# resp_data=NetWorkAccess.network_access_proxy(url)
		# resp_data=resp_data.decode('utf-8')
		citys=Spider.spider(url,r'<input[\s\S]*?name="startcity"[\s\S]*?/>[^<]*?<a[^>]*>([^>]*?)</a>[^<]*?</li>')
		if citys:
			# regular=r'<input[\s\S]*?name="startcity"[\s\S]*?/>[^<]*?<a[^>]*>([^>]*?)</a>[^<]*?</li>'
			# pattern = re.compile(regular, re.S)
			# citys=re.findall(pattern,resp_data)
			print("总共有以下城市:【"+str(len(citys))+"】")
			print(citys)
			return citys
		return citys


	#获得某个城市总旅游人数
	def get_totle_travel_amount(self,total_pages,city):
		print("**************开始打印"+city+"数据*****************")
		for i in range(1,int(total_pages)):
			try:
				_thread.start_new_thread(self.get_travel_amount,(str(i),city,))
				# self.get_travel_amount,(str(i),city,)
				time.sleep(NetWorkAccess.get_request_time())
			except Exception as e:
				print(e)

	def save_to_file(self,data,city):
		with open('citys/'+city+'.txt','a',encoding='utf8') as f:
			for item in data:  
	   			f.write(item+'-')
		f.close()
		
	# 获得某个城市旅游人数
	def get_city_totle_peoples(self,city):
		try:
			f = open('citys/'+city+'.txt', 'r', encoding='utf-8')
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
				_thread.start_new_thread(self.thread_start,(city,))
				time.sleep(NetWorkAccess.get_request_time())
			except Exception as e:
				print(e)

	# 开线程
	def thread_start(self,city):
		pages=self.get_city_pages(city)
		self.get_totle_travel_amount(pages,city)




if __name__=="__main__":
	sp=TravelSpider()
	sp.start()
