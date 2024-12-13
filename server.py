from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', data={}) 

@app.route('/dance')
def dance():
    return render_template('dance.html', data={}) 

@app.route('/music')
def music():
    return render_template('music.html', data={}) 

@app.route('/cited')
def cited():
    return render_template('cited.html', data={}) 

@app.route('/instruments')
def instruments():
    return render_template('instruments.html', data={})

@app.route('/quiz')
def quiz():
    return render_template('quiz.html', data={}) 

if __name__ == '__main__':
    app.run(debug=True, port=3000)
