def bill(total, paid):
    return total - paid

total = float(input("Total: "))
paid = float(input("Paid: "))

print("Remaining:", bill(total, paid))