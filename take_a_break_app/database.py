"""
This file contain all database operation for take_a_break_app
"""

import pymysql
from . import dbpassword #not in git for security reason


def create_user(username, email, password):
    """
    create a user with the given information, validation of information will be done before this
    create_user: string, string, string -> Bool
    """
    db = pymysql.connect(host='localhost', 
                    user = "root",
                    password=dbpassword.ROOT_PASSWORD,
                    database='login')
    cursor = db.cursor()
    command = "INSERT INTO login (username, email, password) VALUES (\"{}\", \"{}\", \"{}\")".format(username, email, password)
    try:
        cursor.execute(command)
        db.commit()
    except:
        db.rollback()
        return False #shows a error to backend
    db.close()
    return True # shows add successfully

def check_user_exist(username):
    db = pymysql.connect(host='localhost', 
                    user = "root",
                    password=dbpassword.ROOT_PASSWORD,
                    database='login')
    cursor = db.cursor()
    command = "SELECT username FROM LOGIN where username={}".format(username)
    try:
        cursor.execute(command)
        results = cursor.fetchall()
        db.close()
        return len(results) == 0 #false = no such user exist
    except:
        db.rollback()
        return True #shows a error to backend

def check_user(username, password):
    """
    0: valid user + correct password
    1: incorrect password
    2: username did not find
    3: database error
    """
    db = pymysql.connect(host='localhost', 
                    user = "root",
                    password=dbpassword.ROOT_PASSWORD,
                    database='login')
    cursor = db.cursor()
    command = "SELECT username, password FROM LOGIN where username={}".format(username)
    try:
        cursor.execute(command)
        results = cursor.fetchall()
        if (len(results) == 0):
            return 2
        else: 
            print(results)
    except:
        db.rollback()
        return False #shows a error to backend
    db.close()
    return 0 # shows add successfully

if __name__ == "__main__":
    print("Testing Databse \n")
    db = pymysql.connect(host='localhost', 
                    user = "root",
                    password="gfqpsmp123",
                    database='login')
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print ("Database version : %s " % data)
    check_user("admin", "password")

    db.rollback()
    db.close()


