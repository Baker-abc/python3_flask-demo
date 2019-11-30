from flask import Flask, flash
from flask import abort, redirect, url_for, render_template, make_response, session, escape, request

app = Flask(__name__)

app.secret_key = 'r\x88uSG\xac\x14\xa5\xdde\xb7\x88\xdf>\xcf\x92'


@app.route('/')
def index():
    return render_template('hello9_index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('hello9_login.html', error=error)


if __name__ == '__main__':
    app.env = 'development'
    # app.env = 'production'
    # 生产环境禁用debug
    app.debug = True
    app.run()
