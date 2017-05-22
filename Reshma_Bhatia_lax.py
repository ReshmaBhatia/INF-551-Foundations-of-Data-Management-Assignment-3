import mysql.connector
import sys
import re

a=sys.argv[1]
b=sys.argv[2]
cnx = mysql.connector.connect(user='inf551',password='inf551',host='127.0.0.1', database='inf551')
cursor = cnx.cursor()

query ="select sum(passenger_count) from LAX where arrv_dept=\"" +a+"\"" +"and report_period LIKE '" +b+"%'";
#print query
data_query = (a)
cursor.execute(query,data_query)

row = cursor.fetchone()
a=row;
if not row:
    print 'Query is not executed'
elif a[0]==None:
    print 0
else:
    print a[0]
cnx.commit()
cursor.close()
cnx.close()

