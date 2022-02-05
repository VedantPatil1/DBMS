import sys
import unittest
import inspect
sys.path.insert(0, '/home/vedant/Projects/DBMS/src/')

from SqliteManager import Database

class TestSqliteManager(unittest.TestCase):
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

    def tearDown(self):
        pass

    def test_CreateTableObject(self):
        self.testDatabase.CreateTable('table',{'hi':'ho'})
        tableObject = self.testDatabase.Tables['table']
        TableName = tableObject.tableName
        TableColumns = tableObject.columns
        self.assertAlmostEqual(TableName,'table')
        self.assertAlmostEqual(TableColumns,{'hi':'ho'})
    
    def test_CreateRowObject(self):
        self.tableObject.CreateRow(self.RowId)
        attributes=[]
        for i in inspect.getmembers(self.tableObject.Rows[self.RowId]):  
            if not i[0].startswith('_'):
                if not inspect.ismethod(i[1]): 
                    attributes.append(i)
        attributes.sort()
        desired_attributes = [('email', 'TEXT'), ('first_name', 'TEXT'), ('last_name', 'TEXT'), ('Phone_number', 'INTEGER')]
        desired_attributes.sort()
        self.assertListEqual(attributes,desired_attributes)
    
    
        