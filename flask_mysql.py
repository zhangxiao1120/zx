from flask import Flask,request,flash,url_for,redirect,render_template
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:password@localhost:3306/pymysql?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db=SQLAlchemy(app)

#数据模型
class students1(db.Model):
    id=db.Column('student_id',db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))

    def __ini__(self,name,city,addr,pin):
        self.name=name
        self.city=city
        self.addr=addr
        self.pin=pin

#创建或使用上述数据库
#db.create_all()
# @app.route('/')
# def show_all():
#     return render_template('show_all.html',student=students1.query.all())
#
# @app.route('/new')
# def new():
#     if not request.form['name'] or not request.form['city'] or not request.form['addr']:
#         flash('请填写完整','error')
#     else:
#         student=students1(request.form['name'],request.form['city'],
#                            request.form['addr'],request.form['pin'])
#
#         db.session.add(student)
#         db.session.commit()
#         flash('record was successfully added')
#         return redirect(url_for('show_all'))
#
#     return render_template('new.html')
# if __name__=='__main__':
#db.create_all()

#添加
# student1=students1(name='f',city='ss',addr='dd',pin='dd')
# db.session.add(student1)

#改
# 1. 先把你要更改的数据查找出来
# article1 = students1.query.filter(students1.id == 1).first()
# 2. 把这条数据，你需要修改的地方进行修改
# article1.name = 'new title'
# article1.city = 'bj'
# article1.addr = 'changping'
# article1.pin = 'new pin'

# 删
# 1. 把需要删除的数据查找出来
article1 = students1.query.filter(students1.id == 2).first()
# 2. 把这条数据删除掉
db.session.delete(article1)

db.session.commit()
#app.run(debug=True)