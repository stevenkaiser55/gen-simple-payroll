# Python Final Project
# Steven Kaiser
# CC 1.0

# Description:
# ACME Corporation needs a simple payroll program written in Python.
# The Input Items are the following: Employee Name
#    Hours worked
#    Pay Rate (hourly)
#    Employees are to receive 1.5x pay rate for hours over 40
#    Fed Tax = 10% State tax = 3% FICA rate = 7%
# The program output should be the following:
#   Name Hours Rate Grosspay Fed Tax State Tax FICA Netpay
# Bonus points if program can process 5 employees’ inputs before program ends intrigue
#   Hints: E =1
#   E= 1 + E While E != 5


# The Input Items for Employee 1
def gather_info1 ():
    name1 = input("What is the name of employee 1: ")
    rate1 = int(input("What is the hourly pay rate for employee 1: "))
    hours1 = int(input("Number of regular hours employee 1 worked for the week: "))
    over1 = int(input("Number of overtime hours employee 1 worked for the week: "))
     
    return (name1, rate1, hours1, over1)

# The Input Items for Employee 2
def gather_info2 ():
    name2 = input("What is the name of employee 2: ")
    rate2 = int(input("What is the hourly pay rate for employee 2: "))
    hours2 = int(input("Number of regular hours employee 2 worked for the week: "))
    over2 = int(input("Number of overtime hours employee 2 worked for the week: "))
     
    return (name2, rate2, hours2, over2)

# The Input Items for Employee 3
def gather_info3 ():
    name3 = input("What is the name of employee 3: ")
    rate3 = int(input("What is the hourly pay rate for employee 3: "))
    hours3 = int(input("Number of regular hours employee 3 worked for the week: "))
    over3 = int(input("Number of overtime hours employee 3 worked for the week: "))
     
    return (name3, rate3, hours3, over3)

# The Input Items for Employee 4
def gather_info4 ():
    name4 = input("What is the name of employee 4: ")
    rate4 = int(input("What is the hourly pay rate for employee 4: "))
    hours4 = int(input("Number of regular hours employee 4 worked for the week: "))
    over4 = int(input("Number of overtime hours employee 4 worked for the week: "))
     
    return (name4, rate4, hours4, over4)

# The Input Items for Employee 5
def gather_info5 ():
    name5 = input("What is the name of employee 5: ")
    rate5 = int(input("What is the hourly pay rate for employee 5: "))
    hours5 = int(input("Number of regular hours employee 5 worked for the week: "))
    over5 = int(input("Number of overtime hours employee 5 worked for the week: "))
     
    return (name5, rate5, hours5, over5)

# Calculate for Employee 1
def calculate_regpay1(rate1, hours1):
    regpay1 = (hours1 * rate1)
    return (regpay1)

def calculate_overpay1(rate1, over1):
    overpay1 = int((over1 * rate1 * 1.5))
    return (overpay1)

def calculate_grosspay1(regpay1, overpay1):
    grosspay1 = (regpay1 + overpay1)
    return (grosspay1)

def calculate_fedtax1(grosspay1):
    fedtax1 = int((grosspay1 * .1))
    return (fedtax1)

def calculate_statetax1(grosspay1):
    statetax1 = int((grosspay1 * .03))
    return (statetax1)

def calculate_fica1(grosspay1):
    fica1 = int((grosspay1 * .07))
    return (fica1)
    
def calculate_netpay1(grosspay1, fedtax1, statetax1, fica1):
    netpay1 = (grosspay1 - fedtax1 - statetax1 - fica1)
    return (netpay1)

# Calculate for Employee 2
def calculate_regpay2(rate2, hours2):
    regpay2 = (hours2 * rate2)
    return (regpay2)

def calculate_overpay2(rate2, over2):
    overpay2 = int((over2 * rate2 * 1.5))
    return (overpay2)

def calculate_grosspay2(regpay2, overpay2):
    grosspay2 = (regpay2 + overpay2)
    return (grosspay2)

def calculate_fedtax2(grosspay2):
    fedtax2 = int((grosspay2 * .1))
    return (fedtax2)

def calculate_statetax2(grosspay2):
    statetax2 = int((grosspay2 * .03))
    return (statetax2)

