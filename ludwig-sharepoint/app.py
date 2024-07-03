from flask import Flask, request, jsonify, render_template
from shareplum import Site
from shareplum import Office365
from shareplum.site import Version
import numpy as np
import pandas as pd
import os

app = Flask(__name__)

sharepointUsername = "Bangladesh.IT1@ludwigpfeiffer.com"
sharepointPassword = "A%vhTlN90Z%M"
sharepointSite = "https://ludwpfeiffer.sharepoint.com/sites/PfeifferDhaka"
website = "https://ludwpfeiffer.sharepoint.com"
authcookie = Office365(website, username=sharepointUsername,password=sharepointPassword).GetCookies()
site = Site(sharepointSite, version=Version.v2016, authcookie=authcookie)
set_list = site.List('python_sync')
share_data = set_list.GetListItems('All Items') # this will retrieve all items from list
# final_data = pd.DataFrame(share_data[0:])
# final_data.to_excel("final.xlsx")
# df1 = pd.read_excel("final.xlsx")
# Items = df1['Item Serial No']
# Work = df1['Name of work including materials']
# Units = df1['Units']
# Quantity = df1['Quantity']
# Date = df1['Date']
# workDone = df1['Work Done']


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit',methods=['GET', 'POST'])
def submit():
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]

    # path = 'data.xlsx'
    # df1 = pd.read_excel(set_list)
# this creates pandas data frame you can perform any operation you like do within
# pandas capabilities
    # A = pd.Series(final_features[0][0])
    # B = pd.Series(final_features[0][1])
    # C = pd.Series(final_features[0][2])
    # D = pd.Series(final_features[0][3])
    # E = pd.Series(final_features[0][4])
    # F = pd.Series(final_features[0][5])
    # newItems = Items.append(A)
    # newWork = Work.append(B)
    # newUnits = Units.append(C)
    # newQuantity = Quantity.append(D)
    # newDate = Date.append(E)
    # newWorkDone = workDone.append(F)
    newItems = final_features[0][0]
    newWork = final_features[0][1]
    newUnits = final_features[0][2]
    newQuantity = final_features[0][3]
    newDate = final_features[0][4]
    newWorkDone = final_features[0][5]
    my_data = data=[{'Item Serial No' : newItems, 'Name of work including materials' : newWork, 'Units' : newUnits, 'Quantity': newQuantity, 'Date' : newDate, 'Work Done': newWorkDone}]
    set_list.UpdateListItems(data=my_data, kind='New')
    # df2.to_excel(path, index=False)
    # flash('Sumbitted successfully')
    return render_template('index.html', Data='Sumbitted successfully')
    #return render_template('index.html', data= final_features)

if __name__ == "__main__":
    app.run(debug=True)


# from flask import Flask, jsonify
#
# app = Flask(__name__)
#
# Dushanbe = [{'Item_Serial_No' : "0",
#             'Name_of_work_including_materials' : "Marking of the pipeline route with paint, including inventory of existing underground engineering communications (such as pipes and cables of other networks)",
#             'Units' : "kits",
#             'Quantity': "10863",
#             'Date' : "2020-01-15",
#             'Work_Done': "Yes"}]
#
# @app.route('/')
# def index():
#     return "Welcome for my api"
#
# @app.route("/dushanbe", methods=['GET'])
# def get():
#     return jsonify({'dushanbe_list': Dushanbe})
#
# @app.route("/dushanbe/<int:Item_Serial_No>", methods=['GET'])
# def get_dushanbe(Item_Serial_No):
#     return jsonify({'dushanbes': Dushanbe[Item_Serial_No]})
#
# @app.route("/dushanbe", methods=['POST'])
# def create():
#
#     Dushanbes = [{'Item_Serial_No' : "1", 'Name_of_work_including_materials' : "Work of a bulldozer on the dump", 'Units' : "m3", 'Quantity': "1940", 'Date' : "2020-01-26", 'Work_Done': "No"}]
#     Dushanbe.append(Dushanbes)
#     return jsonify({'Created': Dushanbes})
#
# if __name__ == '__main__':
#     app.run(debug=True)
