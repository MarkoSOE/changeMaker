#Version 0.1

# ChangeMaker propmpts the user to enter an amount of dollars and cents. The program then displays the number of quarters, dimes, nickles, and pennies to make that amount

# Ask the user for the input
enteramount = round(float(input('What is the amount of money you need change for: '))*100)

#initialize variables
quarters=dimes=nickels=cents = 0

#set up while loops to continuously keep track of coins and adjust the amount until zero
while enteramount >= 25:
    quarters += 1
    enteramount -= 25

while enteramount >= 10:
    dimes +=1
    enteramount -= 10

while enteramount >= 5:
    nickels +=1
    enteramount -=5

while enteramount >=1:
    cents += 1
    enteramount -= 1

#return the change amount
print("Your change would be {} quarters, {} dimes, {} nickles, {} cents".format(int(quarters), int(dimes), int(nickels), int(cents)))