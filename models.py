#!/usr/bin/python
# -*- coding: utf-8 -*-

import mysql.connector
import sys
#import pdb


class Database:

    def __init__(self):
        try:
            cnx = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Muff4hire",
                database="uranium_database")
        except mysql.connector.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
            sys.exit(1)
        self.cnx = cnx

    def district_names(self):
        district_names = []
        cnx = self.cnx
        cursor = cnx.cursor()
        sql = ("""SELECT district_name
                     FROM district
                     ORDER BY district_name""")
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            district_names.append(row[0])
        cursor.close()
        # returns a list
        return district_names
