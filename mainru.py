from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import random
from datetime import date
import datetime
from sqlalchemy import Column,Integer,String,Date 
import re
import http.client
import mimetypes
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

app = Flask(__name__)
app.secret_key = 'hello_world'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://webadmin:APIsgk43364@node4994-pp-gold.th.app.ruk-com.cloud:5432/pythonlogin'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

url="https://www.goldtraders.or.th/AvgPriceList.aspx"

def january():
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'html.parser')
    find_word = soup.find_all("table",{"id":"DetailPlace_MainGridView"},"tbody")
    for i in find_word:
        i=str(i).split('มกราคม')[1]
        i=str(i).split('</font>')[1]
        i=str(i).split('<td align="right"><font color="Black" face="Tahoma,Verdana" size="1">')[1]
        i=str(i).split(',')
        i=i[0]+i[1]
        return float(i)
def febuary():
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'html.parser')
    find_word = soup.find_all("table",{"id":"DetailPlace_MainGridView"},"tbody")
    for i in find_word:
        i=str(i).split('กุมภาพันธ์')[1]
        i=str(i).split('</font>')[1]
        i=str(i).split('<td align="right"><font color="Black" face="Tahoma,Verdana" size="1">')[1]
        i=str(i).split(',')
        i=i[0]+i[1]
        return float(i)
def march():
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'html.parser')
    find_word = soup.find_all("table",{"id":"DetailPlace_MainGridView"},"tbody")
    for i in find_word:
        i=str(i).split('มีนาคม')[1]
        i=str(i).split('</font>')[1]
        i=str(i).split('<td align="right"><font color="Black" face="Tahoma,Verdana" size="1">')[1]
        i=str(i).split(',')
        i=i[0]+i[1]
        return float(i)
def april():
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'html.parser')
    find_word = soup.find_all("table",{"id":"DetailPlace_MainGridView"},"tbody")
    for i in find_word:
        i=str(i).split('เมษายน')[1]
        i=str(i).split('</font>')[1]
        i=str(i).split('<td align="right"><font color="Black" face="Tahoma,Verdana" size="1">')[1]
        i=str(i).split(',')
        i=i[0]+i[1]
        return float(i)
def may():
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'html.parser')
    find_word = soup.find_all("table",{"id":"DetailPlace_MainGridView"},"tbody")
    for i in find_word:
        i=str(i).split('พฤษภาคม')[1]
        i=str(i).split('</font>')[1]
        i=str(i).split('<td align="right"><font color="Black" face="Tahoma,Verdana" size="1">')[1]
        i=str(i).split(',')
        i=i[0]+i[1]
        return float(i)
def june():
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'html.parser')
    find_word = soup.find_all("table",{"id":"DetailPlace_MainGridView"},"tbody")
    for i in find_word:
        i=str(i).split('มิถุนายน')[1]
        i=str(i).split('</font>')[1]
        i=str(i).split('<td align="right"><font color="Black" face="Tahoma,Verdana" size="1">')[1]
        i=str(i).split(',')
        i=i[0]+i[1]
        return float(i)
def july():
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'html.parser')
    find_word = soup.find_all("table",{"id":"DetailPlace_MainGridView"},"tbody")
    for i in find_word:
        i=str(i).split('กรกฎาคม')[1]
        i=str(i).split('</font>')[1]
        i=str(i).split('<td align="right"><font color="Black" face="Tahoma,Verdana" size="1">')[1]
        i=str(i).split(',')
        i=i[0]+i[1]
        return float(i)
def august():
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'html.parser')
    find_word = soup.find_all("table",{"id":"DetailPlace_MainGridView"},"tbody")
    for i in find_word:
        i=str(i).split('สิงหาคม')[1]
        i=str(i).split('</font>')[1]
        i=str(i).split('<td align="right"><font color="Black" face="Tahoma,Verdana" size="1">')[1]
        i=str(i).split(',')
        i=i[0]+i[1]
        return float(i)
def september():
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'html.parser')
    find_word = soup.find_all("table",{"id":"DetailPlace_MainGridView"},"tbody")
    for i in find_word:
        i=str(i).split('กันยายน')[1]
        i=str(i).split('</font>')[1]
        i=str(i).split('<td align="right"><font color="Black" face="Tahoma,Verdana" size="1">')[1]
        i=str(i).split(',')
        i=i[0]+i[1]
        return float(i)
def october():
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'html.parser')
    find_word = soup.find_all("table",{"id":"DetailPlace_MainGridView"},"tbody")
    for i in find_word:
        i=str(i).split('ตุลาคม')[1]
        i=str(i).split('</font>')[1]
        i=str(i).split('<td align="right"><font color="Black" face="Tahoma,Verdana" size="1">')[1]
        i=str(i).split(',')
        i=i[0]+i[1]
        return float(i)

month=[]

month.append(january())
month.append(febuary())
month.append(march())
month.append(april())
month.append(may())
month.append(june())
month.append(july())
month.append(august())
month.append(september())
month.append(october())
#month.append
#month.append



