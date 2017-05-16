import MySQLdb


def get_connection():
    try:
        conn = MySQLdb.connect( host='127.0.0.1', user='root', passwd='root@123', db='CONTACT_DB' )
        return conn
    except Exception as e:
        raise e


def create_db():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
             '''
                CREATE TABLE Persons ( PersonID int NOT NULL AUTO_INCREMENT, fisrtname VARCHAR(20), lastname VARCHAR(20),  PRIMARY KEY (PersonID));

                CREATE TABLE Groups ( GroupID int NOT NULL AUTO_INCREMENT, groupname VARCHAR(40) ,  PRIMARY KEY (GroupID,groupname));

                CREATE TABLE person_group (PersonID int NOT NULL, GroupID int NOT NULL, FOREIGN KEY (PersonID) REFERENCES Persons(PersonID) ON DELETE CASCADE, FOREIGN KEY (GroupID) REFERENCES Groups(GroupID) ON DELETE CASCADE, PRIMARY KEY (PersonID, GroupID));

                CREATE TABLE person_address ( StreetADD varchar(100) NOT NULL, PersonID int NOT NULL, FOREIGN KEY (PersonID) REFERENCES Persons(PersonID) ON DELETE CASCADE, PRIMARY KEY (PersonID, StreetADD));

                CREATE TABLE person_email ( emailid varchar(50) NOT NULL, PersonID int NOT NULL, FOREIGN KEY (PersonID) REFERENCES Persons(PersonID) ON DELETE CASCADE , PRIMARY KEY (PersonID, emailid));

                CREATE TABLE person_phone ( phoneNUM varchar(15) NOT NULL, PersonID int NOT NULL, FOREIGN KEY (PersonID) REFERENCES Persons(PersonID) ON DELETE CASCADE, PRIMARY KEY (PersonID, phoneNUM) );
             '''
        )
        connection.commit()
        connection.close()
    except Exception as error:
        return error

def get_connection_login():
    try:
        conn = MySQLdb.connect( host='127.0.0.1', user='root', passwd='root@123', db= 'public')
        return conn
    except Exception as error:
        return error


def process_create_user(fisrtname, lastname, group , email, st_address, phone_number):
    BLOCK = False
    connection = get_connection()
    cursor = connection.cursor()
    query = """INSERT INTO Persons( firstname, lastname ) VALUES('%s', '%s');"""
    query = query % ( fisrtname, lastname )
    cursor.execute(query)
    print("abcdef - error - 70")
    query = """SELECT PersonID FROM Persons ORDER BY Persons.PersonID DESC LIMIT 1;"""
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        PersonID = row[0]
    print(PersonID)
    print("abcdef - error - 74")
    query = """SELECT GroupID from Groups where groupname='%s';"""
    query = query % ( group )
    cursor.execute(query)
    rows = cursor.fetchall()
    try:
        if len(rows) == 0:
            query = """INSERT INTO Groups( groupname ) VALUES( '%s' );"""
            query = query % ( group )
            cursor.execute(query) 

            print("abcdef - error - 79")
            query = """SELECT GroupID FROM Groups ORDER BY Groups.GroupID DESC LIMIT 1;"""
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                GroupID = row[0]
            print(GroupID)
            print("abcdef - error - 83")
        else:
            for row in rows:
                GroupID = row[0]
    except Exception as error:
        print("abcdef - error3")
        return error
    query = """INSERT INTO person_group( GroupID, PersonID ) VALUES('%s', '%s');"""
    query = query % ( GroupID, PersonID )
    cursor.execute(query)   

    print("abcdef - error - 88")
    query = """INSERT INTO person_email( emailid, PersonID ) VALUES('%s', '%s');"""
    query = query % ( email, PersonID )
    cursor.execute(query)

    print("abcdef - error - 93")
    query = """INSERT INTO person_phone( phoneNUM, PersonID ) VALUES('%s', '%s');"""
    query = query % ( phone_number, PersonID )
    cursor.execute(query)

    print("abcdef - error - 98")
    query = """INSERT INTO person_address( StreetADD, PersonID ) VALUES('%s', '%s');"""
    query = query % ( st_address, PersonID )
    cursor.execute(query)

    print("abcdef - error - 103")
    connection.commit()
    connection.close()



