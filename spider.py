from network_access import NetWorkAccess
from log import Log
import re
class Spider:

	def spider(url,regular):
		data=[]
		try:
			resp_data=NetWorkAccess.network_access_proxy(url)
			# Log.show_log(resp_data)
			if resp_data:
				resp_data=resp_data.decode('utf-8')
				pattern = re.compile(regular, re.S)
				data=re.findall(pattern,resp_data)
			return data
		except Exception as e:
			Log.show_log(e)
			Log.save_log('error')
		return data
		
