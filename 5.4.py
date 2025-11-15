a = input('enter price: ')
price = float(a)
vat = float(price*0.23)
price_without_vat = price-vat

print(f'cena {price} sklada sie z {round(price_without_vat,2)} + {round(vat,2)} vat ')
            