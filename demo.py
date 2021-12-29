from flask import Flask, render_template
app = Flask(__name__)
from data import posts


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
        app.run(debug = True)