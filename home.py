import base64
import os

from datetime import date
from urllib import request

from werkzeug.utils import redirect, secure_filename

import pymysql
port = 587
smtp_server = "smtp.gmail.com"
sender_email = "serverkey2018@gmail.com"
password ="extazee2018"
from flask import Flask, render_template, flash, request, session, Response, url_for, send_from_directory, current_app, \
    send_file

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
conn = pymysql.connect(user='root', password='', host='localhost', database='python_secure_e_tender',charset='utf8')

@app.route("/")
def homepage():
    return render_template('index.html')
############################################################## ADMIN
@app.route("/admin")
def admin():
    return render_template('admin.html')
############################################################### FARMER
@app.route("/farmer")
def farmer():
    return render_template('farmer.html')

@app.route("/farmer_register")
def farmer_register():
    return render_template('farmer_register.html')

@app.route("/farmer_registeration",methods = ['GET', 'POST'])
def farmer_registeration():
    if request.method == 'POST':
        cname = request.form['name']
        contact = request.form['contact']
        email = request.form['email']
        address = request.form['address']
        dept = request.form['dept']

        username = request.form['username']
        password = request.form['password']

        if password==password:
            cursor = conn.cursor()
            cursor.execute("SELECT max(id)+1 FROM   manager_details")
            maxid = cursor.fetchone()[0]
            if maxid is None:
                maxid=1
            cursor = conn.cursor()
            cursor.execute("insert into manager_details values('"+str(maxid) + "','"+cname + "','"+contact+"','"+email+"','"+address+"','"+username+"','"+password+"','0','"+dept+"')")
            conn.commit()
        else:
            d=0
        return render_template('farmer_register.html')

    return render_template('farmer_register.html')
@app.route("/farmer_login",methods = ['GET', 'POST'])
def farmer_login():
    if request.method == 'POST':
        n = request.form['username']
        g = request.form['password']
        g1 = request.form['dept']
        n1=str(g)
        cursor = conn.cursor()
        cursor.execute("SELECT * from manager_details where username='" + n + "' and password='" + str(g) + "' and report='"+str(g1)+"'")
        data = cursor.fetchone()
        conn.commit()
       # cursor.close()
        if data is None:
            return 'Username or Password is wrong'
        else:
            session['uname'] =n
            #print(n)
            return render_template('farmer_home.html',sid=n)
    return render_template('farmer.html')
###########################################
@app.route("/farmer_home")
def farmer_home():
    return render_template('farmer_home.html')


@app.route("/farmer_new_product")
def farmer_new_product():
    return render_template('farmer_new_product.html')


@app.route("/farmer_new_product1",methods = ['GET', 'POST'])
def farmer_new_product1():
    if request.method == 'POST':
        today = date.today()
        cdate = today.strftime("%d-%m-%Y")

        uname =session['uname']
        product_name = request.form['product_name']
        category = request.form['category']
        quantity = request.form['quantity']
        price = request.form['price']
        gst = request.form['gst']
        description = request.form['description']

        if 'file' not in request.files:
            flash('No file Part')
            return redirect(request.url)
        file= request.files['file']
        print(file)
        f = request.files['file']
        f.save(os.path.join("static/uploads/", secure_filename(f.filename)))
        cursor = conn.cursor()
        cursor.execute("SELECT max(id)+1 FROM   tender_details")
        maxid = cursor.fetchone()[0]
        if maxid is None:
            maxid=1
        cursor1 = conn.cursor()
        cursor1.execute("insert into tender_details values('"+str(maxid) + "','"+str(uname)+"','"+product_name+"','"+category+"','"+quantity+"','"+price+"','"+gst+"','"+description+"','0','0','"+f.filename+"')")
        conn.commit()
        ###########################
        cursor2 = conn.cursor()
        cursor2.execute("select * from tender_details where manager='"+uname+"'")
    return render_template('farmer_new_product.html')
###############3
@app.route("/farmer_sales",methods = ['GET', 'POST'])
def farmer_sales():
    uname =session['uname']
    cursor2 = conn.cursor()
    cursor2.execute("select id,username,tender_name,department,duration,quotation_amount from quotation_details where manager='"+uname+"' and status='0'")
    return render_template('farmer_sales.html',items=cursor2.fetchall())

@app.route("/farmer_stock",methods = ['GET', 'POST'])
def farmer_stock():
    uname =session['uname']
    cursor2 = conn.cursor()
    cursor2.execute("select id,uname,product_name,category,quantity,price,gst from product_details where uname='"+uname+"'")
    return render_template('farmer_stock.html',items=cursor2.fetchall())

@app.route("/farmer_customer",methods = ['GET', 'POST'])
def farmer_customer():
    uname =session['uname']
    cursor2 = conn.cursor()
    cursor2.execute("select id,name,contact,email,address from customer_details")
    return render_template('farmer_customer.html',items=cursor2.fetchall())
