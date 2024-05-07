from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

'''---- Home page ----'''
@app.route('/')
def home_page():
    return render_template('pharm.html')

'''---- Login page ----'''
@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/appointment')
def appointment_page():
    return render_template('appointment.html')

@app.route('/doctors')
def doctors_page():
    return render_template('doctors.html')

@app.route('/services')
def services_page():
    return render_template('services.html')

@app.route('/medicines')
def medicines_page():
    return render_template('medicines.html')

if __name__=="__main__":
    app.run(debug=True)