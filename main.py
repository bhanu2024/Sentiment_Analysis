from flask import Flask, render_template, redirect, url_for, request
import requests


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():

    return render_template('index.html')


@app.route('/analysis', methods=['POST', 'GET'])
def analysis():
    text_data = request.form
    text = text_data['text']

    url = "https://b2chabreq3.execute-api.ap-south-1.amazonaws.com/Dev"

    payload = "{\"Text\": \" " + text + " \"}"
    headers = {
        'Content-Type': 'text/plain'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    analysis_data = response.json()
    print(analysis_data)
    # print(analysis_data['statusCode'])
    # print(analysis_data['Response'])
    return render_template('analysis_output.html', data=analysis_data)


if __name__ == "__main__":
    app.run(debug=True)

