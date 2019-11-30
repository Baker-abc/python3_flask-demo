from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        try:
            if valid_login(request.form['username'],
                           request.args.get('key', ''),
                           request.form['password']):
                return log_the_user_in(request.form['username'])
            else:
                error = 'Invalid username/password'
        except Exception as msg:
            error = msg

    # 当请求形式为“GET”或者认证失败则执行以下代码
    return render_template('login.html', error=error)


def valid_login(arg1, arg2, arg3):
    print(arg1)
    print(arg2)
    print(arg3)
    return True


def log_the_user_in(arg1):
    print(arg1)
    return "hello {}".format(arg1)


if __name__ == '__main__':
    app.env = 'development'
    # app.env = 'production'
    # 生产环境禁用debug
    app.debug = True
    app.run()
