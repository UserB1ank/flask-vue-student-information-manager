import datetime
import functools
import json
import os

from flask import Flask, request, g

from flask_cors import CORS
from model import db, User, Student
from sql_connect import *
import jwt
from jwt import exceptions

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"

# 数据库

db.init_app(app)

# 用户对象


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
        if g.payload['ip'] != request.remote_addr:  # 验证ip，防止cookie窃取
            return 3
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
            print(e)
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


@app.route('/query', methods=['POST'])
@login_required
def query():
    student_id = request.form['ID']
    data = Student.query.filter_by(id=student_id).first()
    data_dict = {"ID": data.id, "name": data.name, "gender": data.gender, "major": data.major, "phone": data.phone}
    return {'code': 200, 'message': '查询成功', "data": data_dict}


@app.route('/add', methods=['POST'])
@login_required
def add():
    # 从token获取当前管理员的用户名，查询id，设置user_id
    username = g.payload['username']
    user_id = User.query.filter_by(username=username).first().id
    # 设置其它字段
    ID = request.form['id']
    name = request.form['name']
    gender = request.form['gender']
    major = request.form['major']
    phone = request.form['phone']
    student = Student(id=ID, name=name, gender=gender, major=major, phone=phone, user_id=user_id)
    db.session.add(student)
    db.session.commit()
    return {"code": 200, "message": "增加成功"}


@app.route('/update', methods=['POST'])
@login_required
def update():
    """
    先获取原本的记录
    然后再修改
    :return: http_code message
    """
    # print(request.form)
    origin_id = request.form.get('backup_id')
    student = Student.query.filter_by(id=origin_id).first()
    # print(student)
    student.id = request.form.get('data_id')
    student.name = request.form.get('data_name')
    student.gender = request.form.get('data_gender')
    student.major = request.form.get('data_major')
    student.phone = request.form.get('data_phone')
    # print(student)
    db.session.commit()
    return {'code': 200, "message": "修改成功"}


@app.route('/delete', methods=['POST'])
@login_required
def delete():
    ID = request.form.get('ID')
    name = request.form.get('name')
    gender = request.form.get('gender')
    data = Student.query.filter_by(id=ID, name=name, gender=gender).first()
    db.session.delete(data)
    db.session.commit()
    return {'code': 200, 'message': '删除成功'}


@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    phone = request.form.get('phone')
    user = User(username=username, password=password, phone=phone)
    db.session.add(user)
    db.session.commit()
    return {"code": 200, "message": "注册成功"}


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


# 头像
@app.route('/avatar', methods=['POST', 'GET'])
@login_required
def avatar():
    """
    在数据库中保存头像路径，头像文件保存在前端
    post请求时为保存头像
    get请求时为返回头像路径
    做了文件后缀名白名单处理
    :return:
    """
    if request.method == 'POST':
        username = g.payload['username']
        user = User.query.filter_by(username=username).first()
        file = request.files['file']
        file_name = file.filename
        """
        文件后缀名白名单过滤
        """
        white_lst = ['.jpg', '.jpeg', '.png']
        file_ext = os.path.splitext(file_name)[-1]
        if file_ext.lower() in white_lst:
            # 删除老头像
            try:
                old_avatar_path = user.avatar_path
                if old_avatar_path is not None:
                    os.remove(old_avatar_path)
            except Exception as e:
                print(e)
            path = f'./static/avatar/{username}' + file_name
            file.save(path)
            user.avatar_path = path
            db.session.commit()
            # 返回头像地址
            path = str(path).lstrip('.')
            data = "http://127.0.0.1:5000" + path
            return {"code": 200, "message": "头像保存成功", "data": data}
        else:
            return {"code": 415, "message": "文件类型非法"}
    elif request.method == 'GET':
        username = g.payload['username']
        user = User.query.filter_by(username=username).first()
        path = user.avatar_path
        # ./static/avatar/123avatar.jpg
        path = str(path).lstrip('.')
        data = "http://127.0.0.1:5000" + path
        return {"code": 200, "message": "请求成功", "data": data}
    return {"code": 500, "message": "服务端出错"}


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
