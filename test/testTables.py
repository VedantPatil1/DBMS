import sys
import unittest
import inspect
sys.path.insert(0, '/home/vedant/Projects/DBMS/src/')

from SqliteManager import Database

class TestTable(unittest.TestCase):
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
        self.record = {"first_name":"Vedant",
                    "last_name":"Patil",
                    "Phone_number":9011752914,
                    "email":"vedantpatil.w.1@gmail.com",}


    def tearDown(self):
        pass

    
    def test_AddRecord(self):
        self.tableObject.AddRecord(self.RowId,self.record)
        attributes=[]
        for i in inspect.getmembers(self.tableObject.Rows[self.RowId]):  
            if not i[0].startswith('_'):
                if not inspect.ismethod(i[1]): 
                    attributes.append(i)
        attributes.sort()
        desired_attributes = [('email', 'vedantpatil.w.1@gmail.com'), ('first_name', 'Vedant'), ('last_name', 'Patil'), ('Phone_number', 9011752914)]
        desired_attributes.sort()
        self.assertListEqual(attributes,desired_attributes)
        