
#1. Write a function to compute 5/0 and use try/except to catch the exceptions.
def comp():
    try:
        p = int(input ('Enter non-zero integer: '))         
        div = 5 / p
    except ZeroDivisionError:
        while p == 0: 
            p = int(input ('Try again, enter non-zero integer: '))                         
    finally:
        div = 5 / p
        print ('Finally ! the division of number 5 by integer',p, 'is', div)
      
comp()

#2. Implement a Python program to generate all sentences where subject 
#is in ["Americans",#"Indians"] and verb is in ["Play", "watch"] and the 
#object is in ["Baseball","cricket"].
#Hint:Subject,Verb and Object should be declared in the program as shown below.
#subjects=["Americans ","Indians"]
#verbs=["play","watch"]
#objects=["Baseball","Cricket"]
#Output should come as below:
#Americans play Baseball.
#Americans play Cricket.
#Americans watch Baseball.
#Americans watch Cricket.
#Indians play Baseball.
#Indians play Cricket.
#Indians watch Baseball.
#Indians watch Cricket.

subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]

sen = [(a+' '+b+' '+c) for a in subjects for b in verbs for c in objects]

for sen in sen: 
    print (sen)
    
