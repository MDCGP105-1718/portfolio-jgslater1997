annual_salary = float(input("How do you earn in a year."))
portion_saved = float(input("Enter the persetage of you annaual salary you save"))
total_cost = float(input("How much will your dream home cost."))

portion_deposit = 0.2

#the total_cost is the price of the home
# total_cost : 1000000
# annual_salary : 120000
monthy_salary = (annual_salary/12)
# current_saving*r/12 (0.04)

r = 0.04

current_saving = 0

number_of_months = 0
#the while works out the amount of months it will cost to save up for the new house
while current_saving < total_cost * portion_deposit:
    current_saving += current_saving * r/12
    current_saving += monthy_salary * portion_saved
    number_of_months += 1

print(f"months required: {number_of_months}")

#
