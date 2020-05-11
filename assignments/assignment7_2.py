# 7.2 Write a program that prompts for a file name, then opens that file and reads  
# through the file, looking for lines of the form: 
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines  
# and compute the average of those values and produce an output as shown below. 
# Do not use the sum() function or  a variable named sum in your solution. 
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt 
# when you are testing below enter mbox-short.txt as the file name.

totval = 0
count = 0
fileName = input("Enter file name: ")

try:
	file = open(fileName)
	for line in file:
		if not line.startswith("X-DSPAM-Confidence:"): 
			continue
		count = count + 1
		posofint = line.find('0')
		totval = totval + float(line[posofint:])
except:
    print("Please enter mbox-short.txt as the file name.")
    
if(count > 0):
    print("Average spam confidence:", totval/count)
else:
    print("Found no lines starting with X-DSPAM-Confidence")
