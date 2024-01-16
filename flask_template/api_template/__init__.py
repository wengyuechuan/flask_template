from flask import Blueprint
from flask_restful import Api

# 创建蓝图对象
api_template_bp = Blueprint('api_template', __name__, url_prefix='/api_template')

# 创建Api对象
api_template_api = Api(api_template_bp)

from . import views
