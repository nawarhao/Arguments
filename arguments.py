def total_calc(bill_amount, tip_perc):
#define function to calculate the tip on the bill
    total = bill_amount*(1+0.01*tip_perc)
    total = round(total,2)
    print(f"Please pay ${total}")
    
#specify only bill_amount
#default value of tip percentage is used

total_calc(150,20)

#define function to calculate cube
def cube(number):
    return number*number*number

#define a function which will execute cube function if the user entered number is divisible by 3
def by_three(number):
    if number %3 == 0:
        return cube(number)
    else:
        return False

#display result
print(by_three(9))
print(by_three(4))

#Factorials!

def factorial(x):
    '''this is a recursive function to find the factorial of an integer'''
    
    if x==0 or x==1:
        return 1
    else:
        #calling function inside a function
        return x*factorial(x-1)
        
#display result
print(factorial.__doc__)
print(f"the factorial of 0: {factorial(0)}")
print(f"the factorial of 1: {factorial(1)}")
print(f"the factorial of 2: {factorial(4)}")
print(f"the factorial of 5: {factorial(5)}")
print(f"the factorial of 10: {factorial(10)}")