import sqlite3

def insert(user_id,name,user_pic,iden=None,label=None,text=None):
    conn = sqlite3.connect("test1.db")
    c = conn.cursor()
    c.execute("SELECT * FROM PEOPLE WHERE USER_ID='%s'" % (user_id))
    if len(c.fetchall()) == 0:
        c.execute("INSERT INTO PEOPLE VALUES('%s','%s','%s','%s','%s','%s')" % (user_id,name,user_pic,iden,label,text))
    conn.commit()
    conn.close()


def check(user_id):
    conn = sqlite3.connect("test1.db")
    c = conn.cursor()
    c.execute("SELECT IDEN FROM PEOPLE WHERE USER_ID='%s'" % (user_id))
    iden = c.fetchall()[0][0]
    conn.close()
    return iden


def msg(user_id):
    conn = sqlite3.connect("test1.db")
    c = conn.cursor()
    c.execute("SELECT MSG FROM MSG WHERE USER_ID='%s'" % (user_id))
    MSG = c.fetchall()
    conn.close()
    a = []
    for i in MSG:
        a.append(i[0])
    return a


def insert_label(user_id,label):
    conn = sqlite3.connect("test1.db")
    c = conn.cursor()
    c.execute("SELECT * FROM ID_LABEL WHERE ID='%s' AND LABEL='%s'" % (user_id,label))
    if len(c.fetchall()) == 0:
        c.execute("INSERT INTO ID_LABEL VALUES('%s','%s')" % (user_id,label))
    conn.commit()
    conn.close()




def user_info():
    conn = sqlite3.connect("test1.db")
    c = conn.cursor()
    c.execute("SELECT USER_ID,USER_NAME FROM PEOPLE")
    #conn.commit()
    res = c.fetchall()
    conn.close()
    return  res


def update_msg(user_id,text):

    conn = sqlite3.connect("test1.db")
    c = conn.cursor()
    c.execute("INSERT INTO MSG VALUES('%s','%s');" % (user_id,text))
    conn.commit()
    conn.close()




def group_msg(label,text):
    conn = sqlite3.connect("test1.db")
    c = conn.cursor()
    msg = []
    for i in label:
        msg.append(f"'{i}'")
    msg2 = ",".join(msg)
    c.execute("SELECT DISTINCT ID FROM ID_LABEL WHERE LABEL IN (%s)" % msg2)
    temp = c.fetchall()
    conn.close()
    for i in temp:
        update_msg(i[0],text)
 
