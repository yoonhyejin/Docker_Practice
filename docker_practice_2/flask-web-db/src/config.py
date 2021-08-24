import os

mysql_config = {
	# os.getenv 문법으로 바꾸자.
	# compose 파일에 environment 변수 지정 
	'host': os.getenv('MYSQL_HOST', 'db:3306'), # localhost 대신 service name으로 간다  
	#'host' : os.getenv('MYSQL_HOST', 'localhost'), # localhost 대신 service name으로 간다  
	'user': os.getenv('MYSQL_USER', 'root'),
	'pass': os.getenv('MYSQL_PASS', 'root'),
	#'pass': os.getenv('MYSQL_PASS', ''),
	'db':   os.getenv('MYSQL_DB', 'test_db'),
}

def alchemy_uri():
	return 'mysql+pymysql://%s:%s@%s/%s?charset=utf8' % (
		mysql_config['user'], mysql_config['pass'], mysql_config['host'], mysql_config['db']
	)