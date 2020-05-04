from flask import Flask, render_template, send_from_directory, url_for, request, redirect
import os
from database_handler import *


app = Flask(__name__)

 
@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:html_page_name>')
def html_page_selector(html_page_name=None):
    if html_page_name is not None:
        return render_template(html_page_name)
    else: 
        return render_template('index.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('./thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again!'

 