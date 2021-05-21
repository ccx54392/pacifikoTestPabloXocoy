def is_prime(number):
    isPrime = True
    if number <=1:
        isPrime = False
    for i in range(2,number):
        if number % i == 0:
            isPrime = False
    if isPrime:
        print("The number is prime")
    else:
        print("The number is not prime")
                
          

try:
    number = int(input("Enter a number: "))
    is_prime(number)
except:
    print("Invalid entry")
    
