from flask import Flask
from flask import request
import json

app = Flask(__name__) 

@app.route('/post/', methods = ['POST'])
def determine_escalation():
    jsondata = request.get_json()
    data = json.loads(jsondata)

    print("DATA: ")
    print(data)

    #stuff happens here that involves data to obtain a result

    result = {'data': True}
    return json.dumps(result)

if __name__ == '__main__':
    app.run(debug=True, port=5050)