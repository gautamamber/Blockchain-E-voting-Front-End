from flask import Flask , render_template, request, redirect, url_for
app = Flask(__name__)
@app.route('/')
def hello_world():
	return render_template("index.html")

@app.route('/voting_result')
def result():
	return render_template("result.html")

@app.route('/paper_work')
def work():
	return render_template("work.html")

@app.route('/do_vote')
def vote():
    return render_template('vote.html')

@app.route('/add_voters')
def add_voters():
	return render_template("add_voters.html")


if __name__ == '__main__':
	app.run(debug = True)