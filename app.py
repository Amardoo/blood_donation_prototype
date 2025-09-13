from flask import Flask, request, render_template
import sqlite3


app = Flask(__name__)


# Initialize SQLite database
def init_db():
   conn = sqlite3.connect('blood_donation.db')
   c = conn.cursor()
   # Donors table
   c.execute('''CREATE TABLE IF NOT EXISTS donors
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT, donor_id TEXT, age INTEGER,
                 hemoglobin REAL, blood_group TEXT, medical_history TEXT)''')
   # FMEA risks table
   c.execute('''CREATE TABLE IF NOT EXISTS fmea_risks
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 process_step TEXT, failure_mode TEXT,
                 severity INTEGER, occurrence INTEGER, detection INTEGER, rpn INTEGER)''')
   conn.commit()
   conn.close()


init_db()


# Home page
@app.route('/')
def index():
   return render_template('index.html')


# Donor registration
@app.route('/register', methods=['GET', 'POST'])
def register():
   import uuid
   if request.method == 'POST':
      name = request.form['name']
      donor_id = str(uuid.uuid4())[:8]  # Generate a short unique donor ID
      age = request.form['age']
      hemoglobin = request.form['hemoglobin']
      blood_group = request.form['blood_group']
      medical_history = request.form['medical_history']
      conn = sqlite3.connect('blood_donation.db')
      c = conn.cursor()
      c.execute("INSERT INTO donors (name, donor_id, age, hemoglobin, blood_group, medical_history) VALUES (?, ?, ?, ?, ?, ?)",
              (name, donor_id, age, hemoglobin, blood_group, medical_history))
      conn.commit()
      conn.close()
      return f"Registration successful! Donor ID: {donor_id} <a href='/view_donors'>View Donors</a>"
   return render_template('register.html')


# View all donors
@app.route('/view_donors')
def view_donors():
   conn = sqlite3.connect('blood_donation.db')
   c = conn.cursor()
   c.execute("SELECT * FROM donors")
   donors = c.fetchall()
   conn.close()
   return render_template('view_donors.html', donors=donors)


# FMEA risk calculator
@app.route('/fmea', methods=['GET', 'POST'])
def fmea():
   if request.method == 'POST':
       process_step = request.form['process_step']
       failure_mode = request.form['failure_mode']
       severity = int(request.form['severity'])
       occurrence = int(request.form['occurrence'])
       detection = int(request.form['detection'])
       rpn = severity * occurrence * detection
      
       conn = sqlite3.connect('blood_donation.db')
       c = conn.cursor()
       c.execute("INSERT INTO fmea_risks (process_step, failure_mode, severity, occurrence, detection, rpn) VALUES (?, ?, ?, ?, ?, ?)",
                 (process_step, failure_mode, severity, occurrence, detection, rpn))
       conn.commit()
       conn.close()
       return f"Risk logged! RPN: {rpn} <a href='/view_risks'>View Risks</a>"
   return render_template('fmea.html')


# View all FMEA risks
@app.route('/view_risks')
def view_risks():
   conn = sqlite3.connect('blood_donation.db')
   c = conn.cursor()
   c.execute("SELECT * FROM fmea_risks")
   risks = c.fetchall()
   conn.close()
   return render_template('view_risks.html', risks=risks)


if __name__ == '__main__':
   app.run(debug=True)

