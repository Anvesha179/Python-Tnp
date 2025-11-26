#Name: Anvesha     Enrollment no.:0157AL231046    Batch:5 Batch-Time:    10:30 am to 12:10 pm

######  Basic If–Else Problems:   ######

#1. Write a program to check whether a number is positive, negative, or zero.
num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")



#2.Write a program to check whether a number is even or odd.
    num = int(input("Enter an integer: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")



#3.Write a program to check if a given year is a leap year or not.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


#4. Write a program to find the greatest of two numbers.
    num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > num2:
    print(f"The greater number is {num1}.")
elif num2 > num1:
    print(f"The greater number is {num2}.")
else:
    print("Both numbers are equal.")
    

#5.Write a program to check whether a person is eligible to vote (age >= 18).
age = int(input("Enter your age: "))
if age>=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


#6.Write a program to check whether a given character is a vowel or consonant.
char=input("Enter the character :")
vowel=['a','e','i','o','u']
if char in vowel:
 print(f"{char} is vowel")
else:
 print(f"{char} is consonant")


#7.Write a program to check if a number is divisible by 5.
 num = int(input("Enter a number: "))
if num % 5 == 0:
    print(f"{num} is divisible by 5.")
else:
    print(f"{num} is not divisible by 5.")


#8.Write a program to determine whether a given number is a single-digit, two-digit,
# or more than two-digit number.
num=input("Enter the number :")
cnt=len(num)
if cnt==1:
 print("Single digit")
elif cnt==2:
 print("Double Digit")
else:
 print("More than 2 digit")


#9.Write a program to check whether a student has passed or failed (passing marks = 40).
marks=int(input("Enter your marks :"))
if marks>=40:
 print("Student passed the exam")
else:
 print("Student failed the exam")



#10.Write a program to find whether the entered number is a multiple of both 3 and 7.
 num = int(input("Enter a number: "))
if num % 3 == 0 and num % 7 == 0:
    print(f"{num} is a multiple of both 3 and 7.")
else:
    print(f"{num} is not a multiple of both 3 and 7.")


   ######  Ladder If & Nested If:  ######
    
#1.Write a program to find the greatest among three numbers.
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
if num1>num2 and num1>num3:
 print(f"{num1} is greatest among the given numbers")
elif num2>num1 and num2>num3:
 print(f"{num2} is greatest among the given numbers")
else:
 print(f"{num3} is greatest among the given numbers")



#2.Write a program to classify a person based on age: Child (<13), Teenager (13-19), Adult (20-59), Senior (60+).
 age = int(input("Enter your age: "))
if age < 0:
    print("Invalid age entered.")
elif age < 13:
    print("You are classified as a Child.")
elif age <= 19:
    print("You are classified as a Teenager.")
elif age <= 59:
    print("You are classified as an Adult.")
else:
    print("You are classified as a Senior.")



#3.Write a program to assign grades based on marks:

#90-100: A,
#75-89: B,
#50-74: C,
#35-49: D,
#<35: Fail.
    
marks=int(input("Enter marks :"))
if marks>=90 and marks<=100:
 print("A grade")
elif marks>=75 and marks<=89:
 print("B grade")
elif marks>=50 and marks<=74:
 print("C grade")
elif marks>=35 and marks<=49:
 print("D grade")
else:
 print("Fail")



#4.Write a program to check the type of triangle (equilateral, isosceles, or scalene) based on sides.
a = float(input("Side 1: "))
b = float(input("Side 2: "))
c = float(input("Side 3: "))

if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Not a triangle")

    

#5.Write a program to check if a character is uppercase, lowercase, digit, or special symbol.
char = input("Enter a single character: ")
if len(char) != 1:
    print("Please enter exactly one character.")
elif char.isupper():
    print("Uppercase letter")
elif char.islower():
    print("Lowercase letter")
elif char.isdigit():
    print("Digit")
else:
    print("Special symbol")


#6.Write a program to calculate electricity bill based on units:
#Up to 100 units: ₹5 per unit,
#101–200 units: ₹7 per unit,
#Above 200 units: ₹10 per unit.
units = int(input("Enter units consumed: "))
bill = 0

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
else:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10

print(f"Total bill: ₹{bill}")



#7.Write a program to determine the largest of four numbers using nested if.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))
if a > b:
    if a > c:
        if a > d:
            largest = a
        else:
            largest = d
    else:
        if c > d:
            largest = c
        else:
            largest = d
else:
    if b > c:
        if b > d:
            largest = b
        else:
            largest = d
    else:
        if c > d:
            largest = c
        else:
            largest = d

print(f"The largest number is {largest}")




#8.Write a program to check if a given year is a century year and also a leap year.
year = int(input("Enter a year: "))
if year % 100 == 0:
    if year % 400 == 0:
        print(f"{year} is a century year and a leap year.")
    else:
        print(f"{year} is a century year but not a leap year.")
else:
    print(f"{year} is not a century year.")




#9.Write a program to classify BMI value: Underweight (<18.5), Normal (18.5-24.9), Overweight (25-29.9),
#Obese (30+).
bmi = float(input("Enter your BMI: "))
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")



#10.Write a program to display the smallest number among three using nested if.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a < b:
    if a < c:
        smallest = a
    else:
        smallest = c
else:
    if b < c:
        smallest = b
    else:
        smallest = c

print(f"The smallest number is {smallest}")



######   For Loop Problems:   ######


#1.Write a program using a for loop to print all Armstrong numbers between 100 and 999. (Armstrong number:
#sum of cubes of digits equals the number itself. Example: 153 => 13+53+33 = 153).
for num in range(100, 1000):
    digits = [int(d) for d in str(num)]
    if sum(d**3 for d in digits) == num:
        print(num)

        

#2.Write a program to generate and display the first n prime numbers using a for loop.
n = int(input("Enter how many prime numbers to display: "))
count = 0
num = 2
while count < n:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')
        count += 1
    num += 1



#3.Write a program to display all numbers from 1 to 500 that are divisible by 3, but the sum of their digits
#should not exceed 10.
    
for num in range(1, 501):
    if num % 3 == 0:
        digit_sum = sum(int(d) for d in str(num))
        if digit_sum <= 10:
            print(num, end=' ')




#4.Write a program using a for loop to print a pyramid of stars (*) of height n. Example for n=4:

   #*
  #***
 #*****
#*******
n = int(input("Enter the height of the pyramid: "))
for i in range(1, n+1):
   for j in range(n-i):
       print(" ", end="")
   for k in range(2*i-1):
       print("*", end="")
   print()



#5.Write a program to accept a string and check whether it is a pangram (contains all 26 alphabets at least once)
#using a for loop.
text = input("Enter a string: ").lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
found = True

for letter in alphabet:
    if letter not in text:
        found = False
        break

if found:
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")



#6.Write a program using a for loop to print all twin primes between 1 and 100. (Twin primes: pairs of prime
#numbers with a difference of 2, e.g., (3,5), (11,13)).
# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Print twin primes between 1 and 100
print("Twin primes between 1 and 100:")
for i in range(2, 99):
    if is_prime(i) and is_prime(i + 2):
        print(f"({i}, {i + 2})")




#7.Write a program that accepts a number from the user and prints whether it is a Harshad number (number
#divisible by the sum of its digits) using a for loop.
num = int(input("Enter a number: "))
digit_sum = 0
for digit in str(num):
    digit_sum += int(digit)
if num % digit_sum == 0:
    print(f"{num} is a Harshad number.")
else:
    print(f"{num} is not a Harshad number.")



#8.Write a program to generate Pascal’s Triangle up to n rows using a for loop.
n = int(input("Enter number of rows: "))
for row in range(n):
    val = 1
    for col in range(row + 1):
        print(val, end=' ')
        val = val * (row - col) // (col + 1)
    print()


#9.Write a program using a for loop to display the sum of the series:
#12 + 22 + 32 + ... + n2
n = int(input("Enter the value of n: "))
total = 0

for i in range(1, n + 1):
    total += i ** 2

print(f"Sum of the series: {total}")



#10.Write a program that accepts a number from the user and prints whether it is a Strong number (sum of
#factorials of digits = number itself) using a for loop. Example: 145 => 1! + 4! + 5! = 145.
num = int(input("Enter a number: "))
sum_fact = 0

for digit in str(num):
    fact = 1
    for i in range(1, int(digit) + 1):
        fact *= i
    sum_fact += fact

if sum_fact == num:
    print(f"{num} is a Strong number.")
else:
    print(f"{num} is not a Strong number.")




    ######  While Loop Problems:  ######

#11.Write a program using a while loop to find the reverse of a number and check if the reversed number is
#prime. Example: Input = 73 → Reverse = 37 → Prime.
num = int(input("Enter a number: "))
rev = 0
temp = num
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
is_prime = rev > 1 and all(rev % i != 0 for i in range(2, int(rev**0.5) + 1))

# Output
print(f"Reversed number: {rev}")
print("Prime" if is_prime else "Not prime")



#12.Write a program that continues to accept numbers from the user until the sum of digits of all numbers
#entered becomes greater than 100.
total_sum = 0
while total_sum <= 100:
    num = int(input("Enter a number: "))
    total_sum += num
    print("Total sum so far:", total_sum)
print("Total sum exceeded 100")




#13.Write a program using a while loop to check whether a number is a Duck number (a number containing zero
#but not starting with zero, e.g., 202, 1203).
num = input("Enter a number: ")

if num[0] == '0':
    print("Not a Duck number (starts with zero)")
else:
    i = 0
    found_zero = False
    while i < len(num):
        if num[i] == '0':
            found_zero = True
            break
        i += 1
    print("Duck number" if found_zero else "Not a Duck number")



#14.Write a program using a while loop to accept a number and check if it is a Happy number. (A number is
#happy if repeatedly replacing it with the sum of squares of its digits eventually reaches 1). Example: 19 is a
#happy number.
num = int(input("Enter a number: "))
seen = set()

while num != 1 and num not in seen:
    seen.add(num)
    num = sum(int(d)**2 for d in str(num))

if num == 1:
    print("Happy number")
else:
    print("Not a happy number")



#15.Write a program using a while loop to find the largest prime factor of a given number.
num = int(input("Enter a number: "))
i = 2
largest = 0

while i <= num:
    if num % i == 0:
        largest = i
        num //= i
    else:
        i += 1

print(f"Largest prime factor is {largest}")



#16.Write a program to repeatedly accept a string from the user until the string entered is a palindrome.
while True:
    s = input("Enter a string: ")
    if s == s[::-1]:
        print("Palindrome detected. Program ends.")
        break
    else:
        print("Not a palindrome. Try again.")




#17.Write a program using a while loop to compute the sum of digits of a number until the result becomes a
#single-digit number (Digital root). Example: 9875 => 9+8+7+5=29 => 2+9=11 => 1+1=2.
num = int(input("Enter a number: "))

while num >= 10:
    sum_digits = 0
    while num > 0:
        sum_digits += num % 10
        num //= 10
    num = sum_digits

print(f"Digital root is {num}")



#18.Write a program using a while loop to generate the Collatz sequence for a given number. (Rule: If n is even
#=> n/2, if odd => 3n+1. Continue until n=1).
n = int(input("Enter a number: "))

while n != 1:
    print(n, end=' ')
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1

print(1)



#19.Write a program using a while loop to accept a number and check whether it is a Kaprekar number.
#(Kaprekar number: if square of the number can be split into two parts whose sum equals the number.
#Example: 452=2025 => 20+25=45).
num = int(input("Enter a number: "))
sq = num ** 2
str_sq = str(sq)
length = len(str_sq)
i = 1
is_kaprekar = False

while i < length:
    left = int(str_sq[:i]) if str_sq[:i] else 0
    right = int(str_sq[i:]) if str_sq[i:] else 0
    if left + right == num and right != 0:
        is_kaprekar = True
        break
    i += 1

print(f"{num} is a Kaprekar number." if is_kaprekar or num == 1 else f"{num} is not a Kaprekar number.")




#20.Write a program to simulate an ATM machine using a while loop where a user can:
#• Check balance
#• Deposit money
#• Withdraw money (only if balance is sufficient)
#• Exit
#Continue until the user chooses to exit.
balance = 0
balance = 0  # Initial balance

while True:
    print("\n===== ATM Menu =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(f"Your current balance is: ₹{balance}")
    
    elif choice == 2:
        amount = float(input("Enter amount to deposit: ₹"))
        balance += amount
        print(f"₹{amount} deposited successfully. New balance: ₹{balance}")
    
    elif choice == 3:
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= balance:
            balance -= amount
            print(f"₹{amount} withdrawn successfully. Remaining balance: ₹{balance}")
        else:
            print("Insufficient balance! Transaction failed.")
    
    elif choice == 4:
        print("Thank you for using the ATM. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")




        ####### THANK YOU ######




    
















 
    

   








