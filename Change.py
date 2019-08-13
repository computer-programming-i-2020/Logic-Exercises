'''
Created on Jul 23, 2019

@author: karl
'''

def main():
    print("Enter an amount of money to convert to change")
    change = countChange(input())
    print("Quarters: " + str(change[0]))
    print("Dimes: " + str(change[1]))
    print("Nickels: " + str(change[2]))
    print("Pennies: " + str(change[3]))
    

def countChange(value):
    value = float(value)
    quarters = int(value // .25)
    value = value % .25
    dimes = int(value // .1)
    value = value % .1
    nickels = int(value // .05)
    value = value % .05
    pennies = int(value // .01)
    return([quarters, dimes, nickels, pennies])

if __name__ == "__main__":
    main()