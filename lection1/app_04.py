from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/<name>/')
def hello(name='незнакомец'):
    return f'привет, {name.capitalize()}!'

@app.route('/file/<path:file>/')
def set_patn(file):
    print(type(file))
    return f'путь до файла {file}!'

@app.route('/number/<float:num>/')
def set_number(num):
    print(type(num))
    return f'переданное число  {num}!'



if __name__ == '__main__':
    app.run(debug=True)