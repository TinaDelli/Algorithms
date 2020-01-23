#!/usr/bin/python

import argparse

prices = [100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]

def find_max_profit(prices):
  current_min = prices[0]
  current_max = prices[0]
  #find out the largest number
  for num in prices:
    if current_max < num:
      current_max = num
  for el in prices:
    if prices.index(current_max) == 0:
        pass #todo
        for i in range(prices.index(current_max) + 1, len(prices)):
          if current_max < i:
            current_max = i
          elif prices.index(i) < prices.index(current_max):
            if i < current_min:
              current_min = i
      #skip that current max and look for a new maximum number
      #set that value to current max, look for current min 
    elif prices.index(el) < prices.index(current_max):
        if el < current_min:
          current_min = el
   

  print(f"{current_max} min:{current_min}")    
  return current_max - current_min
  

      # if prices.index(current_max) < prices.index(num):
      # if prices.index(current_max) == 0:
      #   current_min =  current_max + 10
      # elif num < current_min:
      #   current_min = num

print (find_max_profit(prices))


  

  


# Write a function find_max_profit that receives as input a list of stock prices.
#  Your function should return the maximum profit that can be made from a single buy and sell. 
# You must buy first before selling; no shorting is allowed here.

# For example, find_max_profit([1050, 270, 1540, 3800, 2]) should return 3530, 
# which is the maximum profit that can be made from a single buy and then sell of these stock prices.


#HINT
# For this problem, we essentially want to find the maximum difference between the smallest and largest prices in the list of prices,
#  but we also have to make sure that the max profit is computed by subtracting some price by another price that comes before it; 
# it can't come after it in the list of prices.

# So what if we kept track of the current_min_price_so_far and the max_profit_so_far?
# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))