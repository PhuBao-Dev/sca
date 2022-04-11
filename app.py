from flask import Flask, render_template, request, redirect, url_for
from checker import SpellChecker

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        username = request.form['username']
        checker = SpellChecker("./movies_text.txt")
        sen = username.split()
        rel = []
        for wo in sen:
            rel.append(checker.check(wo)[0][0])
        
        result = " ".join(rel)
        return render_template('index.html', result=result, getIn=username)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
