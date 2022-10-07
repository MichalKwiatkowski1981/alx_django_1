import flask

app = flask.Flask('moja apka')

@app.route('/dodaj/<int:x>/<int:y>')
def generuj (x, y):
    return {
        'wynik': x + y
    }

if __name__ == '__main__':
    app.run(debug=True)

