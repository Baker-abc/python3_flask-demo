from flask import Flask

app = Flask(__name__)


# 如果访问 /,返回 Index Page
@app.route('/')
def index():
    return 'Index Page'


# 如果访问 /hello，返回 Hello, World!
@app.route('/hello')
def hello():
    return 'Hello, World!'


@app.route('/user/<username>')
def show_user_profile(username):
    # 显示用户名
    return 'User {}'.format(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # 显示提交整型的用户"id"的结果，注意"int"是将输入的字符串形式转换为整型数据
    return 'Post {}'.format(post_id)


# 转换器的主要类型如下：
# 类型	含义
# string	默认的数据类型，接受没有任何斜杠“/”的字符串
# int	    接受整型
# float	    接受浮点类型
# path	    和 string 类似，但是接受斜杠“/”
# uuid	    只接受 uuid 字符串

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # 显示 /path/ 之后的路径名
    return 'Subpath {}'.format(subpath)


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


if __name__ == '__main__':
    app.env = 'development'
    # app.env = 'production'
    # 生产环境禁用debug
    app.debug = True
    app.run()
