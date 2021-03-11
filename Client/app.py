from flask import Flask, render_template, request
import os
import requests
from run_client import predict
import json
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		input2 = request.form['input2']
		input4 = request.form['input4']
		input5 = request.form['input5']
		input6 = request.form['input6']
		input7 = request.form['input7']
		input8 = request.form['input8']
		input9 = request.form['input9']
		result = predict({'Country or region': input2, 'GDP per capita': input4, 'Social support': input5, 'Healthy life expectancy': input6, 'Freedom to make life choices': input7, 'Generosity': input8, 'Perceptions of corruption': input9})
		print(result)
		if float(result) == 1:
			result = "Most likely you are happy and live in a happy environment"
		else:
			result = "Keep strong, be happy"
	else:
		result = 'damn'
	return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
