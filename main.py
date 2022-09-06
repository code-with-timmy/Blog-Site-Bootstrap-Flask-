from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    blog_endpoint = "https://api.npoint.io/ae1c5b6c48f5a14d4a83"
    response = requests.get(blog_endpoint)
    data = response.json()
    return render_template("index.html", blogs_data=data)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/blog/<int:num>')
def get_blog(num):
    blog_endpoint = "https://api.npoint.io/ae1c5b6c48f5a14d4a83"
    response = requests.get(blog_endpoint)
    data = response.json()[num - 1]
    return render_template("post.html", new_post=data)


if __name__ == "__main__":
    app.run(debug=True)
