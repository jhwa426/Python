"""
Lab 3: Program 3 (Question 7)

"""

def main():
    request = get_number("Enter number (5 - 20): ")
    handling_cost = 5
    cost_per_item = 4.25
    change_cost = get_cost(request, cost_per_item, handling_cost)
    final_result = display_details(request, cost_per_item, handling_cost, change_cost)
    
def get_number(prompt):
    return int(input(prompt))

def get_cost(number, cost_per_unit, handling_cost):
    total_cost = number * cost_per_unit + handling_cost
    return round(total_cost)

def display_details(items, cost_each, handling_cost, final_price):
    print()
    print("Items: ", items, " Cost per item: $", cost_each, sep="")
    print("Handling cost: $", handling_cost, sep="")
    print("Total: $", final_price, sep="")

main()








