from flask import Flask, render_template
from controllers import posts as Posts
from datetime import datetime
from bs4 import BeautifulSoup

app = Flask(__name__)

# Filters

@app.template_filter('pretty_date')
def pretty_date_from_timestamp(timestamp):
	date = datetime.fromtimestamp(timestamp / 1000)

	return date.strftime('%B %-d %Y')

@app.template_filter('read_time')
def read_time_from_article(article):
	words = article["content"]["markdown"].split(" ")
	time = int(round(len(words) / 150))
	print time

	if time < 1:
		return "Less than a minute to read"
	elif time < 2:
		return "{} minute to read".format(int(round(time)))
	else:
		return "{} minutes to read".format(int(round(time)))

@app.template_filter('plain_text')
def get_plain_from_markdown(html):
	return ''.join(BeautifulSoup(html, "lxml").findAll(text=True))

@app.template_filter('first_bit')
def get_first_bit_of_string(string):
	return string[:140] + "..."

# Routes

@app.route("/")
def return_home():
	return render_template("index.html", posts=Posts.get(), about=Posts.get("56d8b29ed1befa0797463ad6"))

@app.route("/posts/")
def return_posts():
	return render_template("posts.html", posts=Posts.get())

@app.route("/posts/<_id>")
def return_post(_id):
	post = Posts.get(_id)

	if post:
		return render_template("post.html", post=Posts.get(_id))

	return return_home()

if __name__ == "__main__":
	app.run(debug=True, port=8000)
