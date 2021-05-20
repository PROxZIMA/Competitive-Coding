def solve(meal, tip, tax):
    return round(meal + meal * tip / 100 + meal * tax / 100)

meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())

print(solve(meal_cost, tip_percent, tax_percent))