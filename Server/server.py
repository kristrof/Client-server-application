import MySQLdb;
import getpass;
import base64
import pickle

def passwd():
    f = open('conf.txt')
    passw = f.readline()
    f.close()
    passw =base64.b64decode(passw[:-1])
    passw = passw.decode('utf-8')
    return passw

def status_table(name):
    password = passwd()
    db = MySQLdb.connect("localhost","root",password,"testbd")
    #name = input("Name table:")
    cursor = db.cursor()
    tables = cursor.execute("SHOW TABLES")
    table_list = []
    for tables in cursor:
        table_list.append(tables)
    if ((name.decode('utf-8')) in str(table_list)):
        result = "Table exists"
    else:    
        result="Table not found. The table is created."
        cursor.execute("CREATE TABLE %s(col1 int,col2 int)" %name )
    db.close()    
    return result

def table(data):
    password=passwd()
    massiv=[]
    name_table = str(data[1])
    db = MySQLdb.connect("localhost","root",password,"testbd")
    cursor1 = db.cursor()
    cursor1.execute("SELECT * FROM %s" % str(data[1]))
    for row in cursor1.fetchall():
        massiv.append(row)
    massiv = pickle.dumps(massiv)    
    db.close()
    return massiv, name_table

def ins_row(data, name_table):
    #insert row 
    #data.pop(0)
    data1=(data[1]).split(':')    
    password = passwd()
    db = MySQLdb.connect("localhost", "root", password, "testbd",autocommit=True)
    cursor1 = db.cursor()
    cursor2 = db.cursor()
    cursor1.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = '%s'"% name_table)
    column_list = []
    for col in cursor1:
        column_list.append(col)
    i=0 
    for i in range(len(data1)-1):
        s = ""
        s = data1[i][0:-1]
        cursor2.execute("INSERT INTO %s(%s, %s) VALUES (%s)" % (name_table, column_list[0][0], column_list[1][0], s))
    db.close()

def login_in(data):
    #user = []
    #user = data.split(' ')
    password=passwd()
    db = MySQLdb.connect("localhost","root",password,"testbd")
    cursor1 = db.cursor()
    cursor1.execute("SELECT pass FROM log WHERE (id = '%s')" % str(data[1]))
    test_pass = cursor1.fetchone()
    if str(test_pass[0]) == data[2]:
        result = "true"
    else:
        result = "false"
    db.close()    
    return result        
   

    


