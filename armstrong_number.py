n = int(input("Enter a number: "))
temp = n
total = 0

while temp > 0:
    digit = temp % 10
    total = total + digit ** 3
    temp = temp // 10

if total == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
