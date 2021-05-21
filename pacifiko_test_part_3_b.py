def display_sum(number):
    sum = (number/2)*(1+number)
    print("Consecutive sum is: ",sum)

try:
    number = int(input("Enter a number: "))
    display_sum(number)
except:
    print("Invalid entry")
    
