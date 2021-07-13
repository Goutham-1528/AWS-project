# -*- coding: utf-8 -*-

import pymysql
conn = pymysql.connect(
        host= "dataproject.ctw7ud33mt0n.us-east-2.rds.amazonaws.com", #endpoint link
        port = 3306, # 3306
        user = "admin", # admin
        password = "Goutham1528", #adminadmin
        db = "mysql1", #test
        )

#Table Creation
# cursor=conn.cursor()
# create_table="""
# create table Details (name varchar(200),email varchar(200),phone varchar(30),bdate varchar(30),btime varchar(30) )
# """
# cursor.execute(create_table)


def insert_details(name,email,phone,bdate,btime):
    cur=conn.cursor()
    cur.execute("INSERT INTO Details (name,email,phone,bdate,btime) VALUES (%s,%s,%s,%s,%s)", (name,email,phone,bdate,btime))
    conn.commit()

def get_details():
    cur=conn.cursor()
    cur.execute("SELECT *  FROM Details")
    details = cur.fetchall()
    return details
