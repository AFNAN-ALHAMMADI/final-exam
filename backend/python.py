fruits = [
    [1, 'apple', 10],
    [2, 'orange', 5],
    [3, 'banana', 12],
    [4, 'date', 20],
    [5, 'strawberry', 16]
]

print(" fruits : ")
for num, name, price in fruits:
    print(str(num) + " - " + name +" : " + str(price) + "SAR" )

choice = int(input(" Enter the fruit number : "))

if choice >= 1 and choice <= 5:
    index = choice - 1
    name = fruits[index][1]
    price = fruits[index][2]
else:
    print(" The number is incorrect ")
    exit()

tax = price * 0.15
total = price + tax

print(" Name : " + name)
print(" Price :  " + str(price) + "SAR")
print(" Tax (15%) : " + str(tax) + "SAR")
print(" Total : " + str(total) + "SAR")