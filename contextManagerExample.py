#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sqlite3
from contextlib import contextmanager


class DBHandler(object):

    def __init__(self,dbfile):
        self.dbfile = dbfile

    @contextmanager
    def get_cursor(self):
        self.con = sqlite3.connect(self.dbfile)
        cursor = self.con.cursor()
        yield cursor
        self.con.close()
		print 'Connection closed'
        
    def createTable(self):
        with self.get_cursor() as cursor:
            try:
                cursor.execute("""CREATE TABLE PRODUCTS(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    NAME CHAR(10),
                    PRICE REAL(2))""")
                print "Table created successfully"
            except sqlite3.OperationalError:
                print "Table already exists"

    def setProduct(self,**kwargs):
        with self.get_cursor() as cursor:
            cursor.execute("INSERT INTO PRODUCTS (NAME, PRICE) VALUES ('%s', %f) " % (kwargs['name'], kwargs['price']))
            self.con.commit()


    def getPrice(self,**kwargs):
        with self.get_cursor() as cursor:
            cursor.execute("SELECT NAME, PRICE FROM PRODUCTS WHERE NAME='%s'" % kwargs['name'])
            print kwargs['name'],
            print cursor.next()[1]

    def countProducts(self):
        with self.get_cursor() as cursor:
            n = cursor.execute("SELECT COUNT(*) FROM PRODUCTS").next()[0]
            print n


if __name__=="__main__":
    dbh = DBHandler("db0.db")
    dbh.createTable()
    dbh.setProduct(name = "shampoo", price = 10.5)
    dbh.getPrice(name = "shampoo")
    #dbh.countProducts()