def calculate_fica2(grosspay2):
    fica2 = int((grosspay2 * .07))
    return (fica2)
    
def calculate_netpay2(grosspay2, fedtax2, statetax2, fica2):
    netpay2 = (grosspay2 - fedtax2 - statetax2 - fica2)
    return (netpay2)

# Calculate for Employee 3
def calculate_regpay3(rate3, hours3):
    regpay3 = (hours3 * rate3)
    return (regpay3)

def calculate_overpay3(rate3, over3):
    overpay3 = int((over3 * rate3 * 1.5))
    return (overpay3)

def calculate_grosspay3(regpay3, overpay3):
    grosspay3 = (regpay3 + overpay3)
    return (grosspay3)

def calculate_fedtax3(grosspay3):
    fedtax3 = int((grosspay3 * .1))
    return (fedtax3)

def calculate_statetax3(grosspay3):
    statetax3 = int((grosspay3 * .03))
    return (statetax3)

def calculate_fica3(grosspay3):
    fica3 = int((grosspay3 * .07))
    return (fica3)
    
def calculate_netpay3(grosspay3, fedtax3, statetax3, fica3):
    netpay3 = (grosspay3 - fedtax3 - statetax3 - fica3)
    return (netpay3)

# Calculate for Employee 4
def calculate_regpay4(rate4, hours4):
    regpay4 = (hours4 * rate4)
    return (regpay4)

def calculate_overpay4(rate4, over4):
    overpay4 = int((over4 * rate4 * 1.5))
    return (overpay4)

def calculate_grosspay4(regpay4, overpay4):
    grosspay4 = (regpay4 + overpay4)
    return (grosspay4)

def calculate_fedtax4(grosspay4):
    fedtax4 = int((grosspay4 * .1))
    return (fedtax4)

def calculate_statetax4(grosspay4):
    statetax4 = int((grosspay4 * .03))
    return (statetax4)

def calculate_fica4(grosspay4):
    fica4 = int((grosspay4 * .07))
    return (fica4)
    
def calculate_netpay4(grosspay4, fedtax4, statetax4, fica4):
    netpay4 = (grosspay4 - fedtax4 - statetax4 - fica4)
    return (netpay4)

# Calculate for Employee 5
def calculate_regpay5(rate5, hours5):
    regpay5 = (hours5 * rate5)
    return (regpay5)

def calculate_overpay5(rate5, over5):
    overpay5 = int((over5 * rate5 * 1.5))
    return (overpay5)

def calculate_grosspay5(regpay5, overpay5):
    grosspay5 = (regpay5 + overpay5)
    return (grosspay5)

def calculate_fedtax5(grosspay5):
    fedtax5 = int((grosspay5 * .1))
    return (fedtax5)

def calculate_statetax5(grosspay5):
    statetax5 = int((grosspay5 * .03))
    return (statetax5)

def calculate_fica5(grosspay5):
    fica5 = int((grosspay5 * .07))
    return (fica5)
    
def calculate_netpay5(grosspay5, fedtax5, statetax5, fica5):
    netpay5 = (grosspay5 - fedtax5 - statetax5 - fica5)
    return (netpay5)

# Begin Output
while True:

# Output Employee 1
    name1, rate1, hours1, over1 = gather_info1()
    regpay1 = calculate_regpay1(rate1, hours1)
    overpay1 = calculate_overpay1(rate1, over1)
    grosspay1 = calculate_grosspay1(regpay1, overpay1)
    fedtax1 = calculate_fedtax1(grosspay1)
    statetax1 = calculate_statetax1(grosspay1)
    fica1 = calculate_fica1(grosspay1)
    netpay1 = calculate_netpay1(grosspay1, fedtax1, statetax1, fica1)
    print(f"Employee 1 Name: {name1}")
    print(f"Employee 1 Hours: {hours1}")
    print(f"Employee 1 Rate: {rate1}")
    print(f"Employee 1 Grosspay: {grosspay1}")
    print(f"Employee 1 Fed Tax: {fedtax1}")
    print(f"Employee 1 State Tax: {statetax1}")
    print(f"Employee 1 Fica: {fica1}")
    print(f"Employee 1 Net Pay: {netpay1}")

