from markupsafe import escape
from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
    return 'Введи путь к файлу в адресной строке'

@app.route('/<path:file>/')
# http://127.0.0.1:5000/<script>alert("I am haсker")</script>/
def get_file(file):
    print(file)
    #return f'Ваш файл находится в : {file}'
    return f'Ваш файл находится в : {escape(file)}'

if __name__ == '__main__':
    app.run(debug=True)
