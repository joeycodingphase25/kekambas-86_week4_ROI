
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

        pass

    def edit(self): # This will edit any data
        pass

    # def __str__(self, input_dict=None): #WIll build display function based off input value, used to help edit() function
    #     if input_dict == '1':
    #         income_str = ''   # Item to be returned
    #         for x, y in self.income.items():
    #             income_str += f"{x}, ${y}\n--------------------------------------\n"   # Build the return item
    #         return income_str
    #     if input_dict == '2':
    #         expense_str = ''   # Item to be returned
    #         for x, y in self.expenses.items():
    #             expense_str += f"{x}, ${y}\n--------------------------------------\n"   # Build the return item
    #         return expense_str
    #     if input_dict == '3':
    #         capex_str = ''   # Item to be returned
    #         for x, y in self.capex.items():
    #             capex_str += f"{x}, ${y}\n--------------------------------------\n"     # Build the return item
    #         return capex_str
    #     if input_dict == '4':
    #         pass  #print all options
    #     return "1 argument, but zero were given"  # Built in Error Handling
        

    def display(self, input_dict=None):                                        
        if input_dict == '1':
            income_str = '=============================\n'   # Item to be returned
            for x, y in self.income.items():
                income_str += f"{x}, ${y}\n--------------------------------------\n"   # Build the return item
            income_str += '============================='
            return income_str
        if input_dict == '2':
            expense_str = ''   # Item to be returned
            for x, y in self.expenses.items():
                expense_str += f"{x}, ${y}\n--------------------------------------\n"   # Build the return item
            return expense_str
        if input_dict == '3':
            capex_str = ''   # Item to be returned
            for x, y in self.capex.items():
                capex_str += f"{x}, ${y}\n--------------------------------------\n"     # Build the return item
            return capex_str
        if input_dict == '4':
            pass  #print all options
        return "1 argument, but zero were given"  # Built in Error Handling

holders = Container() # initialize a global variable that will hold my input objects
def main():
    password = '' # set as a variable
    while True:
        answer = input("What would you like to do? New Plan 'p', Edit 'e', Quit 'q' -->")
        if answer.lower() == 'p':
            name = input("Please give your name to help us properly hold your plan!  ")
            while len(password) < 4:  # a quick loop to ensure password is secure
                password = input("Please assign a case-sentive password to your account. Must be more than 4 characters!  ")
            name = Inputs(name, password)   # creates all the values and adds to object name
            holders.append(name)  # adds inputs object to hodlers list
            print(f"Thank you, your account plan has been added to our system {name.name.title()}!!")
        if answer.lower() == 'e':
            account = input(f"Which portfolio would you like to edit? {holders}") # create a display function
            if holders.plans == None:
                print("Our records show there is no plans on file")
            if account in holders.plans:
                attempt = input(f"Please enter the password associated with {account}!  ")
                if attempt == holders.plans[account].password:
                    answer = input('Which section would you like to edit?  ')
                    break   #You will use the def edit() function and this section will be really clean
                else:
                    print("You have entered an invalid password. Try Again")
            break
        if answer.lower() == 'q':
            break

main()