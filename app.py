# importing modules from flask library
from flask import Flask, render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# define the route to father webpage
@app.route("/father")
def father():
    name = "Vikram"
    age = 60
    return render_template('father.html', name=name, age=age)

# define the route to son webpage
@app.route("/son")
def son():
    name = "Prabhanjan"
    age = 30
    return render_template('son.html', name=name, age=age)

# define the route to friend webpage
@app.route("/friend")
def friend():
    name = "Amar"
    age = 32
    return render_template('friend.html', name=name, age=age)

# run the file
if __name__ == '__main__':
    app.run(debug=True)
