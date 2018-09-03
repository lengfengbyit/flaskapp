
# 全局配置文件

import os

class Config(object):
    # session 配置，用于session加密, 需要是一个24位的字符串，可以使用os.urandome产生随机数
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)
    DEBUG = True

    # 数据库配置
    DIALECT = 'mysql'
    DRIVER = 'pymysql'
    USERNAME = 'root'
    PASSWORD = 'root'
    HOST = '127.0.0.1'
    PORT = 3306
    DATABASE = 'flaskapp'

    # 'mysql://root@localhost:3306/test?charset=utf8mb4'
    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = True
