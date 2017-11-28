class Log:

	print_log=True
	def save_log(log_content):
		with open('logs.txt','a',encoding='utf8') as f:
			f.write('['+log_content+']'+'\n')
		f.close()

	def save_log2(tag,log_content):
		with open('logs.txt','a',encoding='utf8') as f:
			f.write(tag+'['+log_content+']'+'\n')
		f.close()

	def show_log(str):
		if Log.print_log:
			print(str)