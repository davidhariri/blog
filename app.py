from flask import Flask, render_template
from controllers import posts as Posts
from datetime import datetime

app = Flask(__name__)

@app.template_filter('pretty_date')
def pretty_date_from_timestamp(timestamp):
	date = datetime.fromtimestamp(timestamp / 1000)

	return date.strftime('%B %-d %Y')

@app.template_filter('read_time')
def read_time_from_article(article):
	words = article["content"]["markdown"].split(" ")
	time = len(words) / 150

	if time < 1:
		return "Less than a minute"
	elif time > 1 and time < 1.5:
		return "{} minute".format(int(round(time)))
	else:
		return "{} minutes".format(int(round(time)))

@app.route("/")
def return_home():
	return render_template("home.html", posts=Posts.get())

@app.route("/posts/")
def return_posts():
	return render_template("all_posts.html", posts=Posts.get())

@app.route("/posts/<_id>")
def return_post(_id):
	return render_template("single_post.html", post=Posts.get(_id))

if __name__ == "__main__":
	app.run(debug=True, port=8000)
