n = int(input())

new1 = n % 4
new2 = n % 100
new3 = n % 400


if new1 == 0:
    if new2 != 0 or new3 == 0:
        print("1")
    else:
        print("0")
else:
    print("0")