from flask import Flask, request, make_response, render_template

app = Flask(__name__)


@app.route('/')
def index():
    resp = make_response(render_template('hello.html'))
    resp.set_cookie('username', 'the username')

    # 注意这里引用cookies字典的键值对是使用cookies.get(key)
    # 而不是cookies[key]，这是防止该字典不存在时报错"keyerror"
    print('username in cookie is {}'.format(request.cookies.get('username')))
    return resp


if __name__ == '__main__':
    app.env = 'development'
    # app.env = 'production'
    # 生产环境禁用debug
    app.debug = True
    app.run()
