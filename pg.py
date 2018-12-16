import os
import psycopg2
import numpy as np
from pprint import pprint

"""
CREATE TABLE table_test (id serial PRIMARY KEY, num integer, data varchar);


"""


def connection(sql_command):
    try:
        conn = psycopg2.connect("dbname='test' user='postgres' host='localhost' password='1'")
    except psycopg2.Error as err:
        print("Connection error: {}".format(err))

    cur = conn.cursor()
    cur.execute(sql_command)
    conn.commit()
    cur.close()
    conn.close()


def create_table(table_name):
    sql = f"CREATE TABLE IF NOT EXISTS {table_name} (id serial PRIMARY KEY, n1 numeric, n2 numeric, n3 numeric);"
    connection(sql)


def insert_table(table, n1, n2, n3):
    sql = f"INSERT INTO {table} (n1, n2, n3) VALUES ({n1}, {n2}, {n3});"
    connection(sql)


def truncate_table():
    connection("TRUNCATE table_test;")

def get_data():
    try:
        conn = psycopg2.connect("dbname='test' user='postgres' host='localhost' password='1'")
    except psycopg2.Error as err:
        print("Connection error: {}".format(err))
    cur = conn.cursor()
    cur.execute('SELECT n1,n2,n3 FROM numpy2')
    records = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return records

if __name__ == '__main__':
    # arr = np.linspace(1, 18, 18).reshape((6, 3))
    # print(*arr)
    print(
    np.array(get_data(), dtype=float)
    )

    # pprint(n_arr)




    # create_table('numpy2')
    #
    # truncate_table()
    # for i in arr:
    #     insert_table('numpy2', *i)
