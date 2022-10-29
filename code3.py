#python program to demonstrate the errors using abort() in Flask.
#importing abort 
from flask import Flask,abort
#Initialize the flask application
app=Flask(__name__)
@app.route('/<uname>')
def index(uname):
    if uname[0].isdigit():
        abort(400)
    return '<h1>Good Username</h1>'

if __name__== '__main__':
    app.run()

#this code is contributed by Bhargav Katabathuni.
