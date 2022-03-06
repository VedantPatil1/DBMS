import sys
import unittest
import inspect
sys.path.insert(0, '/home/vedant/Projects/DBMS/src/')

from SqliteManager import Database

class TestRow(unittest.TestCase):
    def setUp(self):
        self.testDatabase = Database('test.db')
        self.columns = {"first_name":"TEXT",
                        "last_name":"TEXT",
                        "Phone_number":"INTEGER",
                        "email":"TEXT",}
        self.tableName = 'testTable1'
        self.testDatabase.CreateTable(self.tableName,self.columns)
        self.tableObject=self.testDatabase.Tables[self.tableName]
        self.RowId = 12
        self.tableObject.CreateRow(self.RowId)

    def tearDown(self):
        pass