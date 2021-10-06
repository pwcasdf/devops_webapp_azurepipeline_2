from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return 'hello world!!!! v1'

if __name__ == '__main__':
    app.run('0.0.0.0','8080')