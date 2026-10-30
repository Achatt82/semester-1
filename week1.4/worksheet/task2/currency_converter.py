
"""
    Portfolio Task - Week 4

    By submitting this code you are declaring that all work in this file,
    other than any provided template code, was written and developed by
    you independently.

    Name: Alex Chatterton
"""

# There was no read me? So I had to guess what you wanted me to write.

def currency_converter(amount, from_currency, to_currency):

    conversion_rate = {
        'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
        'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
        'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45},
        'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
    }

    # Input checking

    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    if (amount < 0):
        print("Cannot have negative values for currency.")
        return None
    
    if (from_currency not in conversion_rate):
        print(f"{from_currency} is either an invalid or unsupported currency.")
        return None

    if (to_currency not in conversion_rate[from_currency]):
        print(f"{to_currency} is either an invalid or unsupported currency.")
        return None

    # Edge cases

    if (from_currency == to_currency):
        return amount

    # Logic

    value = float(amount) * conversion_rate[from_currency][to_currency]

    # Format to value to 2dp 
    return f"{value:.2f}"

# Submit only this file currency_converter.py with the completed function.

# Remove any additional code you may have added during development and testing.
