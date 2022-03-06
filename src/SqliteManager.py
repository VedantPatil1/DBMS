import sqlite3

databaseConnection = {}
TableConfig ={"TableName":{"Column1":"Type1"},
              }

class Database:
    def __init__(self,Name):
        self.Name = Name
        self.Tables = {}     # Holds objects of the class Table in the database
        conn = sqlite3.connect(self.Name)
        self.cur = conn.cursor()
        
    class Table:
        def __init__(self,tableName,columns):  #name of table and names of column in {"name":"type"}
            self.tableName=tableName
            self.columns = columns
            self.Rows = {}  #Holds objects of class Row in the table
        
        def CreateTableInSqliteCommand(self):
            command = "CREATE TABLE IF NOT EXISTS " + self.tableName + " ("
            for column in self.columns:
                command = command + column + " " + self.columns[column] + ", "
            command = command + ")"
            return command


        class Row:
            def __init__(self,record):
                for elementKey in record:
                    setattr(self, elementKey, record[elementKey])

        def AddRecord(self,RowId,record):
            self.Rows[RowId]= self.Row(record)
        
    def CreateTable(self,tableName,columns):
        self.Tables[tableName]=(self.Table(tableName, columns))
    
    def RunInitialConfig(self):
        self.CreateTable()
        
    