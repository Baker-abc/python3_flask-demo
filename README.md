# python3_flask_demo
## learning in windows

#### pip freeze >requirements.txt   这种方式配合virtualenv 才好使，否则把整个环境中的包都列出来了。
#### pipreqs ./ --encoding=utf8 --force   这个工具的好处是可以通过对项目目录的扫描，自动发现使用了那些类库，自动生成依赖清单。缺点是可能会有些偏差，需要检查并自己调整下。
#### pip install -r requirements.txt

#Code：test <br>
#flaskr： 简易demo <br>
##flaskr init <br>
$ python <br>
$ from flaskr import init_db <br>
$ init_db() <br>
