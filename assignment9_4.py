# 9.4 Write a program to read through the mbox-short.txt and figure out who has the 
# sent the greatest number of mail messages. The program looks for 'From ' lines and 
# takes the second word of those lines as the person who sent the mail. The program 
# creates a Python dictionary that maps the sender's mail address to a count of the 
# number of times they appear in the file. After the dictionary is produced, the 
# program reads through the dictionary using a maximum loop to find the 
# most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

emaildict = dict()
maxemailid = ''
maxemailcnt = 0

for line in handle:
    if(line.startswith('From:')): continue
    elif(line.startswith('From')):
        mylst = line.split()
        emaildict[mylst[1]] = emaildict.get(mylst[1], 0) + 1
        
for emailid in emaildict:
    if emaildict[emailid] > maxemailcnt:
        maxemailcnt = emaildict[emailid]
        maxemailid = emailid
        
print(maxemailid, maxemailcnt)
