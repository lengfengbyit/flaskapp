from flask import render_template, flash, redirect, url_for
from app import app, db
from app.models import Article

@app.route('/article/list')
def article_list():

    artlist = Article.query.all()
    print(artlist)
    return render_template('article/index.html', artlist=artlist)

@app.route('/article/info/<id>')
def article_info(id):
    info = Article.query.filter_by(id=id).first_or_404()
    return Article.get_debug_queries()
    return '%s: %s' % (info.title, info.content)

@app.route('/article/add')
def article_add():

    art = Article(title="这是一个标题2", content="这是文章内容2")
    art2 = Article(title="这是标题3", content="这是内容3")
    # 将数据保存到数据库中
    db.session.add(art)
    db.session.add(art2)
    db.session.commit()
    return '返回值：%s' % art.id
