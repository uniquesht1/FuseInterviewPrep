
def order_pizza(size, *toppings,**details):
    """
    Creates a pizza order with specified size, toppings, and additional details.

    Args:
        size (int): The size of the pizza in inches.
        *toppings (str): Variable number of toppings to be added to the pizza.
        **details (dict): Additional details about the order (e.g., delivery address, special instructions).

    Returns:
        None: Prints the order summary to console.

    Example:
        >>> order_pizza(12, "pepperoni", "mushrooms", delivery=True, address="123 Main St")
        Making a 12-inch pizza with the following toppings:
        - pepperoni
        - mushrooms
        {'delivery': True, 'address': '123 Main St'}
    """
    """Summarizes the pizza order."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
        print (details)
        
order_pizza(12, "pepperoni", "mushrooms", "extra cheese", crust="thin", sauce="marinara")