# Find the Union of two numbers and Print the length of the set
"""
First line get input the number of person read english paper
second line get input who read the english newspaper 
third line get input the number of person read french paper 
fouth line get input who read the french newspaper
 
""" 
n=int(input())
english = set(map(int, input().split()))
b=int(input())
french = set(map(int, input().split()))
roll_number = english.union(french)
print(len(roll_number))
