# Program ID: a1_BonnevilleC_HusicE
# Description: Creating a program to determine and print to a customer's
# month energy bill.
# Revision History:
# Created by Christine Bonneville on January, 25 2025

"""Constants"""
from a1_BonnevilleC_HusicE import loyalty_discount

SUBSIDY = 0.12
TAX_RATE = 0.13

UNIT_FEE1 = 0.20
UNIT_FEE2 = 0.30
UNIT_FEE3 = 0.50
UNIT_FEE4 = 0.75

"""Variables"""
customer_name=input("Enter Customer name: ")
customer_id=float(input("Enter Customer ID: "))
units=float(input("Enter units consumed: "))
customer_years=float(input("\nEnter how many years you have been a"
                           " customer: "))
customer_subsidy=input("\nAre you eligible for the subsidy? y/n: ")

"""If Else for Unit Fee"""
if units <= 299:
    units_consumed = units * 0.2
elif 300 <= units < 500:
    units_consumed = units * 0.3
elif 500 <= units < 900:
    units_consumed = units * 0.5
else:
    units_consumed = units * 0.75

"""Calculations"""
subsidy_amount1 = units_consumed * SUBSIDY
subsidy_amount2 =  0
subsidy_amount3 = 30
subtotal1 = units_consumed - loyalty_discount - subsidy_amount1
subtotal2 = units_consumed - loyalty_discount - subsidy_amount2
subtotal3= units_consumed - loyalty_discount - subsidy_amount3
tax_amount1 = subtotal1 * TAX_RATE
tax_amount2 = subtotal2 * TAX_RATE
tax_amount3 = subtotal3 * TAX_RATE
total1 = subtotal1 + tax_amount1
total2 = subtotal2 + tax_amount2
total3 = subtotal3 + tax_amount3

print(f"\nCustomer Name:    {customer_name}")
print(f"Customer ID:      {customer_id:.0f}")
print(f"\nUnits Consumed:   {units:.0f}")

"""If Else for Unit Amount line with Unit Fee"""
if units <= 299:
    print(f"Unit fee ${UNIT_FEE1:.2f}/unit: ${units_consumed:.2f}")
elif 300 <= units < 500:
    print(f"Unit fee ${UNIT_FEE2:.2f}/unit: ${units_consumed:.2f}")
elif 500 <= units < 900:
    print(f"Unit fee ${UNIT_FEE3:.2f}/unit: ${units_consumed:.2f}")
else:
    print(f"Unit fee ${UNIT_FEE4:.2f}/unit: ${units_consumed:.2f}")

"""Match Statement for Loyalty Discount
Customer years determine loyalty discount
0-2y=$0.00 | 3-4y=$5.00 | 5-6y=$10.00 | Over 6y= $15.00"""
match customer_years:
    case 0 | 1 | 2:
        loyalty_discount = 0.00
    case 3 | 4:
        loyalty_discount = 5.00
    case 5 | 6:
        loyalty_discount = 10.00
    case _:
        loyalty_discount  = 15.00
print(f"Loyalty Discount: -${loyalty_discount:.2f}")

if customer_subsidy == "n":
    print(f"Subsidy Amount:   -${subsidy_amount2:.2f}")
elif customer_subsidy == "y":
    print(f"Subsidy Amount:   -${subsidy_amount1:.2f}")
else:
    print(f"Subsidy Amount:   -${subsidy_amount3:.2f}")

if subtotal1 < 30:
    print(f"\nSubtotal:        ${subtotal2}")
else:
    print(f"\nSubtotal:        ${subtotal1:.2f}")

if subtotal1 < 30:
    print(f"Tax Amount:        ${tax_amount2:.2f}")
else:
    print(f"Tax Amount:        ${tax_amount1:.2f}")

if subtotal1 < 30:
    print(f"Total Amount Owed: ${total2:.2f}")
else:
    print(f"Total Amount Owed: ${total1:.2f}")


print("\nSubsidy in this code is 12% yet in the assignment, "
      "\nit calculates out to be set at 12.85% so the amounts don't "
      "\nmatch in comparison.")



