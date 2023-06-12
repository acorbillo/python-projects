import re
import datetime

def income_statement():

    income_inputs = []
    expense_inputs = []

    print("when inputting, press enter to input another data...")
    print("if done inputting all data input 'd' ")

    try:
        while True:
            i = input("enter income: ")
            i = re.sub(",","", i)
            if i.isdigit() == True:
                income_inputs.append(float(i))
            elif i == "d":
                break
            #print(income_inputs)

        while True:
            e = input("enter expenses: ")
            e = re.sub(",","", e)
            if e.isdigit() == True:
                expense_inputs.append(float(e))
            elif i == "d":
                break
            #print(expense_inputs)
    except ValueError:
        print("invalid input")

    sum_income = sum(income_inputs)
    sum_expense = sum(expense_inputs)

    date = datetime.datetime.now()
    x = date.strftime("%x")
    balance = sum_income - sum_expense

    print("====================================================================")
    print("your income - expense is", "{:,}".format(balance), "as of", x)
    print("====================================================================")

    result = str(balance) + " as of " + str(x)
    balance_inputs = []
    balance_inputs.append(result)
    #print(balance_inputs)

income_statement()
