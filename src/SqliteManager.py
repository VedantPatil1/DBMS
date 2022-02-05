class Database:
    def __init__(self,Name):
        self.Name = Name
        self.Tables = []     # stores the list of tables in the database

    
    class Table:
        def __init__(self,tableName,columns):  #name of table and names of column in {"name":"type"}
            self.tableName=tableName
            self.columns = columns
            
        
        def pushTableToSQLite():
            pass


    def CreateTable(self,tableName,columns):
        self.Tables.append(self.Table(tableName, columns))
        