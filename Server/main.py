import server
import conn
import time


con = conn.connect()
while True:
    #
    data = conn.rec(con)
    data1 = data.split(' ')
    if data1[0] == '1':
        #authorization client
        result = server.login_in(data1)
        conn.snd(result, con)
    elif data1[0] == '2':
        # show table
        result_massiv, name_table = server.table(data1)
        conn.snd_byte(result_massiv, con)
    elif data1[0] == '3':
        print(data1)
        server.ins_row(data1, name_table)
    elif data1[0] == '0':
        # close app
        break
    else: 
        print("ne rabotaet")
conn.conn_close(con)
