from flask import Flask
from flask import abort, redirect, url_for, render_template, make_response, session, escape, request

app = Flask(__name__)

app.secret_key = 'r\x88uSG\xac\x14\xa5\xdde\xb7\x88\xdf>\xcf\x92'


@app.route('/')
def welcome():
    if 'username' in session:
        app.logger.debug('this debug log')
        app.logger.warning('this warning log')
        app.logger.error('this error log')
        return 'Logged in as %s' % escape(session['username'])
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


@app.route('/logout')
def logout():
    # 如果用户名存在，则从会话中移除该用户名
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/index')
def index():
    username = session.get('username')
    return render_template('index.html', username=username)


if __name__ == '__main__':
    app.env = 'development'
    # app.env = 'production'
    # 生产环境禁用debug
    app.debug = True
    app.run()
