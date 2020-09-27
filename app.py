from flask import Flask
from flask import url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '欢迎'

@app.route('/whoami')
def whoami():
    return 'whoami'

@app.route('/users/<name>')
def user(name):
    return 'hello'+name

@app.route('/test_url_for')
def test():
    print(url_for('hello_world',num=2))
    print(url_for('user',name=u'张三'))
    return 'look at terminal!'


if __name__ == '__main__':
    app.run()
