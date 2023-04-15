#this is the list of items store in a variable
data = [350, 400, 250, 200, 150, 1000, 2000, 500, 1000, 500]

# removing the duplicate
item = set(data)
print("this is the non-duplicated values:",item)

# sumation of item
Amount = sum(item)
print("this is the sum total of the amount:", Amount)

# removal of 7% vat from the amount
vat_deduction = 0.07 * Amount

Total = Amount - vat_deduction
print("Total after VAT deduction:",Total)