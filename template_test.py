# -*- coding:utf-8 -*-
# __author__='chenliclchen'

from flask import Flask
from flask import request, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['BOOTSTRAP_SERVER_LOCAL'] = True
bootstrap = Bootstrap(app)


@app.route("/<name>", methods=['GET', 'POST'])
def home(name):
    return render_template("home.html", name=name)

# get请求，进入登陆页面
@app.route("/", methods=['GET'])
def login_form():
    return render_template("login.html")

# post请求，检查登陆信息跳转
@app.route("/login", methods=['POST'])
def login():
    name = request.form['name']
    password = request.form['password']
    if password.strip():
        return render_template("home.html", name=name, password=password)
    return render_template("login.html", message="wrong password", name=name)

# 测试bootstrap的使用
@app.route("/test", methods=['GET'])
def test_strap():
    name = request.args.get('name')
    print "name: ", name
    return render_template("test_strap.html")


if __name__ == "__main__":
    app.run()
