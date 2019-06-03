from flask import Flask, render_template, request
from wtforms import Form , SelectField
from MLHandler import sentiment
from wtforms.widgets import TextArea
from flask import jsonify

app = Flask(__name__)
    
@app.route('/', methods=['GET','POST'])
def home():
    return render_template('home.php')
	
@app.route('/process', methods=['POST'])
def process():
	def sentVal():
		rev = request.form['rev']
		lang = request.form['lang']
		if lang in ('swe', "dan", 'nor'):
			return sentiment(rev, lang)
		else:
			return "Unknown language"
        
	data = sentVal()
	return jsonify({'rev' : data})

if __name__=="__main__":
    app.run() #debug=True
