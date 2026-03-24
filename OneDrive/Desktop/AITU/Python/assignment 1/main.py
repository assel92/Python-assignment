name = input("Enter customer name:")
product = input("Enter product name:")
price = float(input("Enter price per unit (KZT):"))
quantity = int (input("Enter quantity:"))
subtotal = price * quantity
if subtotal>5000:
    discount = subtotal * 0.1
else :
    discount = 0
total = subtotal - discount
print("==============================")
print("        SHOP RECEIPT")
print("==============================")
print("Customer: " + name)
print("Product: " + product)
print("Price: " + str(price) + " KZT")
print("Quantity: " + str(quantity))
print("------------------------------")
print("Subtotal: " + str(subtotal) + " KZT")
print("Discount: " + str(discount) + " KZT")
print("Total: " + str(total) + " KZT")
print("==============================")
print("Discount applied:", subtotal > 5000)
print("Paid more than 3000: ", total > 3000)