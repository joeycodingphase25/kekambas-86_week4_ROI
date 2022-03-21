
#         -annual cash flow (monthly x 12): 390 * 12 = 4680
#         annual cash flow / total investment 4680 / 50000 = 9.36 % (0.0936 * 100)
#     ----Cash on Cash ROI = 9.36 %----

#layout

class Container: #contains financial plans
    def __init__(self) -> None:
        self.plans = {}   # This will assign  'name': INPUT OBJECT
    def append(self, object):
        self.plans[object.name] = object
    def __str__(self): # See all the name-holders for the financial plan
        names = '\n'
        for x in self.plans.keys():
            names += f"-{x}-\n-------------------\n"
        return names 

class Inputs:             # THIS CLASS WILL HOLD ALL THE DATA
    # knownlist = [
    # ['rental', 'laundry', 'storage', 'misc'],     #cycle though list and gather inputs add to init dict
    # ['tax', 'insurance', 'electric', 'water', 'sewer', 'garbage', 'gas','HOA fee', 'lawn/snow','vacancy (5"%" rental income)','repairs', 'CapEx', 'Property management', 'mortgage'],
    # ['down payment', 'closing costs', 'rehab budget', 'misc(other)']
    # ]
    knownlist = [
    ['rental', 'laundry'],     # FOR TESTING
    ['tax', 'insurance'],
    ['down payment', 'closing costs']
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
            print(self.display("1"))
            while response.title() not in self.income:
                response = input(f'Which item would you like to adjust? ')
            new_value = input(f'What is the new value for {response.title()}?  ')
            self.income[response.title()] = new_value
            print(f'This is your new data set {self.display("1")}')
        if answer == 'e':
            print(self.display("2"))
            while response.title() not in self.expenses:
                response = input(f'Which item would you like to adjust? ')
            new_value = input(f'What is the new value for {response.title()}?  ')
            self.expenses[response.title()] = new_value
            print(f'This is your new data set {self.display("2")}')
        if answer == 'p':
            print(self.display("3"))
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
            income_str += f"Your Total Income Expense is : ${income_total}\n"
            income_str += '============================='
            return income_str
        if input_dict == '2':
            expense_total = 0
            expense_str = ''   # Item to be returned
            for x, y in self.expenses.items():
                expense_str += f"{x}, ${y}\n--------------------------------------\n"   # Build the return item
                expense_total = int(y) + expense_total
            expense_str += f"Your Total Income Expense is : ${expense_total}\n"
            expense_str += '============================='
            return expense_str
        if input_dict == '3':
            capex_total = 0
            capex_str = ''   # Item to be returned
            for x, y in self.capex.items():
                capex_str += f"{x}, ${y}\n--------------------------------------\n"     # Build the return item
                capex_total = int(y) + capex_total
            capex_str += f"Your Total Income Expense is : ${expense_total}\n"
            capex_str += '============================='
            return capex_str

        if input_dict == '4':
    
            income_total = 0
            expense_total = 0
            capex_total = 0

            ROI_str = '=============================\n'   # Item to be returned
            for x, y in self.income.items():
                ROI_str += f"{x}, ${y}\n--------------------------------------\n"   # Build the return item
                income_total += int(y) + income_total
            ROI_str += f"Your Total Income Expense is : ${income_total}\n"
            ROI_str += '=============================\n'
            
            for x, y in self.expenses.items():
                ROI_str += f"{x}, ${y}\n--------------------------------------\n"   # Build the return item
                expense_total += int(y) + expense_total
            ROI_str += f"Your Total Expense is : ${expense_total}\n"
            ROI_str += '=============================\n'
       # Item to be returned
            for x, y in self.capex.items():
                ROI_str += f"{x}, ${y}\n--------------------------------------\n"     # Build the return item
                capex_total += int(y) + capex_total
            ROI_str += f"Your Total Capital Expense is : ${capex_total}\n"
            ROI_str += '=============================\n'
            ROI_str += '=============================\n'
            ROI_str += f"Your total Return on Investment is {((income_total-expense_total)*12)/capex_total}%"
            return ROI_str

# ROI is (income - expenses) *12 /total investment
holders = Container() # initialize a global variable that will hold my input objects

def main():
    password = '' # set as a variable
    while True:
        answer = input("What would you like to do? New Plan 'p', Edit 'e', Quit 'q' -->")
        if answer.lower() == 'p':
            name = input("Please give your name to help us properly hold your plan!  ")
            while len(password) < 4:  # a quick loop to ensure password is secure
                password = input("Please assign a case-sentive password to your account. Must be more than 4 characters!  ")
            name = Inputs(name, password)   # INPUT OBJECT <------------------------------
            holders.append(name)  # adds inputs object to hodlers list
            print(f"Thank you, your account plan has been added to our system {name.name.title()}!!")
        if answer.lower() == 'e':
            account = ''
            if holders.plans == None:
                print("Our records show there is no plans on file")
            while account not in holders.plans:
                 account = input(f"Which portfolio would you like to edit? {holders}") # create a display function
            if account in holders.plans:
                attempt = input(f"Please enter the password associated with {account}!  ")
                if attempt == holders.plans[account].password:   # security check

                    while True:  # EDITING MENU
                        answer = input("Welcome to edit Menu, what woul you like to do? Review Plan 'r', Edit Income 'i', Edit Expense 'e', Edit payment 'p', Quit to main 'q'  ")
                        if answer.lower() == 'r':
                            print(name.display('4'))  #********************MAKE THIS STILL IN THE DISPLAY FUNCTION
                        if answer.lower() == 'i':
                            name.edit('i')
                        if answer.lower() == 'e':
                           name.edit('e')
                        if answer.lower() == 'p':
                            name.edit('p')
                        if answer.lower() == 'q':
                            main()
                        # else:
                        #     print('Invalid input recieved, please review main menu and try again!')   #You will use the def edit() function and this section will be really clean
                else:
                    print("You have entered an invalid password. Try Again")
            break
        if answer.lower() == 'q':
            break

main()

