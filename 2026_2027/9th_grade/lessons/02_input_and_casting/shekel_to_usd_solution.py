# Fixed exchange rate: 1 dollar = 3.7 shekels
RATE = 3.7

# input() returns a string, so we convert each value to int
print("Shekels:")
shekels = int(input())
print("Agorot:")
agorot = int(input())

# 100 agorot = 1 shekel, so agorot / 100 gives the shekel part (a float)
total_shekels = shekels + agorot / 100

# Convert to dollars and keep 2 digits after the decimal point
dollars = round(total_shekels / RATE, 2)

print("Dollars:", dollars)
