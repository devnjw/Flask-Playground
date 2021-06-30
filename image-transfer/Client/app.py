from flask import Flask, render_template, request, jsonify
import json
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/image', methods=['POST'])
def image_upload():
    file = request.files['file']

    url = "http://127.0.0.1:5050/post/"
    files = {'file': file}
    res = requests.post(url, files=files).json()

    return render_template('result.html', data=res['data'])

if __name__ == '__main__':
    app.run(debug=True)