class Inputs:             # THIS CLASS WILL HOLD ALL THE DATA
    # knownlist = [
    # ['rental', 'laundry', 'storage', 'misc'],     #cycle though list and gather inputs add to init dict
    # ['tax', 'insurance', 'electric', 'water', 'sewer', 'garbage', 'gas','HOA fee', 'lawn/snow','vacancy (5"%" rental income)','repairs', 'CapEx', 'Property management', 'mortgage'],
    # ['down payment', 'closing costs', 'rehab budget', 'misc(other)']
    # ]
    knownlist = [
    ['rental'],     # FOR TESTING
    ['tax'],
    ['down payment']
    ]
    def __init__(self, name, password):
        self.income = {}
        self.expenses = {}
        self.capex = {}
        self.name = name
        self.password = input("Please assign a case-sentive password to your account. Must be more than 4 characters!  ")
        for x in self.knownlist[0]:  # income dict creater
            answer = input(f"What is your expected {x} income> ")
            self.income[x.title()] = answer
        for x in self.knownlist[1]:    # expense dict creater
            answer = input(f"What is your expected {x} expense> ")
            self.expenses[x.title()] = answer
        for x in self.knownlist[2]:    # capex dict creater
            answer = input(f"What is your expected {x} payment> ")
            self.capex[x.title()] = answer

    def edit(self, answer): # This will edit any data
        response = ''
        if answer == 'i':
            self.display("1")
            while response.title() not in self.income:
                response = input(f'Which item would you like to adjust? ')
            new_value = input(f'What is the new value for {response.title()}?  ')
            self.income[response.title()] = new_value
            print(f'This is your new data set {self.display("1")}')
        if answer == 'e':
            self.display("2")
            while response.title() not in self.expenses:
                response = input(f'Which item would you like to adjust? ')
            new_value = input(f'What is the new value for {response.title()}?  ')
            self.expenses[response.title()] = new_value
            print(f'This is your new data set {self.display("2")}')
        if answer == 'p':
            self.display("3")
            while response.title() not in self.capex:
                response = input(f'Which item would you like to adjust? ')
            new_value = input(f'What is the new value for {response.title()}?  ')
            self.capex[response.title()] = new_value
            print(f'This is your new data set {self.display("3")}')

    def display(self, input_dict=None):                                        
        if input_dict == '1':
            income_total = 0
            income_str = '=============================\n'   # Item to be returned
            for x, y in self.income.items():
                income_str += f"{x}, ${y}\n--------------------------------------\n"   # Build the return item
                income_total = int(y) + income_total
            income_str += f"Your Total Income Expense is : ${income_total}"
            income_str += '============================='
            return income_str
        if input_dict == '2':
            expense_total = 0
            expense_str = ''   # Item to be returned
            for x, y in self.expenses.items():
                expense_str += f"{x}, ${y}\n--------------------------------------\n"   # Build the return item
                expense_total = int(y) + expense_total
            expense_str += f"Your Total Income Expense is : ${expense_total}"
            expense_str += '============================='
            return expense_str
        if input_dict == '3':
            capex_total = 0
            capex_str = ''   # Item to be returned
            for x, y in self.capex.items():
                capex_str += f"{x}, ${y}\n--------------------------------------\n"     # Build the return item
                capex_total = int(y) + capex_total
            capex_str += f"Your Total Income Expense is : ${capex_total}"
            capex_str += '============================='
            return capex_str

        if input_dict == '4':
    
            income_total = 0
            ROI_str = '=============================\n'   # Item to be returned
            for x, y in self.income.items():
                ROI_str += f"{x}, ${y}\n--------------------------------------\n"   # Build the return item
                income_total = int(y) + income_total
            ROI_str += f"Your Total Income Expense is : ${income_total}"
            ROI_str += '============================='
            
            expense_total = 0  # Item to be returned
            for x, y in self.expenses.items():
                ROI_str += f"{x}, ${y}\n--------------------------------------\n"   # Build the return item
                expense_total = int(y) + expense_total
            ROI_str += f"Your Total Income Expense is : ${expense_total}"
            ROI_str += '============================='
            
            capex_total = 0   # Item to be returned
            for x, y in self.capex.items():
                ROI_str += f"{x}, ${y}\n--------------------------------------\n"     # Build the return item
                capex_total = int(y) + capex_total
            ROI_str += f"Your Total Income Expense is : ${capex_total}"
            ROI_str += '============================='
            ROI_str += '============================='
            ROI_str += f"Your total Return on Investment is {((income_total-expense_total)*12)/capex_total}"
            return ROI_str