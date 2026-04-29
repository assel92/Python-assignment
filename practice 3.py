#task 1
store_info = ("FreshMart", "Astana, Respublika Ave 1", "+7 700 000 00 00")
print("==============================")
print(store_info[0])
print(store_info[1])
print(store_info[2])
print("==============================")

#task 2
names=[]
prices=[]
while True:
    product = input("Enter product name (or 'done' to finish): ")
    if product.lower()=='done':
        break
    names.append(product)
    price = float(input("Enter price: "))
    prices.append(price)
print("-------------------------------")
print("Your cart (" + str(len(names)) + " items) :")
print("-------------------------------")
for i in range (len(names)):
    print(names[i] + " - "+ str(prices[i])+" KZT")
print("-------------------------------")

#task 3
weekly_products = set()
while True:
    product1 = input("Enter product name (or 'done' to finish) : ")
    if product1.lower()=='done':
        break
    weekly_products.add(product1)
print("Unique products: " + str(len(weekly_products)))
print(weekly_products)

#task 4
subtotal = sum(prices)
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
discount2 = float(subtotal*(discount/100))
total=float(subtotal-discount2)
customer=input("Enter customer name: ")
receipt = {"Customer":  customer, "Items":len(names), "Subtotal": str(subtotal) + " KZT", "Discount": str(discount2) + " KZT" + "("+str(discount_tier)+")" , "Total": str(total) }
print("==============================")
print("RECEIPT - "+ store_info[0])
print("==============================")
print("Customer: " + receipt["Customer"])
print("Items: " + str(receipt["Items"]))
print("-------------------------------")
for i in range (len(names)):
    print(names[i] + " - "+ str(prices[i])+" KZT")
print("-------------------------------")
print("Subtotal: " + str(receipt["Subtotal"]))
print("Discount: " + str(receipt["Discount"]))
print("Total: " +str(receipt["Total"]))
print("==============================")