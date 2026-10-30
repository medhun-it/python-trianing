units = float(input())
amount = 0.0

if units >= 0 and units <= 50:
    amount = units * 1
elif units <= 150:
    amount = 50 + (units - 50) * 2
elif units <= 250:
    amount = 50 + 200 + (units - 150) * 3
else:
    amount = 50 + 200 + 300 + (units - 250) * 4

if amount > 150:
    amount = amount + amount * 0.2

print(int(amount))
