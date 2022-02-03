"""
Name: 
Username: 
ID number: 

Description
-

A program which simulates the number of medals won for a specific sport in the
Olympic Games, and then it calculates the total cost of the money prizes for the athletes.

`$60 000 for a gold medal`
`$55 000 for a silver medal`
`$50 000 for a bronze medal`
"""
import random

sport_name = input("Enter the sport: ")

number_of_gold = random.randint(0, 2)
number_of_silver = random.randint(0, 4)
number_of_bronze = random.randint(2, 6)

print("The total number of gold(s) is", number_of_gold)
print("The total number of silver(s) is", number_of_silver)
print("The total number of bronze(s) is", number_of_bronze)

prize_money_exclusive_of_tax = (number_of_gold * 60000) + (number_of_silver * 55000) + (number_of_bronze * 50000)

prize_money_including_tax = round(prize_money_exclusive_of_tax * 0.85)
print("The total net prize money is $" + str(prize_money_including_tax))