cal1=(month[0]+month[1]+month[2]+month[3]+month[4]+month[5]+month[6]+month[7]+month[8]+month[9])/len(month)
fortune = '%.2f'%(cal1 - month[-1])
cal='%.2f' %cal1
Result = []
if float(fortune) < 0 :
    prop = '.ราคาทองทีโอกาศที่จะลง.'
elif float(fortune) > 0   :
    prop= '.ราคาทองทีโอกาศที่จะขึ้น. '
else:
    prop=' .ราคาทองคงที่ .'
Result.append(prop)
Result1=Result[0].split('.')






plt.figure(figsize=(12,6))
left = [1, 2, 3, 4, 5,6,7,8,9,10] 
  
height = month
  
tick_label = ['january','febuary','march','april','may','june','july','august','september','october'] 

plt.bar(left, height, tick_label = tick_label,
        width = 0.2,align='edge', color = ['blue']) 
  

plt.title('Gold chart!') 

plt.savefig('pythonlogin\static\images\my_plot8.png')


rateusd=[]
response = requests.get('https://api.exchangeratesapi.io/latest?base=THB')
exchange_rates= eval(response.text)["rates"]

for i in month:
    ex='%.2f' %(exchange_rates["USD"]*i)
    rateusd.append(ex)
rateusd =[float(i) for i in rateusd]
cal2 = (rateusd[0]+rateusd[1]+rateusd[2]+rateusd[3]+rateusd[4]+rateusd[5]+rateusd[6]+rateusd[7]+rateusd[8]+rateusd[9])/(len(rateusd))
fortune1 = '%.2f'%(cal2 - rateusd[-1])
cal3='%.2f' %cal2


plt.figure(figsize=(12,6))
left = [1, 2, 3, 4, 5,6,7,8,9,10] 
  
height = rateusd
  
tick_label = ['january','febuary','march','april','may','june','july','august','september','october'] 

plt.bar(left, height, tick_label = tick_label,
        width = 0.2,align='edge', color = ['blue']) 
  

plt.title('Gold chart!') 

plt.savefig('pythonlogin\static\images\my_plot3.png')







@app.route('/', methods=['GET', 'POST'])
def login():
    msg = ''
    user_id = 0
    email = ""
    newpass =""
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        connection = psycopg2.connect(user="webadmin",
                                    password="APIsgk43364",
                                    host="node4994-pp-gold.th.app.ruk-com.cloud",
                                    port="5432",
                                    database="pythonlogin")
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        account = cursor.fetchall()
        for row in account:
            user_id += row[0]
            email += row[3]

        if account:
            session['loggedin'] = True
            session['user_id'] = user_id
            #session['username'] = account['username']
            for i in password:
                i = '*'
                newpass += i
            session['password'] = newpass
            session['username'] = username
            session['email'] = email
            return redirect(url_for('home'))
        else:
            msg = 'Incorrect username/password!'
    return render_template('index.html', msg=msg)

@app.route('/pythonlogin/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/pythonlogin/register', methods=['GET', 'POST'])
def register():
    msg = ''

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form and 'confirm_password' in request.form:
        
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        email = request.form['email']
        connection = psycopg2.connect(user="webadmin",
                                    password="APIsgk43364",
                                    host="node4994-pp-gold.th.app.ruk-com.cloud",
                                    port="5432",
                                    database="pythonlogin")
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif password != confirm_password:
            msg ='Please Enter Confirm Password like Password.'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            postgres_insert_query = """ INSERT INTO accounts (username, password, email) VALUES (%s,%s,%s)"""
            cursor.execute(postgres_insert_query,(username,password,email))
            connection.commit()
            msg="Register Successfully"
    elif request.method == 'POST':
        msg = 'Please fill out the form!'
    return render_template('register.html', msg=msg)

@app.route('/pythonlogin/home', methods=['GET', 'POST'])
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        
        return render_template('home.html', username=session['username'],prophecy=Result1[1],oct=month[-1],sep=month[-2],aug=month[-3],jul=month[-4],jun=month[-5],may=month[-6],apr=month[-7],mar=month[-8],feb=month[-9],jan=month[-10])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

@app.route('/pythonlogin/profile')
def profile():
    if 'loggedin' in session:
        return render_template('profile.html', account=session)
    return redirect(url_for('login'))

@app.route('/pythonlogin/usd')
def usd():
    return render_template('usd.html',prophecy=Result1[1],calcu1=cal3,octusd=rateusd[-1],sepusd=rateusd[-2],augusd=rateusd[-3],julusd=rateusd[-4],junusd=rateusd[-5],mayusd=rateusd[-6],aprusd=rateusd[-7],marusd=rateusd[-8],febusd=rateusd[-9],janusd=rateusd[-10]) 

@app.route('/pythonlogin/result')
def result():
    connection = psycopg2.connect(user="webadmin",
                                    password="APIsgk43364",
                                    host="node4994-pp-gold.th.app.ruk-com.cloud",
                                    port="5432",
                                    database="pythonlogin")
    cur = connection.cursor()
    cur.execute("select month,resultja FROM result")
    rows = cur.fetchall()
    return render_template('result.html',data=rows,prophecy=Result1[1])

if __name__ == '__main__' :
    app.run(debug=True,host="0.0.0.0")

