from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'andrew',
        'title':'blog post 1',
        'content' : 'first post content',
        'date_posted': '2018.4.20'
    },
    {
        'author':'jane',
        'title':'second post',
        'content':'second post content',
        'date_posted': '2018.4.21'
    }
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html',posts = posts,title = "HELLO")


@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
