import json

import pymysql
from flask import  Blueprint, request

data_bp= Blueprint('data', __name__)


HOST = 'localhost'
USER = 'root'
PASSWD = 'root'
DB = 'test'
PORT = 3306
CHARSET = 'utf8'
connect = pymysql.connect(host=HOST, user=USER, passwd=PASSWD, db=DB, port=PORT, charset=CHARSET)

@data_bp.route('/data',methods=['GET','POST'])
def get_data():
    if request.method == 'POST':

        sql1 = 'select name,count(*) as counts from mat group by name;;'
        try:
            db_cursor = connect.cursor()
            db_cursor.execute(sql1)
        except:
            connect.ping()
            db_cursor = connect.cursor()
            db_cursor.execute(sql1)

        datas=db_cursor.fetchall()

        xdata=[]
        ydata=[]
        jsonData={}

        for data in datas:
            xdata.append(data[0])
            ydata.append(data[1])


        jsonData["xdata"]=xdata
        jsonData["ydata"]=ydata


        print(jsonData)
        j=json.dumps(jsonData,ensure_ascii=False)

        return j

@data_bp.route('/data1',methods=['GET','POST'])
def get_data1():
    if request.method == 'POST':

        sql1 = 'select name,count(*) as counts from mat2 group by name;'
        try:
            db_cursor = connect.cursor()
            db_cursor.execute(sql1)
        except:
            connect.ping()
            db_cursor = connect.cursor()
            db_cursor.execute(sql1)

        datas=db_cursor.fetchall()

        xdata=[]
        ydata=[]
        jsonData={}

        for data in datas:
            xdata.append(data[0])
            ydata.append(data[1])


        jsonData["xdata"]=xdata
        jsonData["ydata"]=ydata


        j=json.dumps(jsonData,ensure_ascii=False)

        return j

