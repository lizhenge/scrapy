import json
import redis 
import pymongo

def main():
	# 指定Redis数据库信息
	rediscli = redis.StrictRedis(host='192.168.133.31', port=6379, db=0)
	# 指定MongoDB数据库信息
	mongocli = pymongo.MongoClient(host='localhost', port=27017)

	# 创建数据库
	db = mongocli['busroute']

	# 创建表
	sheet = db['beijing_busroute']
	i = 1
	while True:
		source, data = rediscli.blpop(['busroute:items'])
		# print(json.loads(data.decode()).items())
		
		item = json.loads(data.decode())

		sheet.insert(item)
		print('第{}条数据保存成功'.format(i))
		i += 1 
if __name__ == '__main__':
	main()