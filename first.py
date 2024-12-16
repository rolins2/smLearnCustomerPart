import time

print("Welcome to the DEMO MarketPlace")

admins = {"admin1": "password", "admin2": "password2"}
customers = {"customer1": "password", "customer2": "password2"}

products = [
    {'id': 1, 'name': 'Boots', 'category_id': 1, 'price': 100},
    {'id': 2, 'name': 'Coats', 'category_id': 2, 'price': 200},
    {'id': 3, 'name': 'Jackets', 'category_id': 2, 'price': 150},
    {'id': 4, 'name': 'Caps', 'category_id': 3, 'price': 50}
]

global session
session = {}

class customer:
    def __init__(self, usrName):
        print("Customer Created")
        self.cust = usrName
        self.cart = []

    def show_catalog(self, products):
        print("Following is the list of all the products we have")
        for x in products:
            print(f"{x['name']} \n Price is: {x['price']} \n Product ID: {x['id']}")
        time.sleep(10)

    def addToCart(self, products):
        shopping = True
        while shopping:
            print("This is the list of products we have")
            self.show_catalog(products)

            pID = int(input("Enter the product ID of the item you want to add: "))
            qty = int(input("Enter the quantity of the desired product: "))

            product_found = False
            for product in products:
                if product['id'] == pID:
                    self.cart.append({'product': pID, 'Qty': qty})
                    print(f"{product['name']} has been added to your cart.")
                    product_found = True
                    break
            if not product_found:
                print("Product not found. Please enter a valid product ID.")

            continue_shopping = input("Do you want to add another item? (1 -yes /2 -no): ")
            if continue_shopping != '1':
                shopping = False

    def removeItemFromCart(self):
        if not self.cart:
            print("Your cart is empty. There is nothing to remove.")
        else:
            print("We are in the else of the remove cart")
            self.check_cart()

            itmRmv = int(input("Enter the item to remove from the cart: "))
            product_found = False
            for ct in self.cart:
                if ct['product'] == itmRmv:
                    product_found = True
                    # remove takes out the item by value
                    self.cart.remove(ct)
                    print(f"Item with Product ID {itmRmv} has been removed from your cart.")
                    break

            if not product_found:
                print("Product not found. Please enter a valid product ID.")
                self.removeItemFromCart()

            fs = True
            while fs:
                c = int(input("Do you want to continue? Press 1 (Yes) 2 (No): "))

                if c == 1:
                    print("Loop continues")
                    self.removeItemFromCart()
                    break
                elif c == 2:
                    fs = False
                    print("Thank you, your items have been removed from the cart.")
                else:
                    print("Invalid Input")

    def check_cart(self):
        if not self.cart:
            print("Your cart is empty.")
            time.sleep(10)
        else:
            print("Your Cart Contains:")
            for item in self.cart:
                prod = ""
                for p in products:
                    if p['id'] == item['product']:
                        prod = p
                if prod:
                    print(f"{prod['name']} : \n Quantity: {item['Qty']} \n ID: {prod['id']}")
            time.sleep(10)

    def checkOut(self, products):
        if not self.cart:
            print("Your cart is empty.")
            time.sleep(10)
        else:
            print("Following are the items in your cart")
            print(f"You have {len(self.cart)} items in your cart")
            total = 0
            for item in self.cart:
                prod = ""
                for p in products:
                    if p['id'] == item['product']:
                        prod = p
                if prod:
                    ttlItemPrice = prod['price'] * item['Qty']
                    total += ttlItemPrice
                    print(f"{prod['name']} : \n Quantity: {item['Qty']} \n Price per unit: Rs {prod['price']} \n Total Price of Item = Rs {ttlItemPrice}")
                    print("---------")

            print(f"Total : {total}")
            inps = int(input("Press 1 to pay \n Press 2 to go back to main menu"))
           
                
            if(inps ==1 ):
                paym = False
                while(paym == False):
                    print("\n Press 1 to pay via upi ")
                    print("Press 2 to pay via credit card")
                    print("Press 3 to pay via debit card")
                    print("Press 4 to pay via cash on delivery")
                    paym = int(input("Make your payment choice "))
                    if(paym ==1 or paym ==2 or paym==4):
                        print("Thank you for your payment of "+str(total) + " your order would reach you shortly ")
                        time.sleep(10)
                        self.cart = []
                        paym = True
                    elif(paym == 4):
                        print("Please keep Rs"+str(total) +" ready at the time of delivery")
                        self.cart = []

                        paym = True

                        break
                    else:
                        print("Invalid choice ")
                        paym = False 
            elif(inps ==2 ):
                return ;
            else: 
                print("Invalid Input")
                self.checkOut(products)

inp = int(input("Press 1 for Admin Login or Press 2 for Customer login: "))

def loginAuth(arr):
    global session
    AdmName = input("Please Enter your username: ")
    AdmPass = input("Please enter your password: ")

    if AdmName in arr and arr[AdmName] == AdmPass:
        print("Woohooo")
        session['username'] = AdmName
        return True
    else:
        print("Invalid username and password")
        print("Enter details again")
        loginAuth(arr)

if inp == 1:
    print("Hello Admin")
    val = loginAuth(admins)
    if val:
        print(f"Hello {session['username']}")

elif inp == 2:
    print("Hello Customer")
    val = loginAuth(customers)
    if val:
        print(f"Hello {session['username']}")
        cust = customer(session['username'])

        choice = 0
        # create a function greet and call it later
        print("Welcome to Demo Mart")

        while choice != 7:
            print("Choose an option")
            print("Press 1 to view the catalog")
            print("Press 2 to view cart")
            print("Press 3 to add item to cart")
            print("Press 4 to remove an item from cart")
            print("Press 5 to checkout")
            print("Press 6 to logout")
            print("Press 7 to end")

            choice = int(input("Make your decision: "))

            if choice == 1:
                cust.show_catalog(products)
            elif choice == 2:
                cust.check_cart()
            elif choice == 3:
                cust.addToCart(products)
            elif choice == 4:
                print("Let's remove an item now")
                cust.removeItemFromCart()
            elif choice == 5:
                print("Welcome to the checkout page:")
                cust.checkOut(products)
            elif choice == 7:
                print("Thank you for visiting Demo Mart!")
            else:
                print("Invalid input")
