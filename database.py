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

def create_db(id):
    new_record = {
        "id": str(id),
        "pos":"0",
        "income": "None",
        "Pay date": "None",
        "Monthly Investments": "None",
        "Expenses": "None"
    }

    try:
        if records.find_one({'id':str(id)})==None:
            records.insert_one(new_record)
        else:
            records.update_many({'id':str(id)},{'$set':new_record})
    except:
        records.update_many({'id': str(id)}, {'$set': new_record})

def get_pos(id):
    return records.find_one({'id': str(id)})['pos']

def set_pos(id, pos):
    new_record = {
        "pos":str(pos)
    }
    records.update_one({'id': str(id)}, {'$set': new_record})

def update1(id, income, pay_date):
    new_record = {
        "income": str(income),
        "Pay date": str(pay_date),
    }
    records.update_many({'id':str(id)},{'$set':new_record})

def update2(id, invest):
    new_record = {
    "Monthly Investments" : str(invest),
    }
    records.update_one({'id': str(id)}, {'$set': new_record})

def update3(id, expenses):
    new_record = {
    "Expenses" : str(expenses)
    }
    records.update_one({'id': str(id)}, {'$set': new_record})

def get_data(id):
    return records.find_one({'id':str(id)})

def reset(id):
    new_record = {
        "pos":"0",
        "income" : "None",
        "Pay date" : "None",
        "Monthly Investments" : "None",
        "Expenses" : "None"
    }
    records.update_many({'id': str(id)}, {'$set': new_record})

def get_value(id):
    return records.find_one({'id':str(id)})