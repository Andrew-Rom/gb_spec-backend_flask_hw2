import math

from flask import Flask, request, redirect, render_template, url_for, flash, session, make_response

app = Flask(__name__)
app.secret_key = b'2f5db05144a1008ad353eac6ffa199cb5112c9828735d4974ef930d091a94f0b'


@app.route('/')
@app.route('/index/')
@app.route('/index.html/')
def index():
    context = {'page_name': 'Главная'}
    return render_template('index.html', **context)


@app.route('/task5/', methods=['GET', 'POST'])
@app.route('/task5.html/', methods=['GET', 'POST'])
def task5_calc():
    if request.method == 'POST':
        n1 = request.form.get('num1', type=int)
        n2 = request.form.get('num2', type=int)
        operation = request.form.get('calc')
        match operation:
            case 'add':
                result = n1 + n2
            case 'subtract':
                result = n1 - n2
            case 'multiply':
                result = n1 * n2
            case 'divide':
                try:
                    result = n1 / n2
                except ZeroDivisionError:
                    result = 'Деление на ноль недопустимо'
            case _:
                return render_template('500.html')
        context = {'page_name': 'Задание № 5', 'calc_result': str(result)}
        return render_template('task5.html', **context)
    context = {'page_name': 'Задание № 5'}
    return render_template('task5.html', **context)


@app.route('/task6/', methods=['GET', 'POST'])
@app.route('/task6.html/', methods=['GET', 'POST'])
def task6():
    if request.method == 'POST':
        if not request.form['age']:
            flash('Возраст не указан', 'message-alert')
            return redirect(url_for('task6'))
        elif request.form.get('age', type=int) <= 0:
            flash('Возраст указан некорректно', 'message-alert')
            return redirect(url_for('task6'))
        flash('Возраст указан корректно', 'message-success')
        return redirect(url_for('task6'))
    return render_template('task6.html')


@app.route('/task7/', methods=['GET', 'POST'])
@app.route('/task7.html/', methods=['GET', 'POST'])
def task7():
    if request.method == 'POST':
        if not request.form['num']:
            flash('Число не указано', 'message-alert')
            return redirect(url_for('task7'))
        num = request.form.get('num', type=int)
        res = math.pow(num, 2)
        output = f'Квадрат числа {num} равен: {res}'
        return output
    return render_template('task7.html')

@app.route('/task8/', methods=['GET', 'POST'])
@app.route('/task8.html/', methods=['GET', 'POST'])
def task8():
    if request.method == 'POST':
        if request.form['name']:
            value = request.form.get('name')
            flash(f'Привет, {value}!')
            return redirect(url_for('task8'))
    return render_template('task8.html')


@app.route('/task9/', methods=['GET', 'POST'])
@app.route('/task9.html/', methods=['GET', 'POST'])
def task9_form():
    if request.method == 'POST':
        session['user_name'] = request.form.get('name')
        session['user_email'] = request.form.get('email')
        return redirect(url_for('task9_login'))
    return render_template('task9.html')


@app.route('/task9_login/', methods=['GET', 'POST'])
@app.route('/task9_login.html/', methods=['GET', 'POST'])
def task9_login():
    if 'user_name' in session and 'user_email' in session:
        context = {'msg': f"Hi, {session['user_name']} ({session['user_email']})"}
        response = make_response(render_template('task9_login.html', **context))
        return response
    return render_template('task9.html')

@app.route('/task9_logout/', methods=['GET', 'POST'])
def task9_logout():
    session.pop('user_name', None)
    session.pop('user_email', None)
    return redirect(url_for('task9_form'))


if __name__ == '__main__':
    app.run(debug=True)