from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
"""
@app.route('/', methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Add') == 'Add':
            # pass
            print("Sub")
        elif request.form.get('Sub') == 'Sub':
            # pass # do something else
            print("Sub")
        else:
            # pass # unknown
            return render_template("website.html")
    elif request.method == 'GET':
        # return render_template("index.html")
        print("No Post Back Call")
    return render_template("index.html")
"""

if __name__ == "__main__":
    app.run(debug=True)
