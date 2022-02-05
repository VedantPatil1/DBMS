import sqlite3


conn = sqlite3.connect('BalanceSheet.db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Expenses (Name text, Date text, Amount text)")
cur.execute("SELECT * FROM Expenses")
rows = cur.fetchall()

class Expense:
    def __init__(self, Name, Date, Amount):
        self.Amount = Amount
        self.Date = Date
        self.Name = Name

    def PushToSqlite3(self):
        cur.execute("insert into Expenses values (?, ?, ?)", (self.Name, self.Date, self.Amount))

    def DisplayExpense(self):
        print("Name   ::  ", self.Name)
        print("Date   ::  ", self.Date)
        print("Amount ::  ", self.Amount)


Expenses = []                 ## A List that holds objects of class Expense


def RunInitialSetup():
    pass


def UpdateExpenses():
    for row in rows:
        expense_name = row[0]
        expense_date = row[1]
        expense_amount = row[2]
        Expenses.append(Expense(expense_name, expense_date, expense_amount))


def AddExpense():
    print("Add a new expense")
    expense_name = str(input("Discriptive Name of an expense \n ->"))
    expense_date = str(input("Date ( DD/MM/YYYY )\n ->"))
    expense_amount = int(input("Amount (no dec. ) \n ->"))
    Expenses.append(Expense(expense_name, expense_date, expense_amount))


def DisplayExpenses():
    for exp in Expenses:
        exp.DisplayExpense()
        exp.PushToSqlite3()


conn.commit()
conn.close()
