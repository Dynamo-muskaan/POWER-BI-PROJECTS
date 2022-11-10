# TASK

# given an integer "n" perform the following conditional actions

# if n is odd,print weird
# if n is even and in the inclusive range of 2 to 5,print not weird
# if n is even and in the inclusive range of 6 to 20, print weird
#if n is even and greater than 20,print not weird


'''n = int(input("enter the number: "))
if n % 2 != 0:
	print("weird")
elif n % 2 == 0:
	if 0<n<6:
		print("not weird")
	elif 4<n<22:
	    print("weird")
	elif n>20:
	    print("not weird")
	else:
	    print("error")        	

n = int(input("enter the number: "))
if n % 2 != 0:
	print("weird")
elif n % 2 == 0:
	if 0<n<6:
		print("not weird")
	elif 4<n<22:
	    print("weird")
	else:
	    print("not weird")'''









# TASK 2

'''Given an list of integers nums and add an integer target return
indicates of the two numbers such that they add up to get the target..

INPUT 1:    nums=[2,7,11,15]  , target=9
OUTPUT 1:   [0,1]   (Because nums[0]+nums[1]==9, we return [0,1])


INPUT 2:   nums=[3,2,4] , target=6
OUTPUT:    [1,2]'''

''' MEANING OF THE QUESTION - 
humari koi b list hai uske kisi b 2 ya 3 nos ko add krke 9 aana 
chahiye to output me show krna chahiye ki list me konse index 
pr wo numbers hai jinko add krne pr 9 aayega '''


'''num = []
l = int(input("enter the length of the list: "))
k = 0
z = 0
target = 9
while k < l:
	k+=1
	m = int(input("enter anything: "))
	num.append(m)
print(num)
for i in range(0,len(num)):
	if num[i]+num[i+1]==target:
		z+=1
		print(num[i],num[i+1])
		print(i,i+1)'''










# TASK 3

'''current no 0  previous no 0
current no 1  previous no 0
current no 2  previous no 1
current no 3  previous no 2
current no 4  previous no 3
current no 5  previous no 4
current no 6  previous no 5
current no 7  previous no 6
current no 8  previous no 7
current no 9  previous no 8'''


'''x = 0
	for i in range(10):
		if i == 0:
			print("current no",i,"previous no",i)
		elif i >= 0:
			print("current no",i,"previous no",i-1)
	'''	









# run a program to capitalize the first and last character of each word in a string

'''input = hello world
output = HellO WorlD'''

'''x = "muskaan verma"
print(x[0].upper()+x[1:6]+x[6].upper(),x[8].upper()+x[9:12]+x[-1].upper())

ouput - MuskaaN VermA'''








'''x = "prince" 
 remove "i" from this string
 output - "prnce"''' 

'''x = "prince"
for i in x:
	if i == "i":
		continue
	print(i,end="")	'''








# TASK 

'''lets learn about list comprehensions you are given three integers x,y,and z 
representing the dimensions of cuboid along with an integer "n" 
print a list of all possible coordinates given by (i,j,k) on a 3D grid 
where the sum of i+j+k is not equal to n 
here, 0<=i<=x, i can only take values from 0 till x
0<=j<=y,       j can only take values from 0 till y
0<=k<=z        k can only take values from 0 till z

input:
x = 1
y = 1
z = 2
n = 3
all permutations of [i,j,k] are:
[[0,0,0],[0,0,1],[0,0,2],[0,1,0],[0,1,1],[0,1,2],[1,0,0],[1,0,1],[1,0,2]]

but here we have to print the list of permutations of [i,j,k] 
which is not equal to n so we will take only these arrays:

[[0,0,0],[0,0,1],[0,0,2],[0,1,0],[0,1,1],[1,0,0],[1,0,1] etc ]'''

'''a = []
x = int(input("enter the no1: "))
y = int(input("enter the no2: "))
z = int(input("enter the no3: "))
n = int(input("enter an integer: "))
for i in range(0,x+1):
	for j in range(0,y+1):
		for k in range(0,z+1):
			if i+j+k!=n:
				b = [i,j,k]
				a.append(b)
print(a)'''








# TASK

'''given the participants score sheets for your university sports day,
you are required to find the runner up score you are given n scores
store them in a list and find the score of the runner up

output - [2,3,6,6,5]
runner up score - 5'''


