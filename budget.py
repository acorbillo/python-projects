class Budget:

    def budget():


        import datetime

        income_inputs = []
        expense_inputs = []
        savings_inputs = []

        while True:

            income = float(input("enter your monthly income: "))
            expense = float(input("enter your monthly expenses: "))
            savings = income - expense

            income_inputs.append(income)
            expense_inputs.append(expense)
            savings_inputs.append(savings)

            sum_income_inputs = sum(income_inputs)
            sum_expense_inputs = sum(expense_inputs)
            sum_savings_inputs = sum(savings_inputs)

            date = datetime.datetime.now()
            x = date.strftime("%x")

            print("=======================================================")
            print("your total income is", sum_income_inputs, "as of", x)
            print("-------------------------------------------------------")
            print("your total expenses is", sum_expense_inputs, "as of", x)
            print("-------------------------------------------------------")
            print("your total savings is", sum_savings_inputs, "as of", x)
            print("=======================================================")
            # print(income_inputs)
            # print(expense_inputs)
            # print(savings_inputs)

            if len(savings_inputs) == 12:
                break

    budget()


