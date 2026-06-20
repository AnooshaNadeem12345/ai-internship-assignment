#Menu Funtion

def menu(item):
    if item == "karahi":
        return "Karahi is cooking"
    elif item == "biryani":
        return "Biryani is ready"
    elif item == "bbq":
        return "BBQ is grilled"
    elif item == "chai":
        return "Chai is served"
    else:
        return "Item not available"
 
input_item = input("Enter the item you want to order: ")
result = menu(input_item)
print(result)

# # CUSTOMER SERVICE SYSTEM

customers = {}
customers["Customer 1"] = input("Customer 1 order: ")
customers["Customer 2"] = input("Customer 2 order: ")
customers["Customer 3"] = input("Customer 3 order: ")
customers["Customer 4"] = input("Customer 4 order: ")
customers["Customer 5"] = input("Customer 5 order: ")

for customer, order in customers.items():
    result = menu(order)
    print(f"{customer} ordered {order} -> {result}")

# Karahi Spice Level System
def karahi(spice_level):
    if spice_level == "high":
        return "very spicy karahi"
    elif spice_level == "medium":
        return "normal karahi"
    elif spice_level == "low":
        return "mild karahi"
    else:
        return "Invalid spice level"

result = karahi(input("Enter spice level for karahi (high, medium, low): "))
print(result)

# BBQ Platter System

def bbq(pieces):
    if pieces >= 10:
        return "Full BBQ Platter"
    elif pieces >= 5:
        return "Half BBQ Platter"
    else:
        return "small BBQ Platter"

result = bbq(int(input("Enter number of BBQ pieces: ")))
print(result)   

#Chai Sugar function

def chai(sugar):
    if sugar == 0:
        return "No sugar Chai"
    elif sugar == 1:
        return "Normal sugar Chai"
    elif sugar >= 2:
        return "Sweet Chai Chai"
    else:return "Invalid sugar level"

result = chai(int(input("Enter sugar level for Chai (0, 1, 2): ")))
print(result)

#Chai System(FULL SYSTEM COMBINED WITH ALL FUNCTIONS)
def karahi(spice_level):
    if spice_level == "high":
        return "Spicy Karahi"
    elif spice_level == "medium":
        return "Normal Karahi"
    elif spice_level == "low":
        return "Mild Karahi"
    else:
        return "Invalid spice level"

def bbq(pieces):
    if pieces >= 10:
        return "Full BBQ Platter"
    elif pieces >= 5:
        return "Half BBQ Platter"
    else:
        return "Small BBQ Platter"

def chai(sugar_level):
    if sugar_level == "high":
        return "Sweet Chai"
    elif sugar_level == "medium":
        return "Normal Chai"
    elif sugar_level == "low":
        return "Less Sweet Chai"
    else:
        return "Invalid sugar level"

def menu(item):
    if item == "karahi":
        spice = input("Enter spice level (high, medium, low): ")
        return karahi(spice)
    elif item == "biryani":
        return "Biryani is ready"
    elif item == "bbq":
        pieces = int(input("Enter number of BBQ pieces: "))
        return bbq(pieces)
    elif item == "chai":
        sugar = input("Enter sugar level (high, medium, low): ")
        return chai(sugar)
    else:
        return "Item not available"

# DESI RESTAURANT MANAGEMENT SYSTEM

for i in range(1, 6):
    order = input(f"Customer {i} → Enter item (karahi/biryani/bbq/chai): ")
    result = menu(order)
    print(f"Customer {i} → {order} → {result}")
    print()