# Output Employee 2
    name2, rate2, hours2, over2 = gather_info2()
    regpay2 = calculate_regpay2(rate2, hours2)
    overpay2 = calculate_overpay2(rate2, over2)
    grosspay2 = calculate_grosspay2(regpay2, overpay2)
    fedtax2 = calculate_fedtax2(grosspay2)
    statetax2 = calculate_statetax2(grosspay2)
    fica2 = calculate_fica2(grosspay2)
    netpay2 = calculate_netpay2(grosspay2, fedtax2, statetax2, fica2)
    print(f"Employee 2 Name: {name2}")
    print(f"Employee 2 Hours: {hours2}")
    print(f"Employee 2 Rate: {rate2}")
    print(f"Employee 2 Grosspay: {grosspay2}")
    print(f"Employee 2 Fed Tax: {fedtax2}")
    print(f"Employee 2 State Tax: {statetax2}")
    print(f"Employee 2 Fica: {fica2}")
    print(f"Employee 2 Net Pay: {netpay2}")

# Output Employee 3
    name3, rate3, hours3, over3 = gather_info3()
    regpay3 = calculate_regpay3(rate3, hours3)
    overpay3 = calculate_overpay3(rate3, over3)
    grosspay3 = calculate_grosspay3(regpay3, overpay3)
    fedtax3 = calculate_fedtax3(grosspay3)
    statetax3 = calculate_statetax3(grosspay3)
    fica3 = calculate_fica3(grosspay3)
    netpay3 = calculate_netpay3(grosspay3, fedtax3, statetax3, fica3)
    print(f"Employee 3 Name: {name3}")
    print(f"Employee 3 Hours: {hours3}")
    print(f"Employee 3 Rate: {rate3}")
    print(f"Employee 3 Grosspay: {grosspay3}")
    print(f"Employee 3 Fed Tax: {fedtax3}")
    print(f"Employee 3 State Tax: {statetax3}")
    print(f"Employee 3 Fica: {fica3}")
    print(f"Employee 3 Net Pay: {netpay3}")

# Output Employee 4
    name4, rate4, hours4, over4 = gather_info4()
    regpay4 = calculate_regpay4(rate4, hours4)
    overpay4 = calculate_overpay4(rate4, over4)
    grosspay4 = calculate_grosspay4(regpay4, overpay4)
    fedtax4 = calculate_fedtax4(grosspay4)
    statetax4 = calculate_statetax4(grosspay4)
    fica4 = calculate_fica4(grosspay4)
    netpay4 = calculate_netpay4(grosspay4, fedtax4, statetax4, fica4)
    print(f"Employee 4 Name: {name4}")
    print(f"Employee 4 Hours: {hours4}")
    print(f"Employee 4 Rate: {rate4}")
    print(f"Employee 4 Grosspay: {grosspay4}")
    print(f"Employee 4 Fed Tax: {fedtax4}")
    print(f"Employee 4 State Tax: {statetax4}")
    print(f"Employee 4 Fica: {fica4}")
    print(f"Employee 4 Net Pay: {netpay4}")

# Output Employee 5
    name5, rate5, hours5, over5 = gather_info5()
    regpay5 = calculate_regpay5(rate5, hours5)
    overpay5 = calculate_overpay5(rate5, over5)
    grosspay5 = calculate_grosspay5(regpay5, overpay5)
    fedtax5 = calculate_fedtax5(grosspay5)
    statetax5 = calculate_statetax5(grosspay5)
    fica5 = calculate_fica5(grosspay5)
    netpay5 = calculate_netpay5(grosspay5, fedtax5, statetax5, fica5)
    print(f"Employee 5 Name: {name5}")
    print(f"Employee 5 Hours: {hours5}")
    print(f"Employee 5 Rate: {rate5}")
    print(f"Employee 5 Grosspay: {grosspay5}")
    print(f"Employee 5 Fed Tax: {fedtax5}")
    print(f"Employee 5 State Tax: {statetax5}")
    print(f"Employee 5 Fica: {fica5}")
    print(f"Employee 5 Net Pay: {netpay5}")
    
    break