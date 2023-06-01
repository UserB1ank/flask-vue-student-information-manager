import datetime
import functools
import json

from flask import Flask, request, g
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


# 用户对象
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    username = db.Column(db.String(10), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(11), nullable=False)

    def __repr__(self):
        return "<User: %s, %s, %s, %s>" % (self.id, self.username, self.password, self.phone)


# 学生信息对象
class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.String(10), primary_key=True, nullable=False)
    name = db.Column(db.String(10), nullable=False)
    gender = db.Column(db.String(4), nullable=False)
    major = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(11), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    owner = db.relationship('User', backref=db.backref('posts', lazy='dynamic'))

    def __repr__(self):
        return "<User: %s, %s, %s, %s,%s>" % (self.id, self.name, self.gender, self.major, self.phone)


# 跨域
CORS(app)

# 构造header
headers = {
    'typ': 'JWT',
    'alg': 'HS256'
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
        g.payload = jwt.decode(token, secret, algorithms=['HS256'])
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
    g.payload = None
    if not token:
        g.status = 0
        return
    else:
        token = token.replace('token=', '')
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
                return {'code': 401, 'message': 'Invalid_Token'}
            elif g.status == 0:
                return {'code': 401, 'message': '未登录'}
            else:
                return f(*args, **kwargs)
        except BaseException as e:
            return {'code': 500, 'message': '服务端出错'}

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


@app.route('/register', methods=['POST'])
def register():
    return "nihao"
    pass


@app.route('/manager', methods=['GET'])
@login_required
def manager():
    userinfo = g.payload
    # print(userinfo)
    user = User.query.filter_by(username=userinfo['username']).first()
    # print(user)
    students = user.posts
    stu_data = list()
    stu = None
    for student in students:
        stu = {"id": student.id,
               "name": student.name,
               "gender": student.gender,
               "major": student.major,
               "phone": student.phone}
        stu_data.append(stu)
    return {"code": 200, "message": "登录成功", "data": stu_data}


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
