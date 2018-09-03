from flask_script import Manager
from app import app, db
from flask_migrate import Migrate, MigrateCommand
from app.models import Test

# falsk_script的命令管理功能
manage = Manager(app)

# 要使用Migrate，必须绑定app和db
migrate = Migrate(app, db)

# 将migrate的所有的命令(数据库相关)，添加的manager的db中
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()


# 接下来执行终端命令
# 1. python manage.py db init   初始化数据库迁移目录(migrations)
# 2. python manage.py db migrate 根据model生产数据库迁移文件
# 3. python manage.py db upgrade 执行数据迁移命令、数据库中生成对应的数据表