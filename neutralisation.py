'''
Neutralisation
Given two sti ot the satno length and c.omprifi0d ot and
int a now stiinq that shows tho cosuit ot tho interaction of the
two sting assuminq tho following rules:
1) if + and + on 
2) action b/w two negative characters rosulte, in a negative
chat aetet. against a "-" returns another
•3)Intetaction b/w a positive and a negative character results in a
"O" (neutt at). against a "-" returns a "0".)
Assume that characters in similar positions in the strings interact
with each other. For example, the 4th character in the first string
intet acts with the 4th character in the second string.
'''
'''Explanation
Given String A is + ---
+++- and Bis
The interaction between the two strings is
From the following rules, the result should be
0-0-0 -++0-
So the output is 0-0-0-++0-
Sample Input 1
'''

# cook your dish here
one, two=list(input().split(" "))
result=''
for i in range(len(one)):
    a=one[i]
    b=two[i]
    if (a==b):
        result+=a
    else:
        result+='0'
print(result)
