''' This is the sample code to implement cx_oracle in python
Author: Hari om Singh
Date  : 13 jan 2017 ''''

import cx_Oracle

con=cx_Oracle.connect('python/python@localhost:1521/xe')
cur=con.cursor()
result=cur.execute('select name,age,location from friends')
for values in result:
    print(values)
con.close()
