from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.secret_key = "Secret Key"

#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:jahid0439@localhost/cw6'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


#Creating model table for our CRUD database
class Data(db.Model):
    id = db.Column(db.String(50), primary_key = True)
    sn = db.Column(db.String(4))
    itemCode = db.Column(db.String(20))
    desOfItems = db.Column(db.String(1500))
    quantity = db.Column(db.Float)
    unit = db.Column(db.String(4))
    workDone = db.Column(db.Float)
    date = db.Column(db.String(10))
    reporterName = db.Column(db.String(15))
    schemeId = db.Column(db.String(7))
    itemStatus = db.Column(db.String(20))
    locationCondition = db.Column(db.String(7))
    weatherCondition = db.Column(db.String(12))
    createdBy = db.Column(db.String(22))
    contractorName = db.Column(db.String(40))
    modifiedBy = db.Column(db.String(22))
    created = db.Column(db.String(15))
    isExtra = db.Column(db.String(4))


    def __init__(self, id, sn, itemCode, desOfItems, quantity, unit, workDone, date,
    reporterName, schemeId, itemStatus, locationCondition, weatherCondition, createdBy, contractorName,
    modifiedBy, created, isExtra):

        self.id = id
        self.sn = sn
        self.itemCode = itemCode
        self.desOfItems = desOfItems
        self.quantity = quantity
        self.unit = unit
        self.workDone = workDone
        self.date = date
        self.reporterName = reporterName
        self.schemeId = schemeId
        self.itemStatus = itemStatus
        self.locationCondition = locationCondition
        self.weatherCondition = weatherCondition
        self.createdBy = createdBy
        self.contractorName = contractorName
        self.modifiedBy = modifiedBy
        self.created = created
        self.isExtra = isExtra




#This is the index route where we are going to
#query on all our employee data
@app.route('/')
def Index():
    all_data = Data.query.all()

    return render_template("index.html", entryList = all_data)



#this route is for inserting data to mysql database via html forms
@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == 'POST':


        id = request.form['id']
        sn = request.form['sn']
        itemCode = request.form['itemCode']
        desOfItems = request.form['desOfItems']
        quantity = request.form['quantity']
        unit = request.form['unit']
        workDone = request.form['workDone']
        date = request.form['date']
        reporterName = request.form['reporterName']
        schemeId = request.form['schemeId']
        itemStatus = request.form['itemStatus']
        locationCondition = request.form['locationCondition']
        weatherCondition = request.form['weatherCondition']
        createdBy = request.form['createdBy']
        contractorName = request.form['contractorName']
        modifiedBy = request.form['modifiedBy']
        created = request.form['created']
        isExtra = request.form['isExtra']

        my_data = Data(id, sn, itemCode, desOfItems, quantity, unit, workDone, date, reporterName,
        schemeId, itemStatus, locationCondition, weatherCondition, createdBy, contractorName,
        modifiedBy, created, isExtra)
        db.session.add(my_data)
        db.session.commit()

        flash("Entry Inserted Successfully")

        return redirect(url_for('Index'))


#this is our update route where we are going to update our employee
@app.route('/update', methods = ['GET', 'POST'])
def update():

    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))

        my_data.id = request.form['id']
        my_data.sn = request.form['sn']
        my_data.itemCode = request.form['itemCode']
        my_data.desOfItems = request.form['desOfItems']
        my_data.quantity = request.form['quantity']
        my_data.unit = request.form['unit']
        my_data.workDone = request.form['workDone']
        my_data.date = request.form['date']
        my_data.reporterName = request.form['reporterName']
        my_data.schemeId = request.form['schemeId']
        my_data.itemStatus = request.form['itemStatus']
        my_data.locationCondition = request.form['locationCondition']
        my_data.weatherCondition = request.form['weatherCondition']
        my_data.createdBy = request.form['createdBy']
        my_data.contractorName = request.form['contractorName']
        my_data.modifiedBy = request.form['modifiedBy']
        my_data.created = request.form['created']
        my_data.isExtra = request.form['isExtra']

        db.session.commit()
        flash("Information Updated Successfully")

        return redirect(url_for('Index'))




#This route is for deleting our employee
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Information Deleted Successfully")

    return redirect(url_for('Index'))






if __name__ == "__main__":
    app.run(debug=True)
