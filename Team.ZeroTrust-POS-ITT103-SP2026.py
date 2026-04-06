##variables
storeName = "Team Zero Trust's Best Buy Retail Store"
taxRate = 0.10
discountRate = 0.05
discountThreshold = 5000

##the store's inventory list
products = {
    "rice":         {"price":90, "stock": 20},
    "flour":        {"price":95, "stock": 15},
    "sugar":        {"price":160, "stock": 25},
    "mackerel":     {"price":110, "stock": 30},
    "bread":        {"price":590, "stock": 18},
    "eggs":         {"price":450, "stock": 60},
    "sardine":      {"price":260, "stock": 10},
    "tang":         {"price":90, "stock": 12},
    "bigga soda":   {"price":120, "stock": 8},
    "toilet paper": {"price":110, "stock": 40},
    "hennesy":      {"price":10000, "stock": 15}
}

##the function for displaying the menu with its price and amount in inventory including spacing for neatness. 
def showProducts():
    print(" ")
    print("PRODUCT LIST")
    print("Item         Price($)    Stock")
    for p in products:
        print(f"{p:<12} ${products[p]['price']:<10} {products[p]['stock']:<10}")
    print()

## function showing product list for user to add items to cart, it will be in lowercase.
def addToCart(cart):
    showProducts()
    item = input("Enter item: ").lower()
    ## if the item entered not found in the product list, print the "Item not found" and start loop again. 
    if item not in products:
        print("Item not found")
        return
    ##Upon enetering the quantity, it will be read and stored as an integer and if not an integer, "Invalid number" will print.
    qty = int(input("Enter quantity: "))
    if qty <=0:
        print("Invalid number")
        return
    ##If the stock is less than the quantity entered "Not enough stock" will be printed. 
    if qty > products[item]["stock"]:
        print("Not enough stock")
        return
    ##if the item is already in the cart, add what is entered to it.
    if item in cart:
        cart[item] += qty
    else:
        cart[item] = qty

    products[item]["stock"] -= qty
    print("Added to cart")
    print(" ")
    
##Removing items from cart, using the len() function = (if the items in cart is 0), "Cart empty" will be printed.
def removeFromCart(cart):
    if len(cart) == 0:
        print("Cart empty")
        return
    ##User will enter item to remove which will be in lowercase. 
    printCart(cart)
    item = input("Enter item to remove: ").lower()
    
    ##If its not in the the cart, "Not in cart" will be printed.
    if item not in cart:
        print("Not in cart")
        return
        
    ##Upon enetering the quantity, it will be read and stored as an integer again and if its not an integer, "Invalid number" will print.
    qty = int(input("Enter quantity: "))
    if qty <=0:
        print("Invalid number")
        return
    print("Removed")
    print(" ")

##def printCart(cart) function shows items inside the cart, if the cart is empty "Cart empty" will be printed.
def printCart(cart):
    print("")
    print("CART")
    if len(cart) == 0:
        print("Cart empty")
        return
##The subtotal starts at zero so that it can add up the total cost of all the items. 
##Each item in the cart and its price from the products list.
##The entered quantity multiplies by price to gives the total cost
##adds that to the overall total, and finally shows the item name, quantity, and total cost on one line.
    subtotal = 0
    for item in cart:
        price = products[item]["price"]
        qty = cart[item]
        total = price * qty
        subtotal += total
        print(item, "x", qty, "=", "$",total)

    print("Subtotal:", "$",subtotal)
    print(" ")

def checkout(cart):
    subtotal = 0
    for item in cart:
        subtotal += products[item]["price"] * cart[item]
        
##discount is applied if the subtotal is greater than 5000
    if subtotal > discountThreshold:
        discount = subtotal * discountRate
    else:
        discount = 0
##tax & subtotal calculation
    tax = (subtotal - discount) * taxRate
    total = subtotal - discount + tax

##Printing the stored discount, tax and total.
    printCart(cart)
    print("Discount: $", discount)
    print("Tax: $", tax)
    print("Total: $", total)

##The amount paid will be entered and stored as an integer. The total will be subtract from the amount paid.
##If the paid amount is lesser than then total, then "Not enough money" will be printed and a new transaction will be asked.
    paid = int(input("Enter amount paid: $"))
    if paid >= total:
        print("Change: $", paid - total)
    else:
        print("Not enough money")
        print(" ")

##Main menu function created with a combination of while loop and if else loops
def main():
    print("Welcome to", storeName)
    while True:
        cart = {}
        while True:
            print("(1) View Products")
            print("(2) Add To Cart")
            print("(3) Remove From Cart")
            print("(4) View Cart")
            print("(5) Checkout")
            print("(6) Cancel")
            
##Choice variable create based on user's input
            choice = input("Enter your choice by selecting a number between (1-6): ")
            
##Action execute from menu depending on the integer's value of choice. 
            if choice == "1":
                showProducts()
            elif choice == "2":
                addToCart(cart)
            elif choice == "3":
                removeFromCart(cart)
            elif choice == "4":
                printCart(cart)
            elif choice == "5":
                if len(cart) > 0:
                    checkout(cart)
                else:
                    print("Cart empty")
                break
            elif choice == "6":
                print("Cancelled")
                break
            else:
                print("Invalid option")
##RunAgain function determine if the user wants to start another transcation or not. 
##"Y" for Yes and 'N' for No
        if (runAgain := input("New transaction? ('Y' for Yes and 'N' for No): ").lower()) == "n":
            print("")
            print("Goodbye & Thank You Shopping With Us!")
            break
        print("")
        
##A new transaction starts again
main()
