from flask import Flask

app = Flask(__name__)


html ="""
<h1>Привет, меня зовут Михаил</h1>
<p>Я учусь в лобачевском<br>На 5 курсе</br></p>
"""

@app.route('/')
def index():
    return 'Hi'

@app.route('/text/')
def text():
    return html

@app.route('/poems/')
def poems():
    poem = ['Вот не думал,не гадал',
            'программистом взял и стал']
    txt ='<h1>Стихотворение<h1>\n<p>' + '<br/>'.join(poem) + '</p>'
    return txt












if __name__ == '__main__':
    app.run(debug=True)