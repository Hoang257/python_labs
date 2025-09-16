price = float(input('Еnter the product price: '))
discount = float(input('Еnter the discount of the product:' ))
vat = float(input('Еnter vat of the product:' ))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

print(f'Base after discount: {base}')
print(f'Vat: {vat}')
print(f'Final summ: {total}')