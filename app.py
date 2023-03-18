#import database_functions as db
from flask import Flask, render_template, request
import requests





app = Flask(__name__)

@app.route('/')
def index():
    

    return render_template('index.html')

@app.route('/search', methods=['GET','POST'])
def search():
    if request.method == 'GET':
        input = request.args['fname']
    else:
        input = request.form['fname']
    
    response = requests.get(f'https://api.aviationstack.com/v1/airlines?access_key=42c1b498145ddb1f3d0c5d019f27e7b4')
    data = response.json()


    return render_template('arrivals.html' , data = data)


if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0')