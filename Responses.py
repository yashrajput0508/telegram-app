data=[
"""Hey! I’m Nerd - your budgeting assistant. I’ll help setup budget, weekly targets and keep you on track. Select a goal to begin
Type option number
1. New Gadget, vacation etc
2. Investing money
3. Building emergency fund
4. Paying off debt
5. Just saving"""
,

"""
Your Income & Pay date?
Type (eg): 15000, 27

Income is salary/ allowance/ stipend etc per month
"""
,

"""
Monthly Investments (SIP etc)

Enter total amount
"""
,

"""
Expenses every month?

Home: Rent, Maids, Cook etc.
Bills: Electricity, Water, DTH, Landline, Mobile, Wifi, Gas etc.
EMI: Loans, Insurance etc.

Enter total amount

(Don't include credit card bill payment, grocery)
"""
,

"""
income : {income}
Pay date : {pay date}
Monthly Investments : {monthly investments} 
Expenses : {expenses}

type Y for contunue type N for input again.
"""
]
import database as db
def sample_responses(input_text, id):
    f = db.get_pos(id)
    if input_text=="restart":
        db.set_pos(str(id),"0")
        db.create_db(str(id))
        return data[0]
    elif f=='0':
        if input_text in ['1','2','3','4','5']:
            db.set_pos(str(id),"1")
            return data[1]
        else:
            return "Enter value between 1 to 5"
    elif f=='1':
        try:
            val = input_text.split(",")
            val[0] = val[0].strip(" ")
            val[1] = val[1].strip(" ")
            if 1 <= int(val[1]) <= 31:
                income, paydate = str(val[0]), str(val[1])
                db.update1(id, income, paydate)
                db.set_pos(str(id),"2")
                return data[2]
            else:
                return "Enter valid Date"
        except:
            return "enter correct income value"

    elif f=='2':
        invest = input_text
        try:
            invest_1 = int(invest)
            if int(db.get_value(id)['income'])>=invest_1:
                db.update2(id, invest)
                db.set_pos(str(id),"3")
                return data[3]
            else:
                return "Monthly Investments greater than income"
        except:
            return "enter correct invest value"

    elif f=='3':
        expenses = input_text
        try:
            if int(db.get_value(id)['income'])>=(int(db.get_value(id)['Monthly Investments'])+int(expenses)):
                db.update3(id, expenses)
                db.set_pos(str(id),"4")
                val = db.get_value(id)
                income, pay_date, invest, expenses=val['income'], val['Pay date'], val['Monthly Investments'], val['Expenses']
                return f"""
                        income : {income}
Pay date : {pay_date}
Monthly Investments : {invest} 
Expenses : {expenses}
        
type Y for contunue type N for input again.
                        """
            else:
                return "Please enter less expenses"
        except:
            return "Please enter valid value"
    elif f=='4':
        if input_text=='y':
            return "Awesome"
        elif input_text=="n":
            db.set_pos(str(id),"0")
            db.reset(id)
            return data[0]
        else:
            return "type Y for contunue type N for input again."

