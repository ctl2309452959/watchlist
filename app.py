import os
import sys

from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'  # 如果是windows操作系统，是三个斜杠
else:
    prefix = 'sqlite:////' # 如果是Mac，Linux，是四个斜杠

# 配置
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 关闭对模型修改的监控


@app.route('/')
def index():
    name = "Smart"
    movies = [
        {"title":"杀破狼", "year":"2003"},
        {"title":"扫毒", "year":"2018"},
        {"title":"捉妖记", "year":"2016"},
        {"title":"囧妈", "year":"2020"},
        {"title":"葫芦娃", "year":"1989"},
        {"title":"玻璃盒子", "year":"2020"},
        {"title":"调酒师", "year":"2020"},
        {"title":"釜山行", "year":"2017"},
        {"title":"导火索", "year":"2005"},
        {"title":"叶问", "year":"2015"},

    ]

    return render_template('index.html',name = name , movies = movies)

















app.run(host="127.0.0.1", port="3000")
