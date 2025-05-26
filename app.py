
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dash1():
    return render_template('dash1.html')

@app.route('/dash')
def dash2():
    return render_template('dash2.html')

if __name__ == '__main__':
     app.run(debug=False)
