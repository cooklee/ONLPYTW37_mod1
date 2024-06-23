from flask import Flask, render_template, request

app = Flask(__name__)

lst = [
    {
        'title':'Pan Tadeusz',
        'author':'Adam Mickiewicz'
    },
    {
        'title':'Wyprawa',
        'author':'Jrr Tolkien'
    },
    {
        'title':'Dwie wieze',
        'author':'Jrr tolkien'
    },
    {
        'title':'Czas Pogardy',
        'author':'Andrzej Sapkowski'
    }

]
@app.route('/')
def hello_world():  # put application's code here
    return render_template('base.html')


@app.route("/przedstaw_sie", methods=['GET', 'POST'])
def p():
    if request.method == 'GET':
        return render_template('welcome_form.html')
    else:
        imie = request.form['imie']
        nazwisko = request.form['nazwisko']
        return render_template('show.html', first_name=imie, last_name=nazwisko)


@app.route('/books')
def books():
    return render_template('books.html', books=lst)


if __name__ == '__main__':
    app.run()
