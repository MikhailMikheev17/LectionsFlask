from flask import Flask, flash, redirect, render_template,request, url_for

app = Flask(__name__)

app.secret_key = b'32afa21381144811307a9791a911003d3cfd36415a809e8f58256555ffb79d22'

"""
Генерация надежного секретного ключа
>>> import secrets
>>> secrets.token_hex()
"""


@app.route('/')
def index():
    return 'Hi'

@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
    # Проверка данных формы
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))
        #Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('flash_form.html')


if __name__ == '__main__':
    app.run(debug=True)
    #app.run(debug=False) 