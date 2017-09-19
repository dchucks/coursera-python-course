# 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, 
# print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. 
# For the test, enter a score of 0.85 for desired output B.

rawscore = raw_input("Enter Score: ")
outofrange = False
grade = None

try:
	score = float(rawscore)
except:
    print "Invalid input, try again."
    exit()

if(score < 0.0):
    outofrange = True
elif (score > 1.0):
    outofrange = True
    
if(outofrange is True):    
    print "Entered number should be between 0.0 and 1.0."
    quit()
else:
    if(score >= 0.9):
        grade = "A" 
    elif(score >= 0.8):
        grade = "B"
    elif(score >= 0.7):
        grade = "C"
    elif(score >= 0.6):
        grade = "D"
    elif(score < 0.6):
        grade = "F"
    print grade