'''a = []
x = int(input("enter the number of student: "))
for i in range(x):
	n = int(input("enter the scores: "))
	a.append(n)
b = sorted(a,reverse=True)
print(b)
print("runnerupscore: ",b[1])'''







# TASK

# print the even places words of the word "pynative"

'''x = "pynative"
for i in range(len(x)):
	if i%2==0:
		print(x[i],end=" ")'''

'''x = "pynative"
	for i in range(0,len(x),2):
	    print(x[i])'''	






# TASK 

'''write a func. to return True if the first and last number of the 
given list is same if the nos are different then return false

given:
number_x = [10,20,30,40,10] true
number_y = [75,65,55,32,45] false'''


'''x = []
y = int(input("enter the size of the list: "))
z = 0
while z < y:
	z+=1
	a = eval(input("enter anything: "))
	x.append(a)
print(x)
if x[0]==x[-1]:
	print("true")
else:
	print("false")	'''










# task 

# print a dict by user input then {2:56,1:2,5:12,4:24,6:18,3:323}
# keys and values are sorted in alphabetical order by keys 
# it should be arranged in thus way (1:2),(2:56),(3:323),(4:24) etc..


'''x = {}
ans = []
y = int(input("enter the size of dict: "))
z = 0
while z < y:
	z+=1
	a = eval(input("enter the keys: "))
	b = eval(input("enter the values: "))
	x.update({a:b})
	ans.append([a,b])
print("dict as follows",x)
print(ans)
s = sorted(x.keys())
print("the keys of the dict are: ",s)
result = sorted(ans)
print(result)'''








# task

'''Create a new list from a two list using the following condition

Given a two list of numbers, write a program to create a new list 
such that the new list should contain odd numbers from the first 
list and even numbers from the second list.

Given:

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
Expected Output:

result list: [25, 35, 40, 60, 90]'''

'''list1 = []
list2 = []
list3 = []
x = int(input("enter the length of list1: "))
y = int(input("enter the length of list2: "))
z1 = 0
z2 = 0
while z1<x:
	z1+=1
	a = eval(input("enter anything: "))
	list1.append(a)
print(list1)
while z2<y:
	z2+=1
	b = eval(input("enter items: "))
	list2.append(b)
print(list2)	
for i in range(len(list1)):
	if list1[i]%2!=0:
		print("odd nos are",list1[i],end=" ")
		list3.append(list1[i])
		print()
for j in range(len(list2)):
    if list2[j]%2==0:
    	print("even nos are",list2[j],end=" ")
    	list3.append(list2[j])
    	print()
print(list3)'''


#create a program to cheach a no. is prime or not

'''
x = int(input("enter a number: "))
y = 2
if y > x:
	print("number is not a prime no.")
elif x == y:
    print("number is a prime number")
else:
    while y < x:
        if x % y == 0:
            print("not a prime number")
            break
        y += 1    	
    else:
    	print("it is prime no.")'''







#TASK

'''Calculate income tax for the given income by adhering to the 
below rules
Taxable Income	Rate (in %)
First $10,000	0
Next $10,000	10
The remaining	20
Expected Output:

For example, suppose the taxable income is 45000 the income tax payable is

10000*0% + 10000*10%  + 25000*20% = $6000.'''

        			


# input  = ["apple","orange","lichi","lemon","plum"]
# newlist = []
# output
# newlist = ["lichi","lemon"]

'''a = []
x = ["apple","orange","lichi","lemon","plum"]
y=x[2:4]
print(y)
a.append(y)
print(a)'''


'''Combining a one and a two-dimensional NumPy Array

Input:
One dimensional array:
[0 1 2 3 4]
Two dimensional array:
[[0 1 2 3 4]
 [5 6 7 8 9]]

Output:
0:0
1:1
2:2
3:3
4:4
0:5
1:6
2:7
3:8
4:9'''


import numpy as np


'''
Combining a one and a two-dimensional NumPy Array 
Input:
One dimensional array:
[0 1 2 3 4]
Two dimensional array:
[[0 1 2 3 4]
 [5 6 7 8 9]]
Output:
0:0 1:1 2:2 3:3 4:4 0:5 1:6 2:7 3:8 4:9'''


'''x = np.arange(5)
print(x)
y = np.arange(10).reshape(2,5)
print(y)
for a, b in np.nditer([x, y]):
    print("%d:%d" % (a, b),)'''
    
