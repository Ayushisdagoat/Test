def main():
    cost_per_item = 19.99
    quantity = 5 

    # Part 1: Calculate subtotal_cost, tax, and total_cost
    subtotal_cost = cost_per_item * quantity
    tax = subtotal_cost * 0.13
    total_cost = subtotal_cost + tax

    # Part 2: Print the values
    print(f'cost_per_item = ${cost_per_item:0.2f}')
    print(f'quantity = {quantity}')
    print(f'subtotal_cost = ${subtotal_cost:0.2f}')
    print(f'tax = ${tax:0.2f}')
    print(f'total_cost = ${total_cost:0.2f}')

    # Part 3: Fixing the error
    initial_investment = 1000
    interest_rate = 0.035
    investment = initial_investment
    
    # Calculate the investment over 5 years
    for _ in range(5):
        investment += investment * interest_rate
    
    # The error in the original code is due to concatenating a string with a float.
    # We need to convert the float to a string for proper concatenation.
    print('After 5 years, your investment will be worth ' + str(investment) + ' dollars.')

if __name__ == "__main__":
    main()