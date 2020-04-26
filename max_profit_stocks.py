#You are given an array. Each element represents the price of a stock
#on that particular day. Calculate and return the maximum profit you
#can make from buying and selling that stock only once.

#For example: [9, 11, 8, 5, 7, 10]

#Here, the optimal trade is to buy when the price is 5, and sell when #it is 10, so the return value should be 5 (profit = 10 - 5 = 5).


def buy_and_sell(prices): #O(n) time O(1) memory
  if len(prices) < 2:
    return 0
  begin = prices[0]
  max_profit = 0
  for el in prices:
    if el < begin:
      begin = el
    elif el - begin > max_profit:
      max_profit = el - begin
  return max_profit


print(buy_and_sell([9, 11, 8, 5, 7, 10]))
# 5
