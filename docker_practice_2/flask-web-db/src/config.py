import os

mysql_config = {
	### local ### 
	# 'host' : os.getenv('MYSQL_HOST', 'localhost'), # localhost 대신 service name으로 간다  
	# 'pass': os.getenv('MYSQL_PASS', ''),

	### docker ### 
	'host': os.getenv('MYSQL_HOST', 'db:3306'), # localhost 대신 service name으로 간다  
	'pass': os.getenv('MYSQL_PASS', 'root'),

	### 공통 ### 
	'user': os.getenv('MYSQL_USER', 'root'),
	'db':   os.getenv('MYSQL_DB', 'test_db'),
}

def alchemy_uri():
	return 'mysql+pymysql://%s:%s@%s/%s?charset=utf8' % (
		mysql_config['user'], mysql_config['pass'], mysql_config['host'], mysql_config['db']
	)