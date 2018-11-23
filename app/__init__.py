from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import *
from datetime import timedelta
import os
import pymysql

# 创建app实例
app = Flask(__name__)

# 解决跨域
CORS(app, supports_credentials=True)

# 配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root!@#$@127.0.0.1:3306/erp'

# 移除数据库警告
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)

# 绑定app, 实例化db
db = SQLAlchemy(app)

