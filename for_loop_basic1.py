for i in range(1, 156):
    print(i)


for i in range(0,1000,5):
  print(i)


for i in range (0,101):
        if i % 10 == 0:
            print ('Coding')
        elif i % 5 == 0:
            print("Coding Dojo")
        else:
            print(i)

minimum = 0
maximum = 500000
Oddtotal = 0

for number in range(minimum, maximum+1):
    if(number % 2 != 0):
        print("{0}".format(number))
        Oddtotal = Oddtotal + number

print("The Sum of Odd Numbers from {0} to {1} = {2}".format(minimum, maximum, Oddtotal))

sum = 0
for i in range(1,500001,2):
    sum += i
print(sum)

number = 2018
while number > 0:
        print (number)
        number = number - 4

for i in range(2018,0,-4):
    print(i)

low = 2
high = 9
mult = 3

for i in range(low,high + 1):
    if i % mult == 0:
        print(i)