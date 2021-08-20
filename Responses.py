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
def sample_responses(input_text):

    with open("file.txt",'r') as value:
        f = value.readlines()[0]
        value.close()
    if input_text=="restart":
        with open("file.txt", 'w') as f:
            f.write('0')
            f.close()
        db.reset()
        return data[0]
    elif f=='0':
        if input_text in ['1','2','3','4','5']:
            with open("file.txt", 'w') as f:
                f.write('1')
                f.close()
            return data[1]
        else:
            return "Enter valid value"
    elif f=='1':
        try:
            val = input_text.split(",")
            income, paydate = str(val[0]), str(val[1])
            db.update1(income, paydate)
            with open("file.txt", 'w') as f:
                f.write('2')
                f.close()
            return data[2]
        except:
            return "Enter valid format"

    elif f=='2':
        invest = input_text
        try:
            invest_1 = int(invest)
            if int(db.get_value()['income'])>=invest_1:
                db.update2(invest)
                with open("file.txt", 'w') as f:
                    f.write('3')
                    f.close()
                return data[3]
            else:
                return "Monthly Investments greater than income"
        except:
            return "Enter valid value"

    elif f=='3':
        expenses = input_text
        try:
            if int(db.get_value()['income'])>=(int(db.get_value()['Monthly Investments'])+int(expenses)):
                db.update3(expenses)
                with open("file.txt", 'w') as f:
                    f.write('4')
                    f.close()
                val = db.get_value()
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
            with open("file.txt", 'w') as f:
                f.write('0')
                f.close()
            db.reset()
            return data[0]
        else:
            return "type Y for contunue type N for input again."
