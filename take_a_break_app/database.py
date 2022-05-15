"""
This file contain all database operation for take_a_break_app
"""

import pymysql
from password import *

def create_user(username, email, password):
    """
    create a user with the given information, validation of information will be done before this
    create_user: string, string, string -> Bool
    """
    db = pymysql.connect(host='localhost', 
                    user = "root",
                    password=ROOT_PASSWORD,
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
    db.rollback()
    db.close()


