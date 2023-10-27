class restaurant:
    def __init__(self,item,qty):
        self.item=item
        self.qty=qty
        self.menu= {
            "rice:"30,
            "chicken":100
        }
    
    def findcost(self):
        total=0
        total=self.qty*self.menu[self.item]
        print(self.item,self.qty,total)

order=restaurant("chicken",3)
order.findcost()



#define a classs expensetracker that stores expenses and income in dictionary implement the method to
#store transactiom, view transaction and calculate total expense/income
class expensetracker:
    def __init__(self): #initializing empty dictionary
        self.transactions={
            "expenses":{},
            "income":{}
        }
    def storetransaction(self,type,category,cost,desc,date):
        transaction = {
            "category":category,
            "Cost":cost,
            "Description":desc,
            "Date":date
        }
        if type == "expenses":
            self.transactions['expenses'].append(transaction)
        else:
            self.transactions['income'].append(transaction)
        return True
    
    def view_transactions(self):
        print("INCOME")
        for abc in self.transactions['income']:
            print(abc)
        print("EXPENSES")
        for abc in self.transactions['expenses']:
            print(abc)

    def total_incomeexpense(self):
        print("Total Income")
        total_income=0
        for income in self.transactions['income']:
            print(income["Cost"])
        print(total_income)
        print("Total Expense") 
        total_expense=0
        for expense in self.transactions['income']:
            print(expense["Cost"])
        print(total_expense)  

mytransactions=expensetracker()
mytransactions.storetransaction("income","Salary",10000,"Salary credited","01/09/2023")
mytransactions.storetransaction("expense","Electricity Bill",4500,"MDHC","05/09/2023")
mytransactions.storetransaction("income","Pocket money",10500,"from parents","07/09/2023")
mytransactions.storetransaction("expense","Bday Treat",5000,"To friends","07/09/2023")

mytransactions.view_transactions()
mytransactions.total_incomeexpense()