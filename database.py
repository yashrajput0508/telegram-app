from pymongo import MongoClient
client = MongoClient("mongodb+srv://test:test@cluster0.25kge.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
df = client.get_database('chatbot')
records = df.user_record
"""new_record = {
    "income" : "None",
    "Pay date" : "None",
    "Monthly Investments" : "None",
    "Expenses" : "None"
}"""



def update1(income, pay_date):
    new_record = {
        "income": str(income),
        "Pay date": str(pay_date),
    }
    records.update_many({'id':'1'},{'$set':new_record})

def update2(invest):
    new_record = {
    "Monthly Investments" : str(invest),
    }
    records.update_one({'id': '1'}, {'$set': new_record})

def update3(expenses):
    new_record = {
    "Expenses" : str(expenses)
    }
    records.update_one({'id': '1'}, {'$set': new_record})

def get_data():
    return records.find_one({'id':'1'})

def reset():
    new_record = {
        "income" : "None",
        "Pay date" : "None",
        "Monthly Investments" : "None",
        "Expenses" : "None"
    }
    records.update_many({'id': '1'}, {'$set': new_record})

def get_value():
    return records.find_one({'id':'1'})