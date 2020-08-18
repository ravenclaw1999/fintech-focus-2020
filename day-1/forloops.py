print("We start counting with the number 1.")

#prints 1-20
for i in range(1, 21):
    print("The next number is " + str(i))

for i in "sushi":
    print(i)

for i in "sushi":
    if i == "s":
        print("There is an s")

## 1. Print out every number 1-100
for i in range (1, 101):
    print(i)

## 2. Print out every number from 50-100
for i in range(50, 101):
    print(i)

## 3. Find the sum of the first 100 digits
count = 0
for i in range(1, 101):
    count+=i
    print(count)

## 4. Find the sum of the numbers from 1000 to 2000
sum = 0
for i in range(1000, 2001):
    sum+=i
    print(sum)

## 5. Print out every perfect square number less than or equal to 100
for i in range (1, 11):
    if (i * i) <= 100:
        print(i * i)

## 6. If you got one grain of rice on day 1, two grains of rice on day 2, and four grains of rice on day 3, and it kept doubling like that, print out a daily report of how much rice you'd receive on each day for 30 days.
num = 1
for i in range(1, 31):
    num *= 2
    print(num)

## 7. Print out every number that ends in a 7 from 7-1007.
for i in range(7, 1007):
    i = str(i)
    if "7" in i:
        print(i)
    # print(i.find("7"))

## 8. Print out every even number from 1-100.
for i in range(1, 101):
    if i % 2 == 0:
        print(i)

## 9. Print out every multiple of three from 1-100
for i in range(1, 101):
    if i % 3 == 0:
        print(i)

## 10. Print out multiples of two, another list of multiples of three, and then a third list of items which appear in both lists.
for i in range(1, 101):
    if i % 2 == 0:
        print(i)
    
for i in range(1, 101):
    if i % 3 == 0:
        print(i)

for i in range(1, 101):
    if i % 3 == 0 and i % 2:
        print(i)



## CHALLENGE: Print out numbers which are multiples of 3 OR multiples of 2, but not multiples of both.
for i in range(1, 101):
    if i % 3 == 0 or i % 2:
        print(i)

## SUPER CHALLENGE: Print out the first 40 numbers in the Fibonacci sequence.

num1 = 0
num2 = 1

for i in range(0, 41):
    if i == 0:
        print(num1)
    elif i == 1:
        print(num2)
    else:
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        print(num3)
