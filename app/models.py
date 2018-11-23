from datetime import datetime
from sqlalchemy import or_, and_
from app import db

class DB(db.Model):
    def save(self):
        db.session.add(self)
        db.session.commit()

# 用户表
class User(DB):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    usersn = db.Column()            # 用户编号
    password = db.Column()          # 密码
    firm_name = db.Column()         # 商户名称
    linkman = db.Column()           # 联系人
    tel = db.Column()               # 电话
    sub_bank = db.Column()          # 所属分行
    is_delete = db.Column()

# 权限管理
class auth(DB):
    __tablename__ = 'auth'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column()              # 权限名称
    url = db.Column()               # 权限url
    type = db.Column()              # 类型

# 角色管理
class role(DB):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column()           # 用户ID
    auth_ids = db.Column()          # 权限ID

# 商品表
class commodity(DB):
    __tablename__ = 'commodity'
    id = db.Column(db.Integer, primary_key=True)
    sn = db.Column()                # 商品编号
    brand = db.Column()             # 品牌
    primary_title = db.Column()     # 商品主标题
    sub_title = db.Column()         # 商品副标题
    category = db.Column()          # 商品分类
    is_import = db.Column()         # 是否进口
    origin = db.Column()            # 商品产地
    price = db.Column()             # 活动价格
    is_relief = db.Column()         # 是否扶贫商品
    logo = db.Column()              # 商品主图
    scene_logo = db.Column()        # 场景图
    png_logo = db.Column()          # png透明背景图
    is_delete = db.Column()         # 是否删除
    state = db.Column()             # 商品状态
    comment = db.Column()           # 评论
    store_num = db.Column()         # 库存
    out = db.Column()               # 已售
    is_apply = db.Column()          # 是否报名

# 专题表
class special(DB):
    __tablename__ = 'special'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column()              # 专题名称
    total_num = db.Column()         # 总名额
    applied_num = db.Column()       # 已报名
    start_time = db.Column()        # 开始时间
    end_time = db.Column()          # 结束时间
    state = db.Column()             # 场景状态
    is_delete = db.Column()

