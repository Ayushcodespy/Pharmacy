from flask import Flask, request, render_template
import pyodbc

app = Flask(__name__)

class ItemDatabase:
    def __init__(self):
        self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-F82IRCQF;DATABASE=flaskapp;')
        self.cursor = self.conn.cursor()

    def set_items(self, arg1, arg2, arg3):
        self.cursor.execute("INSERT INTO user_info(email, name, password) VALUES (?, ?, ?)",(arg1, arg2, arg3))
        self.conn.commit()
        

    def check_credentials(self, email, password):
        self.cursor.execute("SELECT * FROM user_info WHERE email=? AND password=?", (email, password))
        return self.cursor.fetchone() is not None

@app.route('/', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        email = request.form['name']
        password = request.form['password']

        db = ItemDatabase()
        if db.check_credentials(email, password):
            return render_template('index.html')
        else:
            message = "Incorrect email or password. Please try again."

    return render_template('login.html', message=message)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        try:
            db = ItemDatabase()
            db.set_items(email, name, password)
            return render_template('login.html')
        except Exception as e:
            return f"An error occurred: {str(e)}"

    return render_template('register.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/doctors')
def doctors():
    return render_template('/doctors.html')

@app.route('/medicines')
def medicines():
    return render_template('/medicines.html')


@app.route('/about')
def about():
    return render_template('/about.html')

if __name__ == '__main__':
    app.run(debug=True)
