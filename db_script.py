from flask_script import Manager

DBManage = Manager()

@DBManage.command
def init():
    print('数据库初始化')

@DBManage.command
def create():
    print('创建数据库')