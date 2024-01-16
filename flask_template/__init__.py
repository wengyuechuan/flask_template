from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config_map

db = SQLAlchemy()


# 创建一个函数，专门用来创建app
def create_app(config_name):
    # 创建一个Flask实例
    app = Flask(__name__)
    # 根据config_name获取配置类
    Config = config_map.get(config_name)
    # 根据类来加载配置信息
    app.config.from_object(Config)
    # 初始化db
    db.init_app(app)

    # 获取api_template蓝图对象
    from flask_template.api_template import api_template_bp
    # 注册蓝图
    app.register_blueprint(api_template_bp)

    return app
