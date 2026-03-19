print("Welcome to our restaurent.Here's the menu:")
total=0
menu={
    "Pizza":40,
    "Pasta":50,
    "Burger":60,
    "Salad":70,
    "Coffee":80
}

for i in menu:
    print(i,'=',menu[i])

order=input("Enter your  first order=")

if order in menu:
    print("Order of",order, "has been added")
    total+=menu[order]

    another_order=input("Do  you want to order anything else?")
    if another_order =="yes":
        order2=input("Enter your  second order=")
        if order2 in menu:
            total+=menu[order2]
       
            print("Order of",order2,"has been added")
        else:
            print("Ordered item",order2,"is not availaible")
    print("The total amount of order to pay is",total)  
else:
    print("Ordered item",order,"is not availaible")
      


