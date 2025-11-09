from flask import Flask, render_template, request
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/')
def home():
    logging.info("Homepage accessed")
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    logging.info(f"Form submitted by: {username}")
    return f"<h2>Hello {username}</h2>"

if __name__ == '__main__':
    app.run(debug=True) 