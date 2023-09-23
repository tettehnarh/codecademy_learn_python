# You work at Len’s Slice, a new pizza joint in the neighborhood. You are going to use your knowledge of Python lists to organize some of your sales data.

# Your code below:
# To keep track of the kinds of pizzas you sell, create a list called toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# To keep track of how much each kind of pizza slice costs, create a list called prices
prices = [2, 6, 1, 3, 2, 7, 2]

# Your boss wants you to do some research on $2 slices.

# Count the number of occurrences of 2 in the prices list, and store the result in a variable called num_two_dollar_slices. Print it out.
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# Find the length of the toppings list and store it in a variable called num_pizzas.
num_pizzas = len(toppings)

# Print the string We sell [num_pizzas] different kinds of pizza!, where [num_pizzas] represents the value of our variable num_pizzas. 
print(f'We sell {num_pizzas} different kinds of pizza!')

# Use the existing data about the pizza toppings and prices to create a new two-dimensional list called pizza_and_prices.
# Each sublist in pizza_and_prices should have one pizza topping and an associated price.
pizza_and_prices = [[2, "pepperoni"],[6, "pineapple"],[1, "cheese"],[3, "sausage"],[2, "olives"],[7, "anchovies"],[2, "mushrooms"]]

# Print pizza_and_prices
print(pizza_and_prices)

# Sort pizza_and_prices so that the pizzas are in the order of increasing price (ascending). 
pizza_and_prices = sorted(pizza_and_prices)
print(pizza_and_prices)

# Store the first element of pizza_and_prices in a variable called cheapest_pizza.
cheapest_pizza = pizza_and_prices[0]

# A man walks into the pizza store and shouts “I will have your MOST EXPENSIVE pizza!”
# Get the last item of the pizza_and_prices list and store it in a variable called priciest_pizza.
priciest_pizza = pizza_and_prices[-1]

# It looks like the most expensive pizza from the previous step was our very last "anchovies" slice. Remove it from our pizza_and_prices list since the man bought the last slice.
pizza_and_prices.pop()

# Since there is no longer an "anchovies" pizza, you want to add a new topping called "peppers" to keep your customers excited about new toppings. Here is what your new topping looks like:
# [2.5, "peppers"]
pizza_and_prices.append([2.5, "peppers"])
print(pizza_and_prices)

# Three mice walk into the store. They don’t have much money (they’re mice), but they do each want different pizzas.
# Slice the pizza_and_prices list and store the 3 lowest cost pizzas in a list called three_cheapest.
three_cheapest = pizza_and_prices[:3]

# Print the three_cheapest list.
print(three_cheapest)

