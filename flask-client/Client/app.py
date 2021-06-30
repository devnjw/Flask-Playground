from flask import Flask, render_template, request, jsonify
import sys
import json
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/post', methods=['POST'])
def home_view():
    conv = [{'input': 'hi', 'topic': 'Greeting'}]
    s = json.dumps(conv)
    res = requests.post("http://127.0.0.1:5050/post/", json=s).json()
    print(res['data'])

    return render_template('result.html', data=res['data'])

if __name__ == '__main__':
    app.run(debug=True)