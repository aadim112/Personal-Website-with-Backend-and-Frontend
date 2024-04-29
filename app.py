from flask import Flask,Request,render_template,url_for,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static'
db = SQLAlchemy(app)

class contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    phno = db.Column(db.String)
    query =db.Column(db.String)
    
    
class projectcard(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    imageurl = db.Column(db.String)
    heading = db.Column(db.String)
    info = db.Column(db.String)
    gitlink = db.Column(db.String)
    status = db.Column(db.String)

class ContactData(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    phoneNo = db.Column(db.String)
    qry = db.Column(db.String)
    Label = db.Column(db.String, default = 'New')


class Hire(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    companyName = db.Column(db.String)
    MobNo = db.Column(db.String)
    Email = db.Column(db.String)
    websitetype = db.Column(db.String)
    Label = db.Column(db.String, default = 'New')
    
class thumbnail(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    img1Url =  db.Column(db.String)
    img2Url =  db.Column(db.String)
    img3Url =  db.Column(db.String)

class Aplan1(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    price = db.Column(db.String)
    typ1 = db.Column(db.String)
    type2 = db.Column(db.String)
    profit1 = db.Column(db.String)
    profit2 = db.Column(db.String)
    profit3 = db.Column(db.String)
    profit4 = db.Column(db.String)

class Aplan2(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    price = db.Column(db.String)
    typ1 = db.Column(db.String)
    type2 = db.Column(db.String)
    profit1 = db.Column(db.String)
    profit2 = db.Column(db.String)
    profit3 = db.Column(db.String)
    profit4 = db.Column(db.String)

class Free(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    price = db.Column(db.String)
    typ1 = db.Column(db.String)
    type2 = db.Column(db.String)
    profit1 = db.Column(db.String)
    profit2 = db.Column(db.String)
    profit3 = db.Column(db.String)
    profit4 = db.Column(db.String)
    
@app.route('/', methods = ['GET'])
def index():
    if request.method == 'GET':
        data = thumbnail.query.filter_by(id = 1).first()
        img1 = data.img1Url
        img2 = data.img2Url
        img3 = data.img3Url
        plan1 = Aplan1.query.filter_by(id = 1).first()
        plan2 = Aplan2.query.filter_by(id = 1).first()
        
        price1 = plan1.price
        p1typ1 = plan1.typ1
        p1type2 = plan1.type2
        p1profit1 = plan1.profit1
        p1profit2 = plan1.profit2
        p1profit3 = plan1.profit3
        p1profit4 = plan1.profit4
        
        price2 = plan2.price
        p2typ1 = plan2.typ1
        p2type2 = plan2.type2
        p2profit1 = plan2.profit1
        p2profit2 = plan2.profit2
        p2profit3 = plan2.profit3
        p2profit4 = plan2.profit4
        return render_template('index.html',img1 = img1,img2 = img2,img3= img3,price1 = price1,p1typ1 = p1typ1,p1type2 = p1type2,p1profit1 = p1profit1,p1profit2 = p1profit2, p1profit3 = p1profit3 , p1profit4 = p1profit4,
                               price2= price2,p2typ1 = p2typ1, p2type2 = p2type2 , p2profit1 = p2profit1 , p2profit2 = p2profit2 , p2profit3 = p2profit3 , p2profit4 = p2profit4)

@app.route('/Sites')
def seeall():
    if request.method == 'GET':
        ProjectData = projectcard.query.all()
        return render_template('sites.html', ProjectData = ProjectData)

@app.route('/Admin',methods = ['GET'])
def Admin():
    if request.method == 'GET':
        Contact = ContactData.query.all()
        hire = Hire.query.all()
        pcards = projectcard.query.all()
        for i in pcards:
            print(i.heading)
        return render_template('Admin.html',Contact =  Contact, hire = hire,pcards = pcards)

@app.route('/add', methods = ['POST','GET'])
def ProjectCards():
    if request.method == 'POST':
        url = request.form['url']
        heading = request.form['heading']
        info = request.form['info']
        gitlink = request.form['gitlink']
        status = request.form['status']
        upload = projectcard(imageurl = url, heading = heading , info = info, gitlink = gitlink, status = status)
        db.session.add(upload)
        db.session.commit()
        return 'Data Uploaded!!'
    
@app.route('/contact', methods = ['POST','GET'])
def Simplecontact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        quer = request.form['query']
        upload = ContactData(name = name,email = email ,phoneNo = phone,qry = quer,Label = 'New')
        db.session.add(upload)
        db.session.commit()
        return render_template('welcome.html')

@app.route('/thumbnailImage', methods = ['POST'])
def thumbnailImage():
    if request.method == "POST":
        url1 = request.form['img1']
        url2 = request.form['img2']
        url3 = request.form['img3']
        data = thumbnail.query.filter_by(id = 1).first()
        data.img1Url = url1
        data.img2Url = url2
        data.img3Url = url3
        db.session.add(data)
        db.session.commit()
        return "Done Updating Thumbnails"

@app.route('/HireMe', methods = ['POST'])
def HireMe():
    if request.method == 'POST':
        name = request.form['name']
        companyName = request.form['companyName']
        mobNo = request.form['mobNo']
        email = request.form['email']
        type = request.form['type']
        upload = Hire( name = name,companyName = companyName,MobNo = mobNo,Email = email, websitetype = type, Label = 'New')
        db.session.add(upload)
        db.session.commit()
        return render_template('welcome.html')
    
@app.route('/plan1',methods = ['POST'])
def plan1():
    if request.method == 'POST':
        price = request.form['price1']
        type1 = request.form['type1']
        type2 = request.form['type2']
        pr1 = request.form['pr1']
        pr2 = request.form['pr2']
        pr3 = request.form['pr3']
        pr4 = request.form['pr4']
        upload = Aplan1.query.filter_by(id = 1).first()
        upload.price = price
        upload.typ1 = type1
        upload.type2 = type2
        upload.profit1 = pr1
        upload.profit2 = pr2
        upload.profit3 = pr3
        upload.profit4 = pr4
        db.session.add(upload)
        db.session.commit()
        return 'Data Updated!!'

@app.route('/plan2',methods = ['POST'])
def plan2():
    if request.method == 'POST':
        price = request.form['price2']
        type1 = request.form['type1']
        type2 = request.form['type2']
        pr1 = request.form['pr1']
        pr2 = request.form['pr2']
        pr3 = request.form['pr3']
        pr4 = request.form['pr4']
        upload = Aplan2.query.filter_by(id = 1).first()
        upload.price = price
        upload.typ1 = type1
        upload.type2 = type2
        upload.profit1 = pr1
        upload.profit2 = pr2
        upload.profit3 = pr3
        upload.profit4 = pr4
        db.session.add(upload)
        db.session.commit()
        return 'Data Updated!!'

@app.route('/deleteData/<string:heading>',methods = ['POST'])
def deleteData(heading):
    if request.method == 'POST':
        data_to_delete = projectcard.query.filter_by( heading = heading).first()
        db.session.delete(data_to_delete)
        db.session.commit()
        return 'Data Deleted!'