@app.route("/customer_home")
def customer_home():
    return render_template('customer_home.html')
##### customer_search
@app.route("/customer_search")
def customer_search():
    cur = conn.cursor()
    cursor2 = conn.cursor()
    cursor2.execute("select id,manager,tender_name,department,amount,duration,last_date,description from tender_details")
    data=cursor2.fetchall()
    return render_template('customer_search.html',items=data)
########
@app.route('/customer_search1',methods = ['GET', 'POST'])
def customer_search1():
    if request.method == 'POST':
        cur = conn.cursor()
        product = request.form['product']
        cursor2 = conn.cursor()
        cursor2.execute("select * from tender_details")
        data=cursor2.fetchall()

        return render_template('customer_search.html', items=cursor2.fetchall())
############
@app.route('/customer_product_1',methods = ['GET', 'POST'])
def customer_product_1():
    if request.method == 'POST':
        cur = conn.cursor()
        product = request.form['product']
        cur.execute("SELECT id,uname,product_name,category,gst FROM product_details where product_name='"+product+"'")
        data = cur.fetchall()
        return render_template('customer_product.html', items=data)
######
@app.route('/student_college2/<string:filename>', methods=['GET','POST'])
def user_file_recei1(filename):
    data=[]
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tender_details where id='"+filename+"'")
    data=cursor.fetchall()
    session['id']=filename
    for x in data:
        print(x)
        a1=x

    d=(a1[0])
    return render_template('customer_product1.html', items=data)
################
@app.route('/customer_product_2',methods = ['GET', 'POST'])
def customer_product_2():
    if request.method == 'POST':
        cur = conn.cursor()
        q = request.form['textfield']
        session['qty']=q
        id=session['id']
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tender_details where id='"+id+"'")
        data=cursor.fetchall()

        cursor.execute("SELECT manager FROM tender_details where id='"+id+"'")
        price=cursor.fetchone()

        cursor.execute("SELECT tender_name FROM tender_details where id='"+id+"'")
        gst=cursor.fetchone()

        #total=int(price[0])+int(gst[0])
        total=q#total*int(q)

        return render_template('customer_product2.html',d1=data,q=q,total=total)
##################
@app.route('/customer_product_3',methods = ['GET', 'POST'])
def customer_product_3():
    if request.method == 'POST':
        cur = conn.cursor()
        q=session['qty']
        uname=session['uname']
        id=session['id']
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tender_details where id='"+id+"'")
        data=cursor.fetchone()

        cursor.execute("SELECT manager FROM tender_details where id='"+id+"'")
        uname1=cursor.fetchone()
        cursor.execute("SELECT tender_name FROM tender_details where id='"+id+"'")
        product_name=cursor.fetchone()
        cursor.execute("SELECT department FROM tender_details where id='"+id+"'")
        category=cursor.fetchone()
        cursor.execute("SELECT duration FROM tender_details where id='"+id+"'")
        price=cursor.fetchone()
        cursor.execute("SELECT filename FROM tender_details where id='"+id+"'")
        gst=cursor.fetchone()
        total=q#total*int(q)

        blockchain_data=str(uname)+""+str(uname1)+""+str(product_name)+""+str(category)+""+str(total)
        message_bytes = blockchain_data.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')

        print(base64_message)


        cursor = conn.cursor()
        cursor.execute("SELECT max(id)+1 FROM   quotation_details")
        maxid = cursor.fetchone()[0]
        if maxid is None:
            maxid=1
        cursor = conn.cursor()
        cursor.execute("insert into quotation_details values('"+str(maxid) + "','"+(uname) + "','"+product_name[0]+"','"+category[0]+"','"+str(price[0])+"','"+str(gst[0])+"','"+str(q)+"','"+str(total)+"','"+uname1[0]+"','0','0')")
        conn.commit()
        ##############333
        f = open("static/1/"+str(maxid)+".txt", "a")
        f.write(base64_message)
        f.close()

        f = open("static/2/"+str(maxid)+".txt", "a")
        f.write(base64_message)
        f.close()

        f = open("static/3/"+str(maxid)+".txt", "a")
        f.write(base64_message)
        f.close()

        f = open("static/4/"+str(maxid)+".txt", "a")
        f.write(base64_message)
        f.close()

        f = open("static/5/"+str(maxid)+".txt", "a")
        f.write(base64_message)
        f.close()
        #################

        return render_template('customer_home.html')
#######################33333333

##############################
@app.route("/customer_product")
def customer_product():
    cur = conn.cursor()
    uname=session['uname']
    cur.execute("SELECT id,manager,tender_name,department,duration,quotation_amount,status FROM quotation_details where username='"+uname+"'")
    data = cur.fetchall()
    return render_template('customer_product.html',items=data)
