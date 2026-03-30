name = input("Enter customer name: ")
count=0
subtotal=0
while True:
    product = input("Enter product name (or 'done' to finish) : ")
    if product.lower()=='done':
        break
    price = float(input("Enter price:"))
    count+=1
    subtotal+=price
print("Customer: " + name.upper())
print("Items: " + str(count))
print("Subtotal: " + str(subtotal))
if subtotal<3000:
    discount_tier='No discount'
    discount=0
else:
    if subtotal>=3000 and subtotal<7000:
        discount_tier='5 %'
        discount=5
    else: 
        if subtotal>=7000:
            discount_tier='15 %'
            discount=15
total=float(subtotal-(subtotal*(discount/100)))
print("------------------------------")
print("Discount tier: "+ discount_tier)
print("Discount: "+str(float(subtotal*(discount/100))) + " KZT")
print("Total: "+str(total) + " KZT")
print("------------------------------")
print("Name uppercase: " + name.upper())
print("Name lowercase: " + name.lower())
print("Name length: " + str(len(name)))
if len(name)>5:
    print('Long name')
else:
    print('Short name')
