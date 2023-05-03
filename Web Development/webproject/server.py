from flask import Flask, render_template, url_for, request, redirect
import smtplib 
from email.message import EmailMessage

app = Flask(__name__)

@app.route("/")
def IndexView():
    return render_template('index.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
            
        return redirect('/')
    else:
        return 'Something wrong!'