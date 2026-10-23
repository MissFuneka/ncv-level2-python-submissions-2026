#creating(defining) a function  

def place_order(item): #semicolon - tells compiler its not done
    print(f"Item placed is:{item}")
    print("Order placed")
    
def getOrder():
    print("Preparing Order")
    return "Collect Your Order" #simplify return but nor printing

def calculate_total(item):
    base_price = 25.5
#     Vat = 0.15
    totalprice = (base_price + len(item)) * 1.15
    return totalprice

    
   
myfood = input("what would you like: ")
place_order(myfood)
#msg= getOrder() #saving return in a variable
#print(msg)
print("")
print(getOrder()) #only allowed to call a function in a print if it has a return

order_total = calculate_total(myfood)

print(f"Your order costs : R{order_total:.2f}")

print("")

