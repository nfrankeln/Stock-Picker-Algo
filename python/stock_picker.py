# for loop method
def picker_double_loop(prices):
    max_profits = 0
    buy_sell_days = []

    for first_day , first_price in enumerate(prices):
        for second_day , second_price  in enumerate (prices):
            if second_day < first_day:
                continue
            if second_price - first_price > max_profits:
                max_profits = second_price - first_price
                buy_sell_days = [first_day,second_day]
    return buy_sell_days

# single loop method
def picker(prices):
    max_profits = 0
    buy_sell_days = []
    lowest_day = 0
    
    for current_day , current_price in enumerate(prices):
        if current_price < prices [lowest_day]:
            lowest_day = current_day
        if current_price - prices [lowest_day] > max_profits:
            max_profits = current_price - prices [lowest_day]
            buy_sell_days = [lowest_day,current_day]
    return buy_sell_days


print(picker([3,2,3,4,1,8]))