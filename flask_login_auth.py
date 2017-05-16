# import Psycopg2 as pg

# --------------------------------------------------------------------
# --------------------------------------------------------------------

# connection to database----------------------------------------------
import MySQLdb

def get_connection():
    try:
        conn = MySQLdb.connect( host='127.0.0.1', user='root', passwd='root@123', db= 'CONTACT_DB')
        cur = mydb.cursor()
        cur.execute("SELECT * FROM Persons")

        # print all the first cell of all the rows
        for row in cur.fetchall():
            print row[0]

        db.close()
        return conn
    except Exception as error:
        return error

# for authenticating ---------------------------------------------------
# Try except block is used for passing errors

def get_connection_login():
    try:
        conn = MySQLdb.connect( host='127.0.0.1', user='root', passwd='root@123', db= 'public')
        return conn
    except Exception as error:
        return error

def authenticate(username, password):
    try:
        connection = get_connection_login()
        cursor = connection.cursor()
        query = """SELECT userid, password from user_rec where userid='%s' and password='%s'"""  # noqa
        query = query % (username, password)
        cursor.execute(query)
        rows = cursor.fetchall()
        try:
            if (rows[0][0] == username) and (rows[0][1] == password):
                print(">>>>>>>", rows[0][0],rows[0][1])
                connection.close()
                return 1
            else:
                connection.close()
                return 0
        except Exception as error:
            return error
    except Exception as error:
        return error
# -------------------------------------------------------------------------


# -------------------------------------------------------------------------
# Search Box --------------------------------------------------------------


def searchbox(userid):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = """SELECT * FROM "public"."user_rec" WHERE userid LIKE '%s'"""
        query = query % ('%' + userid + '%')
        cursor.execute(query)
        rows = cursor.fetchall()
        connection.close()
        return rows
    except Exception as error:
        return error


