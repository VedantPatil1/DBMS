import sys
import unittest
sys.path.insert(0, '/home/vedant/Projects/DBMS/src/')

from SqliteManager import Database


class TestSqliteManager(unittest.TestCase):
    def __init__(self):
        self.testDatabase = Database('test.db')
        
    def testCreateTableObject(self):
        columns = {"first_name":"TEXT",
                   "last_name":"TEXT",
                   "Phone_number":"INTEGER",
                   "email":"TEXT",}
        testDatabase.CreateTable('testTable1',columns)
        

