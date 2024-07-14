menu = {
      'coffee' : 50,
      'Tea' : 45,
      'pizza' : 300,
      'pasta' : 240,
      'Maggie' : 140,
      'chowmin' : 260,
      'pastry' : 170,
      'Burger' : 250,
} 

print("WELCOME TO PYTHON RESTURANT")
print("Here is our Menu...")
print(" coffee : 50 \n tea : 45 \n pizza : 300 \n pasta : 240 \n maggie : 140 \n chowmin : 260 \n pastry : 170 \n Burger : 250") 

order_total = 0

item_1 = input("Enter the name of your item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"{item_1} IS NOT AVAILABLE IN OUR MENU")    

another_item = input("Do you want to add another item? (yes/no) : ") 
if (another_item == "yes"):
    item_2 = input("Enter your order : ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to your order ")
    else:
        print(f"Your item {item_2} is not available in our menu")  

print(f"The total amount of item is {order_total}") 
       
