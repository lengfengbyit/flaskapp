from app import db

# 创建多对多中间表
article_tag = db.Table('article_tag',
    db.Column('article_id',db.Integer, db.ForeignKey('article.id'), primary_key=True),
    db.Column('tag_id',db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)

class Article(db.Model):

    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    # 多对多关系映射
    # article.tags 访问文章关联的标签
    # tag.articles 访问标签关联的文章
    # secondary 定义中间表
    # db.backref 反向引用
    tags = db.relationship('Tag',secondary= article_tag,backref = db.backref('articles'))


class Tag(db.Model):

    __tablename__ = 'tag'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)

class Test(db.Model):
    """ 测试flask_migrate """
    __tablename__ = 'test'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(200), nullable=True)

# 这是用来创建数据表的语句
# db.create_all()