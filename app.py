# -*- coding: utf-8 -*-


from flask import Flask, render_template, request, flash, redirect,url_for, jsonify, session 
from flask import Response,send_file

app = Flask(__name__)

import aws_rds as rds

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/insert',methods = ['post'])
def insert():
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        bdate = request.form['bdate']
        btime = request.form['btime']
        rds.insert_details(name,email,phone,bdate,btime)
        details = rds.get_details()
        print(details)
        return render_template('index.html',details=details)



if __name__ == "__main__":
    
    app.run(host='0.0.0.0',port='80')