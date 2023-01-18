'''Guessing Number
Rahul is playing a Guessing number game with computer. The
objective of the game is to guess the number that computer thinks.
A guess is "correct" when the guess exactly matches the computer's
number. After each guess by Rahul, the computer will give a score
comprising black 8 white coins:
Black coin
• guessed digit is present in the Computer's Number
and in same position.
White con
• guessed digit is present in the Computeris Number but
in another position.
Your task is to find out the number of black coins and the number of
white coins.'''
'''Sample Output 1
1234
1423 , computer =
Given Rahul =
The digit I is same position in the two number strings so Black
peg has 1 and remaining digits are in the different positions in the
two number strings so White peg has 3
So, the output should be blacks : 1 whites : 3
Sample Input 1
1423 1234
Sample Output 1
blacks
1
whites
3
'''


# cook your dish here
black=0
white=0

a,b=list(input().split(" "))
for i in range(len(a)):
    one=a[i]
    two=b[i]
    if (one==two):
        black+=1
    elif (one in b):
        white+=1
    
print(black , white)
