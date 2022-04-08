from flask import Flask, render_template, request, redirect, url_for
from print import printText
from checker import SpellChecker

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        username = request.form['username']

        checker = SpellChecker("./movies_text.txt")
        result = checker.check(username)[0][0]
        # return (result)
        return render_template('index2.html', result=result)

    return render_template('index2.html')

if __name__ == "__main__":
    app.run(debug=True)
