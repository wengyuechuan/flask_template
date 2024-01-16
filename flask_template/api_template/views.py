from flask_restful import Resource
from flask_template.api_template import api_template_bp, api_template_api


# 创建蓝图对象
@api_template_bp.route('/', methods=['GET', 'POST'])
def index():
    return "Hello World!"


# 创建Api接口
class ApiTemplate(Resource):
    def get(self):
        return {"code": 200, "msg": "获取数据成功", "data": "get"}

    def post(self):
        return {"code": 200, "msg": "获取数据成功", "data": "post"}


api_template_api.add_resource(ApiTemplate, '/test/')
