import sys
import unittest
import inspect
sys.path.insert(0, '/home/vedant/Projects/DBMS/src/')

from SqliteManager import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.testDatabase = Database('test.db')
        
        self.columns = {"first_name":"TEXT",
                        "last_name":"TEXT",
                        "Phone_number":"INTEGER",
                        "email":"TEXT",}
        self.tableName = 'testTable1'
        

    def tearDown(self):
        pass
    
    def test_CreateTableObject(self):
        self.testDatabase.CreateTable(self.tableName,self.columns)
        tableObject = self.testDatabase.Tables[self.tableName]
        TableName = tableObject.tableName
        TableColumns = tableObject.columns
        self.assertAlmostEqual(TableName,self.tableName)
        self.assertAlmostEqual(TableColumns,self.columns)
    
 