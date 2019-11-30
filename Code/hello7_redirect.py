from flask import Flask
from flask import abort, redirect, url_for, render_template, make_response

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    abort(404)


@app.errorhandler(404)
def page_not_found(error):
    # return render_template('page_not_found.html'), 404

    resp = make_response(render_template('page_not_found.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp


if __name__ == '__main__':
    app.env = 'development'
    # app.env = 'production'
    # 生产环境禁用debug
    app.debug = True
    app.run()
