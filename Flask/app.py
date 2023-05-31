import datetime
import functools

from flask import Flask, request, jsonify, current_app, g
from flask_cors import CORS
from flask_sqlalchemy import *
from sql_connect import *
import jwt
from jwt import exceptions

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"

# 数据库
db = SQLAlchemy()
db.init_app(app)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(10), unique=True)
    password = db.Column(db.String(20))
    phone = db.Column(db.String(11))

    def __repr__(self):
        return "<User: %s, %s, %s, %s>" % (self.id, self.username, self.password, self.phone)


# 测试是否连接成功
# with app.app_context():
#     with db.engine.connect() as conn:
#         rs = conn.execute("select 1")
#         print(rs.fetchone())  # (1,)


# 跨域
CORS(app)

# 构造header
headers = {
    'type': 'jwt',
    'algo': 'hs256'
}

# 秘钥
salt = 'python_cczu'
app.config['JWT_SECRET'] = salt


# jwt生成
def create_token(username, ip):
    payload = {
        'username': username,
        "ip": ip,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
    }
    result = jwt.encode(payload=payload, key=salt, algorithm='HS256', headers=headers)
    return result


# jwt验证
def verify_jwt(token, secret=None):
    """
    jwt验证
    返回解密后的内容则成功
    返回1，超时
    返回2，认证失败
    返回3，非法的token
    返回5，登录成功
    """
    if not secret:
        secret = app.config['JWT_SECRET']
    try:
        payload = jwt.decode(token, secret=secret, algorithms=['hs256'])
        return 5
    except exceptions.ExpiredSignatureError:
        return 1
    except jwt.DecodeError:
        return 2
    except jwt.InvalidTokenError:
        return 3


# 钩子
@app.before_request
def jwt_authentication():
    """
    获取请求中的token
    g.status 用于判断验证情况
    0，未登录
    1，超时
    2，认证失败
    3，非法的token
    5，登录成功
    """
    token = request.headers.get("Cookie")
    g.status = None
    if not token:
        g.status = 0
        return
    g.status = verify_jwt(token)
    return


# 装饰器函数
def login_required(f):
    """
    用于权限管理，当某个功能需要用户登录时使用
    确保登录后才能使用相应功能
    g.status 用于判断验证情况
    0，未登录
    1，超时
    2，认证失败
    3，非法的token
    :param f:
    :return:
    """

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        try:
            if g.status == 1:
                return {'code': 401, 'message': 'token已失效'}
            elif g.status == 2:
                return {'code': 401, 'message': 'token认证失败'}
            elif g.status == 3:
                return {'code': 401, 'message': '非法的token'}
            else:
                return f(*args, **kwargs)
        except BaseException as e:
            return {'code': 401, 'message': '请先登录认证.'}

    return wrapper


# api路由
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    ip = request.remote_addr
    users = User.query.filter_by(username=username, password=password).first()
    if users:
        token = create_token(username, ip)
        return {"code": 200, "message": "登录成功", "data": {"token": token}}
    else:
        return {"code": 501, "message": "登录失败"}


@login_required
@app.route('/register', methods=['POST'])
def register():
    return "nihao"
    pass


@app.route('/manager', methods=['GET'])
@login_required
def manager():
    return "success"


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
