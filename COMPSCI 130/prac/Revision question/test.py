def main():
    gst = 1.15
    user_input = input("Enter a list of prices: ")
    price_list = user_input.split(" ")
    a_list = []

    for index in range(len(price_list)):
        price = price_list[index]
        
        if "," in price:
            position = price.find(",")
            result = round((float(price[:position])) * gst, 2)
            a_list.append(result)
        else:
            result = round((float(price[:position])) * gst, 2)
            a_list.append(result)

    return print(a_list)
            







main()
##1.25, 2.55, 2.44, 10093.23, 1000.34
