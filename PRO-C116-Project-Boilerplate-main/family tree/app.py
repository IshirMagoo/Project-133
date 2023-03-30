# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/my_page")
def home():

    name = "Ishir" # write your name
    age = "13" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father_page")
def father():

    name = "Pankaj" # write your name
    age = "51" # write your age

    return render_template('father.html' , name = name , age = age)


# define the route to mother webpage
@app.route("/motherpage")
def mother():

    name = "Rashmi" # write your name
    age = "45" # write your age

    return render_template('mother.html' , name = name , age = age)


# define the route to friends webpage
@app.route("/friends_page")
def friend():

    name = "Saksham" # write your name
    age = "12" # write your age

    return render_template('friend.html' , name = name , age = age)


# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
