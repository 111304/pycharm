# app.py (更新后)
from flask import Flask
from config import Config
from models import db
from routes import configure_routes  # 新增导入
import os


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # 初始化数据库
    db.init_app(app)

    # 注册路由  # 新增代码
    configure_routes(app)

    # 创建上传目录
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)