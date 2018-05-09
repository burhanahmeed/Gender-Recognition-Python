from flask import Flask, render_template, request
from PredictClass import PredictClass
from extract import extractimage
# import cv2

app = Flask(__name__)
app.config.update(
	# DEBUG=True,
	TEMPLATES_AUTO_RELOAD=True
	)
@app.route('/')
def hello():
	return render_template('index.html', text='result')

@app.route('/upload', methods=['POST'])
def processing():
	predictor = PredictClass()
	datasettxt = request.form['dataset']
	file = request.files['image']
	dataset = extractimage(file)
	if dataset==False:
		result='Wajah Tidak Terdeteksi'
	else:
		result = predictor.predict(*dataset)
	return render_template('index.html', text=result)
	