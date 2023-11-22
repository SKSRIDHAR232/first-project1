a = 10
b = int(input(" How many 7up's do you want :"))
c = a - b
if b < 10:
    for i in range(b):
        print("Take your drink!!")
else:
    for i in range(a):
        print("Take your drink!!")
    print("Sorry, Out of Stocks")
print("There are {} drinks balance".format(c))
print("Have a Happy Drinks")
