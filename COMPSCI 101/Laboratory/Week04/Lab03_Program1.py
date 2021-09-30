"""
Lab 3: Program 1 (Questions 1 - 5)

"""

def main():
    request = "Enter number of tickets required: "
    tickets = get_number_from_user(request)
    full_price = get_ticket_price(tickets, 15)
    discount = get_discount(tickets, full_price)
    display_ticket_price(tickets, full_price, discount)
    
def display_ticket_price(tickets, price, discount):    
    print("*" * 20)
    print("Tickets:", tickets)
    user_price = price - discount
    print("Price: $", user_price, " (discount included: $"+str(discount)+").", sep="")
    get_amount = get_gst_amount(user_price)
    print("GST included: $", get_amount, sep="")
    print("*" * 20)


def get_gst_amount(price):
    gst = price * 0.15
    return round(gst, 2)

def get_discount(number_of_tickets, total_price):
    discount1 = round(total_price) * 0.1
    discount2 = number_of_tickets * 4 
    total_discount = max(discount1, discount2)
    return round(total_discount)

def get_ticket_price(number_of_tickets, ticket_price):
    price = number_of_tickets * ticket_price
    return round(price)

def get_number_from_user(prompt):
    number = int(input(prompt))
    return number


main()








