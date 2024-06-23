from flask import Flask, render_template, request, redirect

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

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'GET':
        return render_template('add_book.html')
    else:
        title = request.form['title']
        author = request.form['author']
        d= {
            'title':title,
            'author':author
        }
        lst.append(d)
    return redirect('/books')


@app.route('/delete_book/<int:id>', methods=['POST', 'GET'])
def del_book(id):
    if request.method == 'GET':
        return render_template('del_book.html', book=lst[id])
    else:
        odp = request.form['odp']
        if odp == 'Tak':
            lst.pop(id)
        return redirect('/books')

@app.route('/update_book/<int:id>', methods=['POST', 'GET'])
def update_book(id):
    if request.method == 'GET':
        return render_template('add_book.html', book=lst[id])
    else:
        title = request.form['title']
        author = request.form['author']
        d = lst[id]
        d['title'] = title
        d['author'] = author
        return redirect('/books')

if __name__ == '__main__':
    app.run()
