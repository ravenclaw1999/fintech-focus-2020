# flask review
from flask import Flask
app = Flask(__name__)
from flask import render_template, request

# part 1 - basic routing
# @app.route('/')
# def index():
#     return "<h1>Hello puppy!</h1>"

@app.route('/information')
def info():
    return "<h1>Puppies are cute!</h1>"

# part 2 - dynamic routing
@app.route('/puppy/<name>')
def puppy(name):
    return f"<h1>This is a page for {name}</h1>"

# part 3 - templates
# @app.route('/')
# def index():
#     return render_template("basic.html")

# using the render_template function, 
# we can directly render an html file with our flask web app

# part 4 - template variable jinja{{}}

# @app.route('/')
# def index():
#     puppy_name = "Sam"
#     return render_template("basic.html", puppy_name=puppy_name)

# part 5 - template control flow in jinja
# loop
@app.route('/')
def index():
    my_list = [1, 2, 3, 4, 5]
    return render_template("index.html", my_list=my_list)

@app.route('/pupform')
def pupform():
    return render_template("form.html")

@app.route('/results', methods=["GET", "POST"])
def results():
    pup_name = request.form["name"] 
    # this will grab what the user entered for name 
    # and store it in a variable called pup_name
    return render_template("results.html", pup_name=pup_name)