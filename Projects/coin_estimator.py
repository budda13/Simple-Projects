# Without manually calculating tests, I'm not 100% this is right
# but it seems to be running correctly.
# Obviously I didn't verify correct inputs...in real life situation,
# that would be a for sure change.
# I wanted to .append() the coin_amount and wrapper_amount, but it didn't
# seem to like appending two items in this manner. And couldn't [i] like I
# wanted due to (at the time) the lists being empty. But with it only being 4
# items, and only ever four items, the method used isn't an issue, imo.

import math

PWEIGHT, NWEIGHT, DWEIGHT, QWEIGHT = 2.5, 5, 2.268, 5.67
PWRAPPER, NWRAPPER, DWRAPPER, QWRAPPER = 50, 40, 50, 40
COINS = ['pennies', 'nickels', 'dimes', 'quarters']

coin_amount = [0, 0, 0, 0]
wrapper_amount = [0, 0, 0, 0]
coin_weights = []


def coin_calc(coin, weight):
    amount_ = 0
    wraps_ = 0

    if coin == 'pennies':
        amount_ = round(weight / PWEIGHT)
        wraps_ = math.ceil(amount_ / PWRAPPER)
    elif coin == 'nickels':
        amount_ = round(weight / NWEIGHT)
        wraps_ = math.ceil(amount_ / NWRAPPER)
    elif coin == 'dimes':
        amount_ = round(weight / DWEIGHT)
        wraps_ = math.ceil(amount_ / DWRAPPER)
    else:
        amount_ = round(weight / QWEIGHT)
        wraps_ = math.ceil(amount_ / QWRAPPER)

    return amount_, wraps_


print("Welcome to coin calculator.")
weight_type = int(input("Would you like to enter weights in 1: pounds, or 2: grams?  "))

for i in range(4):
    inp = float(input(f"Enter weight of total {COINS[i]}:  "))
    if weight_type == 1:
        inp *= 453.592
    coin_weights.append(inp)

for i in range(4):
    coin_amount[i], wrapper_amount[i] = coin_calc(COINS[i], coin_weights[i])

for i in range(4):
    print(f"You have {coin_amount[i]} {COINS[i]}, and it will take {wrapper_amount[i]} wrappers to wrap them.")
