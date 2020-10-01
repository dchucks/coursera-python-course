# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything 
# other than a valid number catch it with a try/except and put out an appropriate message and ignore the 
# number. Enter the numbers from the book for problem 5.1 (4,5,junk,7) and match the desired output as follows:
# Invalid input
# Maximum is 7
# Minimum is 4

largest = None
smallest = None

while True:
    num = input("Enter a number:")
    if num == "done" : break
    try:
        inum = int(num)
        if(largest is None):
            largest = inum
        elif(inum > largest):            
            largest = inum 
        
        if(smallest is None):
            smallest = inum
        elif(inum < smallest):
        	smallest = inum
    except:
        print("Invalid input")    
    
print("Maximum is", largest)
print("Minimum is", smallest)
