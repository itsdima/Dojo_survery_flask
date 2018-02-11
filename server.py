from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
	if len(request.form['name']) < 1:
		flash('Name Cannot Be Empty!')
		return redirect('/')
	elif len(request.form['comment']) > 120:
		flash('Comment should be less than 120 characters!')
		return redirect('/')
	else:
		flash('Success! Your Name is {}'.format(request.form['name']))
	name = request.form['name']
	location = request.form['location']
	language = request.form['language']
	comment = request.form['comment']
	return render_template('result.html', name=name, location=location, language=language, comment=comment)
app.run(debug=True)