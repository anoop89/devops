from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'first DevOps project'


if __name__ == '__main__':
    app.run()
