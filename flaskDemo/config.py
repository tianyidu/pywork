
DEBUG=True
DIALECT = "mysql"
DRIVER = "pymysql"
USERNAME = "dev"
PASSWORD = "dev"
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "test"
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(
    DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False