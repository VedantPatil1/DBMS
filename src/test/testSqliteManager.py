import sys
import unittest
sys.path.insert(0, '/home/vedant/Projects/DBMS/src/')

from SqliteManager import Database
testDatabase = Database('test.db')

class TestSqliteManager(unittest.TestCase):
    def test_CreateTableObject(self):
        columns = {"first_name":"TEXT",
                   "last_name":"TEXT",
                   "Phone_number":"INTEGER",
                   "email":"TEXT",}
        testDatabase.CreateTable('testTable1',columns)
        tableObject = testDatabase.Tables[0]
        TableName = tableObject.tableName
        TableColumns = tableObject.columns
        self.assertAlmostEqual(TableName,'testTable1')
        self.assertAlmostEqual(TableColumns,columns)
    
    

                
