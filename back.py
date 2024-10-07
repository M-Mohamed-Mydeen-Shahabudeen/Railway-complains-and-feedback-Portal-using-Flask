from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['railway_portal']
complaints_collection = db['complaints']
feedback_collection = db['feedback']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/complaint', methods=['GET', 'POST'])
def complaint():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        complaint = request.form['complaint']
        complaints_collection.insert_one({'name': name, 'email': email, 'complaint': complaint})
        return redirect('/success')
    return render_template('complaint.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        feedback = request.form['feedback']
        feedback_collection.insert_one({'name': name, 'feedback': feedback})
        return redirect('/success')
    return render_template('feedback.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
