from flask import Flask, render_template, request, flash, redirect, url_for, send_file
import requests
import os

app = Flask(__name__)
name = ""
uname = ""
sin = "&"
app.config['SECRET_KEY'] = 'this should be a secret random string'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/genrate', methods=['POST','GET'])
def gen():
    if request.method == 'POST':
        name = request.form.get('user_url')
        uname = request.form.get('ser')
        return render_template('index.html',name = name ,uname = uname)

@app.route('/day/', methods=['GET'])
def user_encode():
    message = request.args.get('name')
    un = request.args.get('uname')
    return render_template('card.html',name = message,uname = un)

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
