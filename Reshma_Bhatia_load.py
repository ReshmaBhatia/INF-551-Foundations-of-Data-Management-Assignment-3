import mysql.connector
import json


def input_vales(report_time,termi,ad,di,count):
    cnx = mysql.connector.connect(user='inf551', password='inf551', host='127.0.0.1',port ='3306', database='inf551')
    cursor = cnx.cursor()
    query = "INSERT INTO LAX(report_period, terminal, arrv_dept, dom_inter, passenger_count) VALUES(%s,%s,%s,%s,%s)"
    data_query = (report_time,termi,ad,di,count)
    cursor.execute(query, data_query)
    cnx.commit()
    cursor.close()
    cnx.close()


testFile = open("lax.json")

data1 = json.load(testFile)
userdata=data1["data"]

for i in userdata:
    j=userdata.index(i)
    report_time=userdata[j][9]
    termi=userdata[j][10]
    ad=userdata[j][11]
    di=userdata[j][12]
    count=userdata[j][13]
    input_vales(report_time,termi,ad,di,count)
