def new_price(old_price, discount = 0):
    newPrice = old_price - old_price*discount
    return newPrice
print(new_price(100))
print(new_price(100, 0.5))
