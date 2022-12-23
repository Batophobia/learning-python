cost = int(input("Total cost: "))
per = int(input("Percent for tip: "))
print(f"Total payment: ${str(cost + cost * per/100)}")