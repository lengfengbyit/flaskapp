from flask import session
from app import app

@app.route('/sess/set')
def sess_set():
    """ session 测试 """

    session['username'] = '张三'
    session['age'] = 20
    return session['username']

@app.route('/sess/get')
def sess_get():

    return session.get('username', '用户名不存在')

@app.route('/sess/del')
def sess_del():
    print(session.get('username'))
    session.pop('username')
    print(session.get('username'))

    return '删除成功'

@app.route('/sess/clear')
def sess_clear():
    """ 清除session中所有的值 """

    print(session.get('username'))
    session.clear()
    print(session.get('username'))

    return '清除成功'