#####customer_my_product
@app.route("/customer_my_product")
def customer_my_product():
    cur = conn.cursor()
    uname=session['uname']
    cur.execute("SELECT uname,product_name,category,price,gst,quantity,total,farmer FROM purchase_details where uname='"+uname+"'")
    data = cur.fetchall()
    return render_template('customer_my_product.html',items=data)
#################################################################################################### CUSTOMER
@app.route("/customer")
def customer():
    return render_template('customer.html')

@app.route("/customer_register")
def customer_register():
    return render_template('customer_register.html')
@app.route("/customer_registeration",methods = ['GET', 'POST'])
def customer_registeration():
    if request.method == 'POST':
        cname = request.form['name']
        contact = request.form['contact']
        email = request.form['email']
        address = request.form['address']

        username = request.form['username']
        password = request.form['password']

        if password==password:
            cursor = conn.cursor()
            cursor.execute("SELECT max(id)+1 FROM   customer_details")
            maxid = cursor.fetchone()[0]
            if maxid is None:
                maxid=1
            cursor = conn.cursor()
            cursor.execute("insert into customer_details values('"+str(maxid) + "','"+cname + "','"+contact+"','"+email+"','"+address+"','"+username+"','"+password+"','0','0')")
            conn.commit()
        else:
            d=0
        return render_template('customer.html')

    return render_template('customer_register.html')


@app.route("/customer_login",methods = ['GET', 'POST'])
def customer_login():
    if request.method == 'POST':
        n = request.form['username']
        g = request.form['password']
        n1=str(g)
        g1=str(g)
        cursor = conn.cursor()
        cursor.execute("SELECT * from customer_details where username='" + n + "' and password='" + str(g) + "'")
        data = cursor.fetchone()
        conn.commit()
       # cursor.close()
        if data is None:
            return 'Username or Password is wrong'
        else:
            session['uname'] =n
            #print(n)
            return render_template('customer_home.html',sid=n)
    return render_template('customer.html')


@app.route("/admin_login", methods = ['GET', 'POST'])
def admin_login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            return render_template('admin_home.html',error=error)
        else:
            return render_template('admin.html', error=error)

@app.route("/admin_home")
def admin_home():
    return render_template('admin_home.html')

@app.route("/admin_train")
def admin_train():
    return render_template('farmer_register.html')

@app.route("/admin_farmer")
def admin_farmer():
    cursor2 = conn.cursor()
    cursor2.execute("select id,manager,tender_name,department,duration,amount,username,status from quotation_details")
    return render_template('admin_farmer.html',items=cursor2.fetchall())


@app.route("/admin_customer")
def admin_customer():
    cursor2 = conn.cursor()
    cursor2.execute("select id,name,contact,email,address from customer_details")
    return render_template('admin_customer.html',items=cursor2.fetchall())

@app.route("/dataset_upload",methods = ['GET', 'POST'])
def dataset_upload():
    if request.method == 'POST':
        if 1==1:
            if 'file' not in request.files:
                flash('No file Part')
                return redirect(request.url)
            file= request.files['file']
            print(file)
            f = request.files['file']
            f.save(os.path.join("static/uploads/", secure_filename(f.filename)))

            return render_template('admin_train.html',msg="Success")
        else:
            return render_template('admin_train.html')

@app.route('/student_college5/<string:filename>', methods=['GET','POST'])
def user_file_recei11(filename):
    data=[]
    di=filename
    ###########################
    f1= open("static/1/"+str(di)+".txt", "r")
    data1=(f1.read())
    f2 = open("static/2/"+str(di)+".txt", "r")
    data2=(f2.read())
    f3 = open("static/3/"+str(di)+".txt", "r")
    data3=(f3.read())
    f4 = open("static/4/"+str(di)+".txt", "r")
    data4=(f4.read())
    f5 = open("static/5/"+str(di)+".txt", "r")
    data5=(f5.read())
    if((data1==data2) and (data1==data3) and (data1==data3) and (data1==data4)and (data1==data5)):

        print("sssssss")
        conn = pymysql.connect(user='root', password='', host='localhost', database='python_secure_e_tender',charset='utf8')
        cursor1 = conn.cursor()
        cursor1.execute("update quotation_details set status='Accept' where id='"+filename+"'")
        conn.commit()
        conn.close()
        return render_template('farmer_home.html', items=data)
    else:
        return ("File Modified")
    #######################33333333



@app.route('/student_college6/<string:filename>', methods=['GET','POST'])
def user_file_recei161(filename):
    data=[]
    conn = pymysql.connect(user='root', password='', host='localhost', database='python_secure_e_tender',charset='utf8')
    cursor1 = conn.cursor()
    cursor1.execute("update quotation_details set status='Reject' where id='"+filename+"'")
    conn.commit()
    conn.close()
    return render_template('farmer_home.html', items=data)
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