'''Get all items between 5 and 10 from a.
Input: a = np.array([2, 6, 1, 9, 10, 3, 27])
Output:(array([6, 9, 10]),)

x = np.array([1,2,3,4,5,6,7,8,9,10])
print(x)
y = x[(x>2)|(x<10)]
print(y)
'''


## Convert a 1D array to a 2D array with 2 rows

'''
x = np.arange(12)
print(x)
print(x.reshape(2,6))'''


'''
Reverse the columns of a 2D array arr.
Input:
arr = np.arange(9).reshape(3,3)
Output : array([[2, 1, 0],
              [5, 4, 3],
              [8, 7, 6]])'''



'''x = np.arange(9).reshape(3,3)
print(x[0][2::-1],x[1][2::-1],x[2][2::-1])'''




'''Compare both arrays element to element and 
find the maximum value among them
Input:
a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
Output: array([ 6.,  7.,  9.,  8.,  9.,  7.,  5.])'''

'''
a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
c = np.maximum(a,b)
print(c)'''




'''Limit the number of items printed in python numpy array a to a maximum of 6 elements.
Input: a = np.arange(15)
Desired Output: array([ 0,  1,  2, ..., 12, 13, 14])'''


'''import numpy as np

a=np.arange(15)
print("Original aarray",a)'''



'''x=int(input("Enter even no of elements you want: "))
z=x//2
arr=np.array([],dtype=int)

for i in range(z):
        arr=np.append(arr,a[i])

for j in range(len(a)-z,len(a)):
        arr=np.append(arr,a[j])

print("New array",arr)'''


# Get n-largest values from a particular column in Pandas DataFrame


'''df=pd.DataFrame({"Name":["Avery","Jas","John","hunter","Jonas","Amir","Mickey","Kelly","Terry","marcus"],
		"Age":[25,25,27,22,29,29,21,25,22,22],
		"Height":[6.2,6.6,6.5,6.5,6.10,6.9,6.8,7.0,6.2,6.4],
		"Weight":[180,235,205,185,231,240,235,238,190,220]})
print(df)'''
#a] Get 5 rows which are having largest weights

#b] Get 3 names which are elders in the data frame

#c] Get 3 names having highest height among everyone and reset its index the output

import pandas as pd

'''x = pd.DataFrame({"Date":pd.date_range("20220810",periods=10),
	"Withdrawl":np.random.randint(8000,15000,10),
	"Credit":np.random.randint(10000,20000,10),
	"Name":"muskaan"},index=["A","B","C","D","E","F","G","H","I","J"],
	columns=["Date","Name","Credit","Withdrawl"])
print(x)
x["Savings"]=x["Credit"]-x["Withdrawl"]
print(x)'''





'''The Fibonacci Sequence is a series of numbers. 
The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.

For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34.

Expected output:

Fibonacci sequence:
0  1  1  2  3  5  8  13  21  34'''

'''a = int(input("enter the range: "))
m = 0
n = 1
p = 0
while (p<=a):
	print(p)
	m=n
	n=p
	p=m+n'''


'''
Find the sum of the series upto n terms
Write a program to calculate the sum of series up to n term. 
For example, 
if n =5 the series will become 
2 + 22 + 222 + 2222 + 22222 = 24690'''
#2[1+11+111+1111+11111]

'''x = int(input("enter the n: "))
summ = 0
a = 1
while a<=x:
	#a+=1
	a=(a*10)+1
	print(a,end=" ")
	a+=1
	summ+=a
print(summ)'''


'''x = int(input("enter the n: "))
y = 0
summ=0
for i in range(x):
	y=(y*10+1)
	print(y,end=" ")
	print()
	summ+=y
print(summ)

x = int(input("enter the n: "))
y = 0
summ=0
for i in range(x):
	y=(y*10+2)
	print(y,end=" ")
	print()
	summ+=y
print(summ)'''


'''x = int(input("enter the n: "))
y = 0
z = 0
summ = 0
while y<=x:
	#y+=1
	y = y*10+2
	y+=1
print(y,end=" ")
	#y+=1
print()
summ+=y 
print(summ)'''


'''Write a program to 
find the sum of the following series
(accept the values of x and n from user)
      1 + x/1! + x*2/2! +...................x*n/n!'''

'''x = 43521
a = str(x)
for i in a[::-1]:
	print(i,end=" ")'''



x = 1500
while x<=2700:
	if x%7==0:
		if x%5==0:
			print(x)
	x+=1