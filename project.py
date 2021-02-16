from flask import Flask,render_template,request,url_for,redirect,session
import sqlite3

conn = sqlite3.connect('user.db')
cursor = conn.cursor()
command1 = """CREATE TABLE IF NOT EXISTS
user(email TEXT,password TEXT)"""
cursor.execute(command1)
conn.close()
app=Flask(__name__)
app.secret_key="Xysdndvudsls"
@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method=='GET':
        conn = sqlite3.connect('user.db')
        cursor = conn.cursor()
        email1=request.form.get('email')
        password=request.form.get('password')
        session['email']=email1
        session['password']=password
        cursor.execute("INSERT INTO user VALUES('email1','password')")
        conn.commit()
        return redirect(url_for('dashboard'))
    return render_template('signup.html')
@app.route('/signin',methods=['POST','GET'])
def signin():
    if request.method=='post':
        conn = sqlite3.connect('user.db')
        cursor = conn.cursor()
        email1=request.form.get('email')
        password=request.form.get('password')
        cursor.execute("SELECT password from user WHERE email=email1")
        result=cursor.fetchall()
        '''if(result==password):
            session['email']=email1
            session['password']=password
            return redirect(url_for('dashboard')'''
        conn.close()
    return render_template('signin.html')
@app.route('/dashboard')
def dashboard():
    '''email1=session['email']
    password=session['password']
    if email1 is None:
        return redirect(url_for('signin'))
    email1=request.form.post('email')
    password=request.form.post('password')'''
    print(session[email1])
    print(session[password])
    return render_template('dashboard.html')
if __name__=='__main__':
    app.run(debug=True)
