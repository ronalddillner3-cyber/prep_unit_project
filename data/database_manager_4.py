###############################################################################
################################################################################

import sqlite3
from sqlite3 import Error
import numpy as np


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def close_connection(conn):
    """ closes a connection to a database """
    conn.close()


def select_all(conn,query_statement="SELECT * FROM longley"):
    """select all rows from our table using the conn we already created """
    cur = conn.cursor()
    query = query_statement

    cur.execute(query)

    rows = cur.fetchall()

    return rows


# def get_rows(connection,query="SELECT * FROM longley"):
#     """ Loop through the retrived rows of a table and print them"""
#
#     cur = connection.cursor()
#     query = "SELECT * FROM longley"
#
#     cur.execute(query)
#
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)

def get_rows(db_file,query = "SELECT * FROM longley"):
    """ Loop through the retrived rows of a table and print them"""
    conn=create_connection(db_file)
    rows=select_all(conn,query)
    #rows = cur.fetchall()
    row_list=[]
    for row in rows:
        print(row)
        row_list.append(row)

    return np.array(row_list)
        #for inf in range(len(row)):
            #print(row[inf])


