"""
Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages.

In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

Sal’s Shippers has several different options for a customer to ship their package:

    Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
    Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
    Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

Here are the prices:

Ground Shipping
Weight of Package 	Price per Pound 	Flat Charge
2 lb or less 	$1.50 	$20.00
Over 2 lb but less than or equal to 6 lb 	$3.00 	$20.00
Over 6 lb but less than or equal to 10 lb 	$4.00 	$20.00
Over 10 lb 	$4.75 	$20.00

Ground Shipping Premium

Flat charge: $125.00

Drone Shipping
Weight of Package 	Price per Pound 	Flat Charge
2 lb or less 	$4.50 	$0.00
Over 2 lb but less than or equal to 6 lb 	$9.00 	$0.00
Over 6 lb but less than or equal to 10 lb 	$12.00 	$0.00
Over 10 lb 	$14.25 	$0.00

Write a shipping.py Python program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.

Note that the walkthrough video for this project is slightly out of date — the walkthrough was done using a version of this project that uses functions. Feel free to come back to the video after having been introduced to functions!
"""

weight = input("What is the weight of your package(in lbs)")
shipping_option = input("How do you want your package shipped? \n 1. Enter 1 for ground shipping \n 2. Enter 2 for premium ground shipping(Flat charge of $125.00) \n 3. Enter 3 for Drone shipping")

#Weight of package
weight = 41.5

# GROUND SHIPPING

#Ground shipping rate
ground_rate = 20
#Cost of shipping
shipping_cost = 0

if weight <= 2:
  ground_shipping_cost = ground_rate + (weight * 1.50)
elif weight <= 6:
  ground_shipping_cost = ground_rate + (weight * 3.00)
elif weight <= 10:
  ground_shipping_cost = ground_rate + (weight * 4.00)
else:
  ground_shipping_cost = ground_rate + (weight * 4.75)

print(f"Ground shipping $ {ground_shipping_cost}")
print()

# PREMIUM GROUND SHIPPING

#Weight of package

#Premium ground shipping rate
ground_rate_premium = 125

premium_shipping_cost = ground_rate_premium

print(f"Premium ground shipping $ {premium_shipping_cost}")
print()

# DRONE SHIPPING

#Drone shipping rate
drone_rate = 0
#Cost of shipping
shipping_cost = 0

if weight <= 2:
  drone_shipping_cost = drone_rate + (weight * 4.50)
elif weight <= 6:
  drone_shipping_cost = drone_rate + (weight * 9.00)
elif weight <= 10:
  drone_shipping_cost = drone_rate + (weight * 12.00)
else:
  drone_shipping_cost = drone_rate + (weight * 14.25)

print(f"Drone shipping $ {drone_shipping_cost}")
print()
