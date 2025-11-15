a = input('enter price:')
b = input('enter discount:')

price = float(a)
price_discount = float(b)
reduction = price-price_discount

print(f'price = {price}\n price with discount = {price%price_discount}\n and reduction = {reduction}')