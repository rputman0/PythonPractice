import math

#get the total change from the user
def getTotalChange(pennies, nickles, dimes, quarters):
    pennies *= .01
    nickles *= .05
    dimes *= .10
    quarters *= .25
            
    total = quarters + nickles + dimes + pennies
    print('${:.2f}'.format(total))

#get the minimum amount of change
def minCoins(cents):
    pennies = nickles = dimes = quarters = 0
    while(cents > 0):
        if(cents%25 == 0):
            quarters += 1
            cents -= 25
        elif(cents%10 == 0):
            dimes += 1
            cents -= 10
        elif(cents%5 == 0):
            nickles += 1
            cents -= 5
        elif(cents%1 == 0):
            pennies += 1
            cents -= 1

    print("Quarters: ",quarters," Dimes: ",dimes,
      "\nNickles: ",nickles,"  Pennies: ",pennies)

getTotalChange(2,2,3,4)
