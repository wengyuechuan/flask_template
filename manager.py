from flask_cors import CORS
from gevent import pywsgi
from flask_template import create_app

app = create_app('develop')
CORS(app, supports_credentials=True)  # 解决跨域问题

if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 5000))
    server.serve_forever()