def create_user( fisrtname, lastname, group , email, st_address, phone_number):
    connection = get_connection()
    cursor = connection.cursor()
    query = """SELECT emailid from person_email where emailid='%s';"""
    query = query % (email, )
    cursor.execute(query)
    rows = cursor.fetchall()
    try:
        if len(rows) == 0:
            print("abcdef")
            process_create_user(fisrtname, lastname, group , email, st_address, phone_number)
        else:
            print("abcdef - error")
            return 1
    except Exception as error:
        print("abcdef - error2")
        return error
    connection.close()

def process_create_group( group ):
    # BLOCK = False
    connection = get_connection()
    cursor = connection.cursor()
    query = """INSERT INTO Groups( groupname ) VALUES('%s');"""
    query = query % ( group )
    cursor.execute(query)
    connection.commit()
    connection.close()

def add_group(group):
    connection = get_connection()
    cursor = connection.cursor()
    query = """SELECT GroupID from Groups where groupname='%s';"""
    query = query % (group, )
    cursor.execute(query)
    rows = cursor.fetchall()
    try:
        if len(rows) == 0:
            process_create_group( group )
        else:
            return 1
    except Exception as error:
        return error
    connection.close()

def message_show():
    connection = get_connection()
    cursor = connection.cursor()
    query = """SELECT * from Persons;"""
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows
    connection.close()


def get_info_persons_group(firstname , lastname):
    connection = get_connection()
    cursor = connection.cursor()
    query = """ SELECT p.PersonID from Persons as p where  p.firstname = '%s' and p.lastname = '%s' ;"""
    query = query % (firstname,lastname)
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        PersonID = row[0]

    query = """SELECT pg.GroupID from person_group as pg where pg.PersonID = '%s' ;"""  # noqa
    query = query % PersonID
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        GroupID = row[0]

    query = """SELECT p.firstname, p.lastname, g.groupname from Persons as p, Groups as g where p.PersonID= '%s' and g.GroupID = '%s' ;"""  # noqa
    query = query % (PersonID,GroupID)
    cursor.execute(query)

    rows = cursor.fetchall()
    return rows
    connection.close()

def get_info_group_member(groupname):
    connection = get_connection()
    cursor = connection.cursor()
    print(groupname)
    query = """SELECT g.GroupID from Groups as g where g.groupname = '%s' ;"""  # noqa
    query = query % groupname
    GroupID = cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        GroupID = row[0]
        
    query = """SELECT pg.PersonID from person_group as pg where pg.GroupID = '%s' ;"""  # noqa
    query = query % GroupID
    PersonID = cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        PersonID = row[0]

    query = """SELECT p.firstname, p.lastname, g.groupname from Persons as p, Groups as g where p.PersonID= '%s' and g.GroupID = '%s' ;"""  # noqa
    query = query % (PersonID,GroupID)
    cursor.execute(query)


    rows = cursor.fetchall()
    for a in rows:
        print(a[0],a[1],a[2])
    return rows

    connection.close()

def person_by_fname_and_lname(firstname, lastname):
    connection = get_connection()
    cursor = connection.cursor()

    query = """SELECT p.firstname, p.lastname from Persons as p where p.firstname like '%s' or p.lastname like '%s' ;"""  # noqa
    query = query % (firstname,lastname)
    cursor.execute(query)


    rows = cursor.fetchall()
    return rows
    connection.close()

def person_by_fname(firstname):
    connection = get_connection()
    cursor = connection.cursor()

    query = """SELECT p.firstname, p.lastname from Persons as p where p.firstname like '%s' ;"""  # noqa
    query = query % (firstname)
    cursor.execute(query)


    rows = cursor.fetchall()
    return rows
    connection.close()

def person_by_lname(lastname):
    connection = get_connection()
    cursor = connection.cursor()

    query = """SELECT p.firstname, p.lastname from Persons as p where p.lastname like '%s' ;"""  # noqa
    query = query % (lastname)
    cursor.execute(query)


    rows = cursor.fetchall()
    return rows
    connection.close()


def search(search, value, value2=''):
    print(search)
    if search == 'group':
        rows = get_info_group_member(value)
    elif search == 'person':
        rows = get_info_persons_group(value, value2)
    elif search == 'firstname':
        rows = person_by_fname(value)
    elif search == 'lastname':
        rows = person_by_lname(value)
    elif search == 'firstname_lastname':
        rows = person_by_fname_and_lname(value, value2)
    return rows


