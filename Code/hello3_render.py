from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):  # 默认 name 为 None
    return render_template('hello.html', name=name)  # 将 name 参数传递到模板变量中


@app.route('/hello2/<name>')
def hello2(name=None):  # 默认 name 为 None
    return render_template('hello2.html', name=name)  # 将 name 参数传递到模板变量中


if __name__ == '__main__':
    app.env = 'development'
    # app.env = 'production'
    # 生产环境禁用debug
    app.debug = True
    app.run()
