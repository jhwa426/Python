"""
Lab 4:
"""

def main():
    price = get_ticket_price(5, 20, True, False)
    print("$" + str(price))
    print("$" + str(get_ticket_price(5, 20, False, True)))
    print("$" + str(get_ticket_price(5, 20, False, False)))
    print("$" + str(get_ticket_price(15, 25, False, True)))

    
def get_ticket_price(number_of_tickets, ticket_price, has_discount, is_a_member):
    price = (number_of_tickets * ticket_price)
    if (has_discount == True) and (is_a_member == True):
        return round(price * 0.80)
    elif (has_discount == True) and (is_a_member == False):
        return round(price * 0.85)
    elif (has_discount == False) and (is_a_member == True):
        return round(price * 0.90)
    elif (has_discount == False) and (is_a_member == False):
        return price


main()








