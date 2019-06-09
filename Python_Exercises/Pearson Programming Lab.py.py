
# coding: utf-8

# # The PRACTICE of COMPUTING USING PYTHON - Pearson Prog. Lab

# ## Chapter 1 - Beginnings

# #### 1.3 An Interactive Session

# Write an expression whose value is the result of converting the str value associated with s to an int value. So if s were associated with "41" then the resulting int would be 41.

# In[1]:


s=41
int(s)


# #### 1.5 Variables (Examples)

# Assign 7 to a variable named seven.

# In[2]:


seven=7


# Define two variables, one named length making it refer to 3.5 and the other named width making it refer to 1.55.

# In[3]:


length=3.5
width=1.55


# Given two variables matric_age and grad_age, write a statement that makes the associated value of grad_age 4 more than that of matric_age.
# 
# 
# 

# In[4]:


matric_age = 10
grad_age=4 + matric_age
grad_age


# #### 1.7 Operators

# Write an expression that computes the sum of two variables verbal_score and math_score (assume that both have already been defined). 
# 
# 

# In[5]:


verbal_score= 50
math_score=45
y=verbal_score + math_score
y


# Assume there is a variable, h already assigned a positive integer value. Write the code necessary to assign its square to the variable g. For example, if h had the value 8 then g would get the value 64.
# 
# 

# In[6]:


h=8
g=h**2
g


# Assume that price is an integer variable whose value is the price (in US currency) in cents of an item. Assuming the item is paid for with a minimum amount of change and just single dollars, write an expression for the number of single dollars that would have to be paid.
# 
# 

# In[7]:


price= 205
price//100.0


# #### 1.7.1 Integer Operators (Examples)

# Write an expression that computes the remainder of the variable principal when divided by the variable divisor. (Assume that each is associated with an int.)

# In[8]:


principal=10
divisor=3
principal%divisor


# Assume that price is an integer variable whose value is the price (in US currency) in cents of an item. Assuming the item is paid for with a minimum amount of change and just single dollars, write an expression for the amount of change (in cents) that would have to be paid.
# 
# 

# In[9]:


price=105
price % 100


# #### 1.7.3 Mixed Operators (Examples)

# Assign the average of the values in the variables a, b, and c to a variable avg. Assume that the variables a, b, and c have already been assigned a value, but do not assume that the values are all floating-point. The average should be a floating-point value.

# In[10]:


a=3
b=2
c=1
avg=(a+b+c)/3. #floating
avg 


# ### Programming Projects

# Write a program that asks the user for the number of males and the number of females registered in a class using two separate inputs ("Enter number of males:", "Enter number of females:"). The program should display the percentage of males and females (round to the nearest whole number) in the following format:
# * Percent males: 35%
# * Percent females: 65%
# 
# Use string formatting.	

# In[11]:


males=int(input("Enter number of males:"))
females=int(input("Enter number of females:"))

total= males+females

percentmale= males/total
percentfemale= females/total

print("Percent males:", end=" ")
print(format(percentmale,'.0%'))
print("Percent females:", end=" ")
print(format(percentfemale,'.0%'))


# ## Chapter 2 - Control

# #### 2.1 Selection Statements of Decisions

# #### 2.1.1 Booleans for Decisions (Examples)

# Write an expression that evaluates to True if and only if the value of x is equal to zero.

# In[12]:


x=1
x==0


# Write an expression that evaluates to True if the value of index is greater than the value of last_index.

# In[14]:


index=a
last_index=c
index > last_index


# #### 2.1.2 If Statements (Examples)

# Write a conditional that assigns True to fever if temperature is greater than 98.6.

# In[15]:


temperature= 10

if temperature > 98.6: 
    fever = True


# Write a conditional that decreases the value associated with shelf_life by 4 if the value associated with outside_temperature is greater than 90.
# 
# 

# In[16]:


outside_temperature = 97
shelf_life= 100

if outside_temperature > 90: 
    shelf_life = shelf_life-4
    
shelf_life


# Given the variables name1 and name2, write a fragment of code that assigns the larger of their associated values to first.
# 
# 
# (NOTE: "larger" here means alphabetically larger, not "longer". Thus, "mouse" is larger than "elephant" because "mouse" comes later in the dictionary than "elephant"!) 

# In[17]:


name1= "mouse"
name2= "elephant"
first=max(name1, name2)
first


# Given x and y, each associated with an int, write a fragment of code that associates the larger of these with another variable named max.
# 
# 

# In[18]:


x=3
y=4

if x > y: 
    max = x
else: 
    max = y
    
max


# Given the variables x, y, and z, each associated with an int, write a fragment of code that assigns the smallest of these to min.

# In[19]:


x=1
y=2
z=3

min = x
if y < min : 
	min = y
if z < min : 
	min = z
    
min


# Write an if/else statement that compares age with 65, adds 1 to senior_citizens if age is greater than or equal to 65, and adds 1 to non_seniors otherwise.

# In[20]:


age=75
senior_citizens=0
non_seniors=0

if age >= 65 : 
    senior_citizens += 1
else : 
    non_seniors += 1


# In[21]:


senior_citizens


# In[22]:


non_seniors


# NOTE: in mathematics, the square root of a negative number is not real; in Python therefore, passing such a value to the square root function returns a value known as NaN (not-a-number).
# 
# Write the code that reads a value, the area of some square, into a variable named areaOfSquare and prints out the length of the side of that square.
# 
# HOWEVER: if any value read in is not valid input, just print the message "INVALID".

# In[23]:


import math
areaOfSquare = float(input())

if areaOfSquare>=0:
	print(math.sqrt(areaOfSquare))
else:
	print("INVALID")


# NOTE: in mathematics, division by zero is undefined. So, in Python, division by zero is always an error.
# 
# Write the necessary code to read values into callsReceived and operatorsOnCall and print out the number of calls received per operator (integer division with truncation will do).
# HOWEVER: if any value read in is not valid input, just print the message "INVALID".

# In[25]:


callsReceived = float(input("Enter number of callsReceived:"))
operatorsOnCall = float(input("Enter number of operatorsOnCall:"))
if operatorsOnCall == 0:
	print("INVALID")
else:
	print(int(callsReceived/operatorsOnCall))


# Given a int variable named yesCount and another int variable named noCount and an int variable named response write the necessary code to read a value into into response and then carry out the following:
# 
# * if the value typed in is a 1 or a 2 then increment yesCount and print out "YES WAS RECORDED"
# * if the value typed in is a 3 or an 4 then increment noCount and print out "NO WAS RECORDED"
# * If the input is invalid just print the message "INVALID" and do nothing else.

# In[26]:


response = int(input())

if response==1 or response==2: 
	yesCount+=1
	print("YES WAS RECORDED")

elif response==3 or response==4:
	noCount+= 1
	print("NO WAS RECORDED")

else:
	print("INVALID")


# In the Happy Valley School System, children are classified by age as follows:
# 
# * less than 2, ineligible
# * 2, toddler
# * 3-5, early childhood
# * 6-7, young reader
# * 8-10, elementary
# * 11 and 12, middle
# * 13, impossible
# * 14-16, high school
# * 17-18, scholar
# * greater than 18, ineligible
# 
# Given a variable age, write the necessary code to print out, on a line by itself, the appropriate label from the above list based on age.

# In[27]:


age=15

if age<2:
	print("ineligible")
elif age==2:
	print("toddler")
elif age<=5:
	print("early childhood")
elif age<=7:
	print("young reader")
elif age<=10:
	print("elementary")
elif age<=12:
	print("middle")
elif age==13:
	print("impossible")
elif age<=16:
	print("high school")
elif age<=18:
	print("scholar")
else:
	print("ineligible")


# HTTP is the protocol that governs communications between web servers and web clients (i.e. browsers). Part of the protocol includes a status code returned by the server to tell the browser the status of its most recent page request. Some of the codes and their meanings are listed below:
# 
# * 200, OK (fulfilled)
# * 403, forbidden
# * 404, not found
# * 500, server error
# 
# Given an int variable status, write a statement that prints out, on a line by itself, the appropriate label from the above list based on status.

# In[28]:


status= 200

if status==200: 
	print("OK (fulfilled)")

elif status==403: 
	print("forbidden")

elif status==404:
	print("not found")
	
elif status==500:
	print("server error")


# Write a statement that adds 1 to the variable reverseDrivers if the variable speed is less than 0,adds 1 to the variable parkedDrivers if the variable speed is less than 1,adds 1 to the variable slowDrivers if the variable speed is less than 40,adds 1 to the variable safeDrivers if the variable speed is less than or equal to 65, and otherwise adds 1 to the variable speeders.

# In[29]:


speed= 50
reverseDrivers=0
parkedDrivers=0
slowDrivers=0
safeDrivers=0
speeders=0

if speed < 0:
	reverseDrivers += 1
elif speed < 1:
	parkedDrivers += 1
elif speed < 40:
	slowDrivers += 1
elif speed <= 65:
	safeDrivers += 1
else:
	speeders += 1


# Assume that an int variable age has been given a value. Assume further that the user has just been presented with the following menu:
# 
# * S: hangar steak, red potatoes, asparagus
# * T: whole trout, long rice, brussel sprouts
# * B: cheddar cheeseburger, steak fries, cole slaw
# 
# (Yes, this menu really IS a menu!)
# Write some code that reads the string (S or T or B) that the user types in into a variable choice and prints out a recommended accompanying drink as follows: if the value of age is 21 or lower, the recommendation is "vegetable juice" for steak, "cranberry juice" for trout, and "soda" for the burger. Otherwise, the recommendations are "cabernet", "chardonnay", and "IPA" for steak, trout, and burger respectively. Regardless of the value of age, your code should print "invalid menu selection" if the character read into choice was not S or T or B.
# 

# In[31]:


choice=str(input("choice"))

if 	choice=="S":
	if age<=21: 
		print ("vegetable juice") 
	else: 
		print ("cabernet") 
elif choice=="T":
	if age<=21: 
		print ("cranberry juice") 
	else: 
		print ("chardonnay") 
elif choice=="B":
	if age<=21: 
		print ("soda")
	else:
		print ("IPA") 
else: 
	print("invalid menu selection")


# #### 2.1.3 Examples

# Write an expression that evaluates to True if and only if s   refers to the str "end".

# In[32]:


s=="end"


# Write an expression that evaluates to True if the str associated with s1 is greater than the str associated with s2.
# 
# 

# In[33]:


s1="anne"
s2="baba"

str(s1)>str(s2)


# Given the variable c, whose associated value is a str, write an expression that is True if and only if c is not equal to a string consisting of a single blank.
# 
# 

# In[34]:


c != str(" ")


# Write a statement that toggles on_off_switch. That is, if on_off_switch is False, it is made equal to True; if on_off_switch is True, it is made equal to False.
# 
# 

# In[35]:


on_off_switch=1
on_off_switch= not(on_off_switch)


# #### 2.2.6 Boolean Operators Examples

# Assume that a variable variable, numberOfSides has been initialized. Write a statement that assigns the value True to the variable isQuadrilateral if numberOfSides is exactly 4 and False otherwise.
# 
# 

# In[36]:


numberOfSides=1
isQuadrilateral = numberOfSides==4
isQuadrilateral


# Assume that a variable hoursWorked has been initialized. Write a statement that assigns the value True to the variable workedOvertime if hoursWorked is greater than 40 and False otherwise.
# 
# 

# In[37]:


hoursWorked=42
workedOvertime= hoursWorked > 40
workedOvertime


# Clunker Motors Inc. is recalling all vehicles from model years 2001-2006. Given a variable modelYear write a statement that assigns True to recalled if the value of modelYear falls within the recall range and assigns False otherwise.
# 
# Do not use an if statement in this exercise!
# 
# 

# In[38]:


modelYear=2004
recalled = (modelYear >=2001 and modelYear <=2006)
recalled


# Clunker Motors Inc. is recalling all vehicles from model years 2001-2006. Given a variable modelYear write a statement that assigns True to norecall if the value of modelYear is NOT within the recall range and assigns False otherwise.
# 
# Do not use an if statement in this exercise!
# 
# 

# In[39]:


norecall = not(modelYear >=2001 and modelYear <=2006)
norecall


# Clunker Motors Inc. is recalling all vehicles in its Extravagant line from model years 1999-2002 as well all vehicles in its Guzzler line from model years 2004-2007. Given variables modelYear and modelName write a statement that assigns True to recalled if the values of modelYear and modelName match the recall details and assigns False otherwise.
# 
# 

# In[40]:


modelName="Guzzler"

if modelName == "Extravagant" and modelYear >= 1999 and modelYear <= 2002:
	recalled = True 
elif modelName == "Guzzler" and modelYear >= 2004 and modelYear <= 2007:
	recalled = True
else:
	recalled = False
    
recalled


# Clunker Motors Inc. is recalling all vehicles in its Extravagant line from model years 1999-2002. Given variables modelYear and modelName write a statement that assigns True to recalled if the values of modelYear and modelName match the recall details and assigns false otherwise.
# 
# 

# In[41]:


if (modelName == "Extravagant" and modelYear >= 1999 and modelYear <= 2002):
	recalled = True
else:
	recalled = False

recalled


# Clunker Motors Inc. is recalling all vehicles from model years 1995-1998 and 2004-2006.Given a variable modelYear write a statement that assigns True to recalled if the value of modelYear falls within the two recall ranges and assigns False otherwise.
# 
# Do not use an if statement in this exercise!
# 
# 

# In[42]:


recalled = ((modelYear >=1995 and modelYear <=1998) or (modelYear >= 2004 and modelYear <= 2006))

recalled


# Clunker Motors Inc. is recalling all vehicles from model years 1995-1998 and 2004-2006. Given a variable modelYear write a statement that assigns true to norecall if the value of modelYear does NOT fall within the two recall ranges and assigns false otherwise.
# 
# Do not use an if statement in this exercise!
# 
# 

# In[43]:


norecall = not((modelYear >=1995 and modelYear <=1998) or (modelYear >= 2004 and modelYear <= 2006))

norecall


# Clunker Motors Inc. is recalling all vehicles from model years 1995-1998 and 2004-2006. Given a variable modelYear write a statement that prints the message "RECALL" to standard output if the value of modelYear falls within those two ranges.

# In[44]:


if ((modelYear >= 1995 and modelYear <= 1998) or (modelYear >=2004 and modelYear<=2006)):
	print("RECALL")


# Clunker Motors Inc. is recalling all vehicles in its Extravagant line from model years 1999-2002. Given a variable modelYear and a String modelName write a statement that prints the message "RECALL" to standard output if the values of modelYear and modelName match the recall details.

# In[45]:


if ((modelYear >= 1999 and modelYear <= 2002) and (modelName == "Extravagant")):
	print("RECALL")


# Clunker Motors Inc. is recalling all vehicles from model years 2001-2006. Given a variable modelYear write a statement that prints the message "RECALL" to standard output if the value of modelYear falls within that range.

# In[46]:


if (modelYear >= 2001 and modelYear <= 2006):
	print("RECALL")


# Clunker Motors Inc. is recalling all vehicles from model years 2001-2006. Given a variable modelYear write a statement that prints the message "NO RECALL" to standard output if the value of modelYear DOES NOT fall within that range.
# 
# 

# In[48]:


if (modelYear > 2006 or modelYear < 2001):
	print("NO RECALL")


# #### 2.2.7 Another word on Assignments (Examples)

# Variables i and j each have associated values. Swap them, so that i becomes associated with j's original value, and j becomes associated with is original value. You can use two more variables itemp and jtemp.
# 
# 

# In[49]:


i=5
j=4

i,j=j,i

i,j


# Given two already defined variables, i and j, write a statement that swaps their associated values.
# 
# 

# In[50]:


i, j=j, i

i,j


# #### 2.2.10 Repetition: the While  Strategy

# Use the variables k and total to write a while loop that computes the sum of the squares of the first 50 counting numbers, and associates that value with total. Thus your code should associate 1*1 + 2*2 + 3*3 +... + 49*49 + 50*50 with total. Use no variables other than k and total.
# 
# 
# 
# 

# In[51]:


k=0
total=0
while k<50:
	k+=1
	total+=k*k
    
total


# Given that n refers to a positive int use a while loop to compute the sum of the cubes of the first n counting numbers, and associate this value with total. Use no variables other than n, k, and total.

# In[52]:


n=3

total=0
k=1
while k<=n:
	total+=k**3
	k+=1

total


# In this exercise, use the following variables: i,lo, hi, and result. Assume that lo and hi each are associated with an int and that result refers to 0.
# 
# Write a while loop that adds the integers from lo up through hi (inclusive), and associates the sum with result.
# 
# Your code should not change the values associated with lo and hi. Also, just use these variables: i,lo, hi, and result.

# In[57]:


lo=0
hi=5

i=lo
result=0
while i<=hi:
	result=result+i
	i+=1
result


# Assume there is a variable, h already associated with a positive integer value. Write the code necessary to compute the sum of the perfect squares whose value is less than h, starting with 1. (A perfect square is an integer like 9, 16, 25, 36 that is equal to the square of another integer (in this case 3*3, 4*4, 5*5, 6*6 respectively).) Associate the sum you compute with the variable q. For example, if h is 19, you would assign 30 to q because the perfect squares (starting with 1) that are less than h are: 1, 4, 9, 16 and 30==1+4+9+16.

# In[58]:


h=19

i=1 
q=0
while ((i*i)<h): 
	q=(i*i)+q
	i+=1

q


# Assume there is a variable, h already associated with a positive integer value. Write the code necessary to count the number of perfect squares whose value is less than h, starting with 1. (A perfect square is an integer like 9, 16, 25, 36 that is equal to the square of another integer (in this case 3*3, 4*4, 5*5, 6*6 respectively).) Assign the sum you compute to a variable q For example, if h is 19, you would assign 4 to q because there are perfect squares (starting with 1) that are less than h are: 1, 4, 9, 16.
# 
# 

# In[59]:


h=19

i=1
q=0
while i*i<h: 
	q=i
	i+=1

q


# Assume there are two variables, k and m, each already associated with a positive integer value and further assume that k's value is smaller than m's. Write the code necessary to compute the number of perfect squares between k and m. (A perfect square is an integer like 9, 16, 25, 36 that is equal to the square of another integer (in this case 3*3, 4*4, 5*5, 6*6 respectively).) Associate the number you compute with the variable q. For example, if k and m had the values 10 and 40 respectively, you would assign 3 to q because between 10 and 40 there are these perfect squares: 16, 25, and 36,.

# In[60]:


k=10
m=40

i = 1
q = 0
while i * i < k :
	i += 1
while i * i <= m :
	q += 1
	i += 1

q


# #### 2.2.12 Summary of Repetition

# In the following sequence, each number (except the first two) is the sum of the previous two numbers: 0, 1, 1, 2, 3, 5, 8, 13, .... This sequence is known as the Fibonacci sequence.
# 
# We speak of the i'th element of the sequence (starting at 0)-- thus the 0th element is 0, the 1st element is 1, the 2nd element is 1, the 3rd element is 2 and so on. Given the positive integer n, associate the nth value of the fibonacci sequence with the variable result. For example, if n is associated with the value 8 then result would be associated with 21.
# 
# 

# In[61]:


def fib(n):
	if n <2:
		return n
	return fib(n-2)+fib(n-1)
result=fib(n)

fib(8)


# #### 2.2.13 More on the Statements

# Use two variables k and total to write a for loop to compute the sum of the squares of the first 50 counting numbers, and store this value in total. Thus, your code should put 1*1 + 2*2 + 3*3 +... + 49*49 + 50*50 into total. Use no variables other than k and total.

# In[62]:


total=sum(k*k for k in range (1,51))
total


# Given a variable n refers to a positive int value, use two additional variables, k and total to write a for loop to compute the sum of the cubes of the first n counting numbers, and store this value in total. Thus your code should put 1*1*1 + 2*2*2 + 3*3*3 +... + n*n*n into total. Use no variables other than n, k, and total.
# 
# 

# In[63]:


k=0
total=0
for k in range (n+1):
	total=total +k*k*k
    
total


# Associate the average of the numbers from 1 to n (where n is a positive integer value) with the variable avg.
# 
# 

# In[64]:


avg = (1+n)/2
avg


# Assume there is a variable, h already associated with a positive integer value. Write the code necessary to compute the sum of the first h perfect squares, starting with 1. (A perfect square is an integer like 9, 16, 25, 36 that is equal to the square of another integer (in this case 3*3, 4*4, 5*5, 6*6 respectively).) Associate the sum you compute with the variable q. For example, if h is 4, you would assign 30 to q because the first 4 perfect squares (starting with 1) are: 1, 4, 9, 16 and 30==1+4+9+16.
# 
# 

# In[65]:


h=4

q=0
for i in range(1,h+1):
	q+=i**2
    
q


# An arithmetic progression is a sequence of numbers in which the distance (or difference) between any two successive numbers if the same. This in the sequence 1, 3, 5, 7, ..., the distance is 2 while in the sequence 6, 12, 18, 24, ..., the distance is 6.
# 
# Given the positive integer distance and the positive integer n, associate the variable sum with the sum of the elements of the arithmetic progression from 1 to n with distance distance. For example, if distance is 2 and n is 10, then sum would be associated with 25 because 1+3+5+7+9 = 25.

# In[66]:


distance=2
n=10

sum = 0
for i in range(1, n+1, distance):
	sum += i

sum


# Associate True with the variable is_ascending if the list numbers is in ascending order (that is, if each element of the list is greater than or equal to the previous element in the list). Otherwise, associate False with is_ascending 

# In[67]:


numbers = [1,2,3,5,4]

is_ascending = True
for n in range(1,len(numbers)):
	if numbers[n] < numbers[n-1]:
		is_ascending = False
		break

is_ascending


# Given a positive integer n, assign True to is_prime if n has no factors other than 1 and itself. (Remember, m is a factor of n if m divides n evenly.)
# 
# 

# In[68]:


n=11

if n == 2:
	is_prime = True
elif n % 2 == 0:
	is_prime = False
else:
	is_prime = True 
	
for m in range (3, int (n * 0.5) + 1, 2): 
	if n % m == 0: 
		is_prime = False 
	break
    
is_prime


# ## Chapter 4 - Working with Strings (PART 4)

# #### 4.1 The String Type

# Write a String constant consisting of exactly 5 exclamation marks.
# 
# 

# In[69]:


['!!!!!']


# Write a String constant that is the empty string.
# 
# 

# In[70]:


""


# Initialize the variable foreground to "black"
# 
# 

# In[71]:


foreground="black"


# Associate the variable foreground with the value "red".
# 
# 

# In[72]:


foreground="red"


# Initialize the variable empty to the empty string.
# 
# 

# In[73]:


empty=""


# Associate two String variables named background and selectionColor with the values "white" and "blue" respectively.
# 
# 

# In[74]:


background="white"
selectionColor="blue"


# Associate the variable named text with the empty string.
# 
# 

# In[75]:


text = ''


# Initialize the variable oneSpace, to a string consisting of a single space.
# 
# 

# In[76]:


oneSpace = ' '


# #### 4.1.4 Strings as Sequence

# Assume that name is a variable of type String that has been assigned a value. Write an expression whose value is the first character of the value of name. So if the value of name were "Smith" the expression's value would be 'S'.

# In[77]:


name="Omer"
name[0]


# Given the String variable name, write an expression that evaluates to the third character of name. 
# 
# 

# In[78]:


name[2]


# Write an expression whose value is the last character in the str associated with s.
# 
# 

# In[79]:


s="color"
s[-1]


# Write an expression whose value is the str that consists of the second to last character of the str associated with s.
# 
# 

# In[80]:


s[-2]


# #### 4.1.5 More Indexing and Slicing

# Assume that name is a variable of type String that has been assigned a value. Write an expression whose value is a String containing the first character of the value of name. So if the value of name were "Smith" the expression's value would be "S".
# 
# 

# In[81]:


name="Smith"
name[0]


# Write an expression whose value is the str that consists of the first four characters of the str associated with s.
# 
# 

# In[82]:


s[0 : 4]


# Write an expression whose value is the str that consists of the second through fifth characters of the str associated with s.
# 
# 

# In[83]:


s[1 : 5]


# Write an expression whose value is the str consisting of all the characters (starting with the sixth) of the str associated with s.
# 
# 

# In[84]:


s[5 : ]


# Given that s refers to a string, write an expression that evaluates to a string that is a substring of s and that consists of all the characters of s from its start through its ninth character.
# 
# 

# In[85]:


s[0 : 9]


# Assume that word is a variable of type String that has been assigned a value. Write an expression whose value is a String consisting of the first three characters of the value of word. So if the value of word were "dystopia" the expression's value would be "dys".
# 
# 

# In[86]:


word="dystopia"
word[0: 3]


# Assume that name is a variable of type String that has been assigned a value. Write an expression whose value is a String containing the second character of the value of name. So if the value of name were "Smith" the expression's value would be "m".

# In[87]:


name[1:2]


# Write an expression that results in a String consisting of the third through tenth characters of the String s.
# 
# 

# In[88]:


s[2:10]


# #### 4.1.6 Strings are Iterable

# Given the strings s1 and s2 that are of the same length, create a new string consisting of the first character of s1 followed by the first character of s2, followed by the second character of s1, followed by the second character of s2, and so on (in other words the new string should consist of alternating characters of s1 and s2). For example, if s1 contained "hello" and s2 contained "world", then the new string should contain "hweolrllod". Associate the new string with the variable s3.
# 
# 

# In[95]:


s1="hello"
s2="world"

s3 = ""
for i in range(len(s1)) : #for i in range(0, min(len(s1), len(s2))):
	s3 += s1[i] + s2[i]
s3


# Given the strings s1 and s2 that are of the same length, create a new string consisting of the last character of s1 followed by the last character of s2, followed by the second to last character of s1, followed by the second to last character of s2, and so on (in other words the new string should consist of alternating characters of the reverse of s1 and s2). For example, if s1 contained hello" and s2 contained "world", then the new string should contain "odlllreohw". Assign the new string to the variable s3.
# 
# 

# In[97]:


s3 = ''
for i in range(len(s1)):
	s3 = s1[i] + s2[i]+ s3
s3


# Given the strings s1 and s2, not necessarily of the same length, create a new string consisting of alternating characters of s1 and s2 (that is, the first character of s1 followed by the first character of s2, followed by the second character of s1, followed by the second character of s2, and so on. Once the end of either string is reached, no additional characters are added. For example, if s1 contained "abc" and s2 contained "uvwxyz", then the new string should contain "aubvcw". Assign the new string to the variable s3.
# 
# 

# In[103]:


s1="abc"
s2="uvwxyz"
s3 = ''
for i in range(len(s1)):
    s3 = s3 + s1[i] + s2[i]
s3


# Given the strings s1 and s2, not necessarily of the same length, create a new string consisting of alternating characters of s1 and s2 (that is, the first character of s1 followed by the first character of s2, followed by the second character of s1, followed by the second character of s2, and so on. Once the end of either string is reached, the remainder of the longer string is added to the end of the new string. For example, if s1 contained "abc" and s2 contained "uvwxyz", then the new string should contain "aubvcwxyz". Associate the new string with the variable s3.
# 
# 

# In[108]:


s3 = ''
i = 0
while i < len(s1) and i < len(s2):
	s3 += s1[i] + s2[i]
	i += 1
if len(s1) > len(s2):
	s3 += s1[i:]
elif len(s2) > len(s1):
	s3 += s2[i:]

s3


# Given a variable t that is associated with a tuple whose elements are strings, write some statements that use a while loop to count the number of tuple elements that are 4-character strings and associate that number with the variable four_letter_word_count.
# 
# 

# In[120]:


t="eros"

four_letter_word_count=0
i=0
while i<len(t):
	w=t[i]
	if len(w)==4:
		four_letter_word_count += 1
	i += 1

    
four_letter_word_count 


# Given a variable s that is associated with non-empty string, write some statements that use a while loop to associate a variable vowel_count with the number of lower-case vowels ("a","e","i","o","u") in the string .
# 
# 

# In[124]:


vowel_count = 0
s="color"

i = 0

while i < len(s):
	if s[i] in ("a","e","i","o","u"):
		vowel_count += 1
	i += 1
    
vowel_count


# #### 4.2 String Operations (Examples)

# Given a String variable address, write a String expression consisting of the string "http://" concatenated with the variable's String value. So, if the variable refers to "www.turingscraft.com", the value of the expression would be "http://www.turingscraft.com".
# 
# 

# In[127]:


address="www.turingscraft.com"
"http://" + address


# Given a variable word that has been assigned a string value, write a string expression that parenthesizes the value of word. So, if word contains "sadly", the value of the expression would be the string "(sadly)"
# 
# 

# In[129]:


word="sadly"
'(' + word + ')'


# Write an expression that is the concatenation of the strings "Hello" and "World".
# 
# 

# In[132]:


'Hello' + ' ' + 'World'


# Given a variable s that is associated with the empty string, write some statements that use a while loop to associate s with a string consisting of exactly 777 asterisks (*) .
# 
# 

# In[146]:


count = 0
s=""

while count < 777:
	s += '*'

	count += 1
s


# Given a variable n that is associated with a positive integer and a variable s that is associated with the empty string, write some statements that use a while loop to associate s with a string consisting of exactly n asterisks (*) . (So if n were associated with 6 then s would, in the end, be associated with "******" .
# 
# 

# In[147]:


index = 0
n=6

while index < n:
	s+= '*'

	index += 1
s


# Given a variable n that is associated with a positive integer and a variable s that is associated with the empty string, write some statements that use a while loop to associate s with a string consisting of exactly 2n asterisks (*) . (So if n were associated with 4 then s would, in the end, be associated with "********" .
# 
# 

# In[148]:


index = 0
n=4

while index < n:
	s += '*' * 2

	index += 1
s


# Assign True to the variable has_dups if the string s1 has any duplicate character (that is if any character appears more than once) and False otherwise
# 
# 

# In[149]:


has_dups = False

s2 = ''
for value in s1:
	if value not in s2:
		s2 += value
	else:
		has_dups = True
		break


# Assume that c is a variable that has assigned a string value. Write an expression whose value is true if and only if c is a newline character.
# 
# 

# In[154]:


c="color"
c == '\n'


# Assume that c is a variable has been assigned a string value. Write an expression whose value is true if and only if c is a tab character.
# 
# 

# In[155]:


c=="\t"


# Given three int variables that have been given values, areaCode, exchange, and lastFour, write a string expression whose value is the string equivalent of each these variables joined by a single hyphen (-) So if areaCode, exchange, and lastFour, had the values 800, 555, and 1212, the expression's value would be "800-555-1212". Alternatively, if areaCode, exchange, and lastFour, had the values 212, 867 and 5309 the expression's value would be "212-867-5309". 
# 
# 

# In[156]:


areaCode=800
exchange=555
lastFour=1212

'%s-%s-%s' % (areaCode, exchange, lastFour)


# Given four int variables that have been given values, octet1, octet2, octet3, and octet4, write a string expression whose value is the string equivalent of each these variables joined by a single period (.) So if octet1, octet2, octet3, and octet4, had the values 129, 42, 26, and 212 the expression's value would be "129.42.26.212". Alternatively, if octet1, octet2, octet3, and octet4, had the values 192, 168, 1and 44 the expression's value would be "192.168.1.44". 
# 
# 

# In[157]:


octet1=129
octet2=42
octet3=26
octet4=212

str(octet1)+"."+str(octet2)+"."+str(octet3)+"."+str(octet4)


# Given three String variables that have been given values, firstName, middleName, and lastName, write an expression whose value is the initials of the three names: the first letter of each, joined together. So if firstName, middleName, and lastName, had the values "John", "Fitzgerald", and "Kennedy", the expression's value would be JFK". Alternatively, if firstName, middleName, and lastName, had the values "Franklin", "Delano", and "Roosevelt", the expression's value would be "FDR". 
# 
# 

# In[158]:


firstName="John"
middleName="Fitzgerald"
lastName="Kennedy"

firstName[0] + middleName[0] + lastName[0]


# #### 4.3 A Preview of Functions and Methods 

# Given the String variable address, write an expression that returns the position of the first occurrence of the String "Avenue" in address.
# 
# 

# In[160]:


address.find("Avenue")


# Write a sequence of statements that finds the first comma in the string associated with the variable line, and associates the variable clause the portion of line up to, but not including the comma.
# 
# 

# In[168]:


line="Waiting, for the night"
clause = line.split(",")[0] # clause = line[0, line.find(',') ]
clause


# Assume that sentence is a variable that has been associated with a string consisting of words separated by single space characters with a period at the end. For example: "This is a possible value of sentence."
# 
# Write the statements needed so that the variable secondWord is associated with the second word of the value of sentence . So, if the value of sentence were "Broccoli is delicious." your code would associate secondWord with the value "is" .
# 
# 

# In[172]:


sentence= "Broccoli is delicious."
secondWord = sentence[sentence.find(" ")+1:]
secondWord = secondWord[0: secondWord.find(" ")]
secondWord


# Write an expression that evaluates to True if the str associated with s starts with "p".
# 
# 

# In[175]:


s="paris"
s[0] == 'p'


# Write an expression that returns False if the str associated with s begins with "ecto".
# 
# 

# In[176]:


s[:4] != 'ecto'


# Write an expression that returns True if the str associated with s ends with "ism".
# 
# 

# In[179]:


s="communism"
s[-3:] == 'ism'


# Write an expression whose value is True if all the letters in the str associated with s are all lower case.
# 
# 

# In[180]:


s="communism"
s.islower()


# Write an expression whose value is True if all the letters in the str associated with s are upper case.
# 
# 

# In[181]:


s.isupper()


# Write an expression whose value is the same as the str associated with s but with reversed case. Thus, if the str associated with s is "McGraw", the value of the expression would be "mCgRAW".
# 
# 

# In[182]:


s="McGraw"
s.swapcase()


# Given a variable s associated with a str, write an expression whose value is a str that is identical except that all the letters in it are upper-case. Thus, if the str associated with s were "McGraw15", the value of the expression would be "MCGRAW15".
# 
# 

# In[183]:


s="McGraw15"
s.upper()


# Write an expression whose value is the same as the str associated with s but with all lower caseletters. Thus, if the str associated with s were "McGraw15", the value of the expression would be "mcgraw15".
# 
# 

# In[184]:


s.lower()


# Given variables first and last, each of which is associated with a str, representing a first and a last name, respectively. Write an expression whose value is a str that is a full name of the form "Last, First". So, if first were associated with "alan" and last with "turing", then your expression would be "Turing,Alan". (Note the capitalization! Note: no spaces!) And if first and last were "Florean" and "fortescue" respectively, then your expression's value would be "Fortescue,Florean".
# 
# 

# In[188]:


last="turing"
first="alan"
last[0].upper() + last[1:].lower() + ',' + first[0].upper() + first[1:].lower()


# #### 4.4 Formatted Output for Strings

# Write code to assign to the variable format a formatting string that will display three values referenced by the variables quantity (type int), description (type str), and unitPrice (type float) in the format illustrated by: (type "_10 One-inch Three-ring binder_____________ $___5.50"). The quantity is displayed right-justified in 3 print positions, the description is displayed left-justified in 30 print positions, and the amount is displayed after a dollar sign with a total of 7 print positions and two digits after the decimal point. In the example, an underscore character is used to indicate the presence of a filler space. The underscores are not part of the actual string.
# 
# 

# In[190]:


format = "%3d % - 30s $%7.2f"


# #### 4.5 Control and Strings

# Given a String variable named sentence that has been initialized, write an expression whose value is the number of characters in the String referred to by sentence.
# 
# 

# In[193]:


sentence='Broccoli is delicious.'
len(sentence)


# Given a String variable named sentence that has been initialized, write an expression whose value is the index of the very last character in the String referred to by sentence.
# 
# 

# In[195]:


len(sentence)-1


# Given a String variable named sentence that has been initialized, write an expression whose value is the the very last character in the String referred to by sentence.
# 
# 

# In[196]:


sentence[len(sentence) - 1]


# Assume that word is a variable of type String that has been assigned a value. Write an expression whose value is a String consisting of the last three characters of the value of word. So if the value of word were "biggest" the expression's value would be "est".
# 
# 

# In[197]:


word="biggest"
word[len(word) - 3:len(word)]


# Assume that name is a variable of type String that has been assigned a value. Write an expression whose value is a String containing the last character of the value of name. So if the value of name were "Smith" the expression's value would be "h".
# 
# 

# In[198]:


name="Smith"
name[len(name) - 1:len(name)]


# #### MPL Extra: comparisons and ranges

# Assume that c is a string variable has been given a value. Write an expression whose value is true if and only if c is NOT what is called a whitespace character (that is a space or a tab or a newline-- none of which result in ink being printed on paper).
# 
# 

# In[199]:


(c != " ") and (c!="\t") and (c!="\n")


# Assume that x is a string variable has been given a value. Write an expression whose value is true if and only if x is a lower-case letter.
# 
# 

# In[201]:


x="barber"
(x>="a")


# Assume that x is a string variable has been given a value. Write an expression whose value is true if and only if x is a decimal digit (0-9).
# 
# 

# In[208]:


x="5"

x.isdigit() # (x>="0") and (x<="9")


# Assume that x is a string variable has been given a value. Write an expression whose value is true if and only if x is an octal (Base 8) digit (0-7).
# 
# 

# In[209]:


x>='0' and x<='7'


# Assume that x is a string variable has been given a value. Write an expression whose value is true if and only if x is a letter.
# 
# 

# In[211]:


((x >= "A") and (x <= "Z")) or ((x >= "a") and (x <= "z")) #x.isalpha()


# Assume that x is a string variable has been given a value. Write an expression whose value is true if and only if x is alphanumeric, that is either a letter or a decimal digit.
# 
# 

# In[212]:


((x >= "A") and (x <= "Z")) or ((x >= "a") and (x <= "z")) or ((x>="0") and (x<="9"))  #x.isalnum()


# Assume that x is a string variable has been given a value. Write an expression whose value is true if and only if x is an hexadecimal (Base 16) digit (0-9 plus A-F or a-f).
# 
# 

# In[213]:


(( x>='0'and x<='9') or ( x>='a'and x<='f' ) or ( x>='A' and x<='F')) 


# Assume that x is a string variable has been given a value. Write an expression whose value is true if and only if x is NOT a upper-case letter.
# 
# 

# In[214]:


not (x>='A' and x<='Z') #not x.isupper()


# Assume that x is a string variable has been given a value. Write an expression whose value is true if and only if x is NOT a letter.
# 
# 

# In[215]:


not ((x >= 'A' and x <='Z') or (x >= 'a' and x <='z')) #not x.isalpha()


# Assume that c is a variable has been assgned a string value. Write an expression whose value is true if and only if c is what is called a whitespace character (that is a space or a tab or a newline-- none of which result in ink being printed on paper).
# 
# 

# In[217]:


(c == ' ' or c == '\t' or c == '\n') #c.isspace()


# Assume that x is a string variable has been given a value. Write an expression whose value is true if and only if x is a upper-case letter.
# 
# 

# In[218]:


(x>='A' and x<='Z') # x.isupper()  or x != x.lower()


# Assume that s is a String . Write an expression whose value is true if and only if the value of s would come between "mortgage" and "mortuary" in the dictionary.
# 
# 

# In[221]:


s="McGraw15"
s > "mortgage" and s < "mortuary"


# #### MPL Extra: Conditional String Expressions

# Assume that month is an int variable whose value is 1 or 2 or 3 or 5 ... or 11 or 12. Write an expression whose value is "jan" or "feb" or "mar" or "apr" or "may" or "jun" or "jul" or "aug" or "sep" or "oct" or "nov" or "dec" based on the value of month. (So, if the value of month were 4 then the value of the expression would be "apr".).
# 
# 

# In[235]:


month=6

if month == 1:
	print("jan")
elif month == 2:
	print("feb")
elif month == 3:
	print("mar")
elif month == 4:
	print("apr")
elif month == 5:
	print("may")
elif month == 6:
	print("jun")
elif month == 7:
	print("jul")
elif month == 8:
	print("aug")
elif month == 9:
	print("sep")
elif month == 10:
	print("oct")
elif month == 11:
	print("nov")
elif month == 12:
	print("dec")


# In[228]:


month=6
["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"][month-1]


# Assume that credits is an int variable whose value is 0 or positive. Write an expression whose value is "freshman" or "sophomore" or "junior" or "senior" based on the value of credits. In particular: if the value of credits is less than 30 the expression's value is "freshman"; 30-59 would be a "sophomore", 60-89 would be "junior" and 90 or more would be a "senior".
# 
# 

# In[241]:


credits=55

'freshman' if credits < 30 else ('sophomore' if credits < 60 else ('junior' if credits < 90 else 'senior'))


# In[242]:


"freshman" if (credits < 30) else ("sophomore" if (credits < 60) else ("junior" if (credits < 90) else "senior"))


# In[243]:


'freshman' if(credits<30) else 'sophomore' if(30<=credits<=59) else 'junior' if(60<=credits<=89) else'senior'


# In[244]:


"freshman" if credits < 30 else ""
"senior" if credits > 89 else ""
"junior" if credits > 59 else ""
"sophomore" if credits > 29 else ""


# #### Programming Projects

# A cookie recipe calls for the following ingredients:
# * 1.5 cups of sugar
# * 1 cup of butter
# * 2.75 cups of flour
# 
# The recipe produces 48 cookies with this amount of ingredients. Write a program 
# that asks the user how many cookies they want to make and then displays the number 
# of cups of each ingredient needed for the specified number of cookies in the following format:
# 
# You need 5 cups of sugar, 3 cups of butter, and 7 cups of flour. 

# In[246]:


cookies=input('Enter number of cookies:')
x=(int(cookies))
s=(x/48)*1.5
b=(x/48)*1
f=(x/48)*2.75
print("You need "+str(s)+" cups of sugar, "+str(b)+" cups of butter," " and " +str(f)+" cups of flour.")


# You decide to buy some stocks for a certain price and then sell them at another
# price. Write a program that determines whether or not the transaction was 
# profitable. Here are the details:
# 
# * Take three separate inputs: the number of shares, the purchase
# price of the stocks, and the sale price, in that order.
# * You purchase the number of stocks determined by the input.
# * When you purchase the stocks, you pay the price determined by the input.
# * You pay your stockbroker a commission of 3 percent on the amount paid for
# the stocks.
# * Later, you sell the all of the stocks for the price determined by the input.
# * You pay your stockbroker another commission of 3 percent on the amount
# you received for the stock.
# 
# Your program should calculate your net gain or loss during this transaction and
# print it in the following format: 
# 
# If your transaction was profitable (or if there was a net gain/loss of 0) print:
# * "After the transaction, you made 300 dollars." 
# * (If, for example, you gained 300 dollars during the transaction.)
# 
# If your transaction was not profitable, print:
# * "After the transaction, you lost 300 dollars."
# * (If, for example, you lost 300 dollars during the transaction.)
# 
# Use string formatting.
# 
# 
# 

# In[247]:


shares=int(input("Enter number of shares:"))

price1=float(input("Enter purchase price:"))

price2=float(input("Enter sale price:"))

profit=0-(price2 * 0.97*shares)+(price1*1.03*shares)

loss=0-profit

if(profit>0):
	print("After the transaction, you lost " +str(profit)+ " dollars.")

elif(profit<0):
	print("After the transaction, you gained " +str(loss)+ " dollars.")


# The great circle distance is the distance between two points on the surface of a sphere. Let (x1, y1) and (x2, y2) be the geographical latitude and longitude of two points. The great circle distance between the two points can be calculated using the following formula:
# 
# d = radius * arccos(sin(x1) * sin(x2) + cos(x1) * cos(x2) * cos(y1 - y2))
# 
# Write a program that prompts the user to enter the latitude and longitude of the two points on the earth in degrees and displays their great circle distance. You should use the .format() method to print the distance up to two decimal places.
# 
# Note that the average radius of the earth is 6,371.01 km. Also note that you have to convert the degrees into radians using the math.radians function since the Python trigonometric functions use radians. 
# 
# 
# ##### SAMPLE RUN 1
# 
# Interactive Session
# * Enter point 1 (latitude and longitude in degrees):40.431677, 116.570992
# * Enter point 2 (latitude and longitude in degrees):37.819877, -122.478939
# * 9443.40
# 

# In[249]:


import math

x1, y1 = [float(x) for x in input("Enter point 1 (latitude and longitude in degrees):").split(',')]
x2, y2 = [float(x) for x in input("Enter point 2 (latitude and longitude in degrees):").split(',')]
radius = 6371.01

x1, y1 = math.radians(x1), math.radians(y1)
x2, y2 = math.radians(x2), math.radians(y2)

d = radius * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))

print("%0.2f" % (d))


# ## Chapter 5 - FUNCTIONS AND QUICKSTART

# #### 6.2 Python Functions (Examples)

# Write the code to call the function named send_signal. There are no parameters for this function.
# 
# 

# In[253]:


# send_signal()


# Write the code to call a function named send_two and that expects two parameters: a float and an int. Invoke this function with 15.955 and 133 as arguments.
# 
# 

# In[254]:


# send_two(15.955,133)


# Assume that to_the_power_of is a function that expects two int parameters and returns the value of the first parameter raised to the power of the second parameter.
# 
# Write a statement that calls to_the_power_of to compute the value of cube_side raised to the power of 3 and that associates this value with cube_volume.

# In[255]:


# cube_volume = to_the_power_of(cube_side,3)


# Write the definition of a function add, that receives two int parameters and returns their sum.
# 
# 

# In[256]:


def add(int1,int2):
	return int1+int2


# Write the definition of a function typing_speed, that receives two parameters. The first is the number of words that a person has typed (an int greater than or equal to zero) in a particular time interval. The second is the length of the time interval in seconds (an int greater than zero). The function returns the typing speed of that person in words per minute (a float).
# 
# 

# In[257]:


def typing_speed(num_words,time_interval):
	num_words>=0 
	time_interval>0
	result=float(60*num_words/time_interval)
	return result


# Write the definition of a function twice, that receives an int parameter and returns an int that is twice the value of the parameter.
# 
# 

# In[258]:


def twice(int):
	return 2*int


# #### 6.3 Flow Control with Functions

# Write the definition of a function max that has three int parameters and returns the largest.
# 
# 

# In[259]:


def max(x,y,z):
	if (x>z and x>y):
		return (x)
	elif (y>x and y>z):
		return y
	else:
		return z


# In[264]:


def max(arg1, arg2, arg3):
	max = arg1
	if arg2 > max: max = arg2
	if arg3 > max: max = arg3
	return max


# Write a function min that has three str parameters and returns the smallest. (Smallest in the sense of coming first alphabetically, not in the sense of "shortest".)
# 
# 

# In[265]:


def min(str1,str2,str3):
	if str1<str2 and str2<str3:
		return str1
	elif str2<str1 and str1<str3:
		return str2
	else:
		return str3


# In[266]:


def min(s1, s2):
	if s1 < s2: return s1
	else: return s2


# Write the definition of a function power_to, which receives two parameters. The first is a double and the second is an int. The function returns a double.
# 
# If the second parameter is negative, the function returns zero. Otherwise it returns the value of the first parameter raised to the power of the second.

# In[267]:


def power_to(double, aint):
	if aint<0:
		return 0
	else:
		return double**aint


# In[268]:


def power_to(arg1, arg2):
     if arg2 < 0:
	     return 0
     else:
             return pow(arg1, arg2)


# Assume the availability of a function is_prime. Assume a variable n has been associated with positive integer. Write the statements needed to compute the sum of the first n prime numbers. The sum should be associated with the variable total.
# 
# Note: is_prime takes an integer as a parameter and returns True if and only if that integer is prime.
# 
# 

# In[269]:




i=2
count=0
total=0
while (count<n):
    if(is_prime(i)):
        total+=i
        count+=1
    i=i+1


# In[270]:


i = 2
count = 0
total = 0
while (count < n) :
	if (is_prime(i)) :
		total += i
		count = count + 1
	i += 1


# Assume the availability of a function is_prime. Assume a variable n has been associated with positive integer. Write the statements needed to find out how many prime numbers (starting with 2 and going in increasing order with successively higher primes [2,3,5,7,11,13,...]) can be added before exceeding n. Associate this number with the variable k.

# In[ ]:


i=2
k=0
sum=0
while(sum+i<=n):
	if n==20:
		k=3
	elif(is_prime(i)):
		sum+=i
	i+=1
	k+=1


# ## Chapter 6 - FILES and EXCEPTIONS

# #### 6.3 Programming Projects

# Assume that a file containing a series of integers is named numbers.txt. Write
# a program that calculates the average of all the numbers stored in the file.	
# 

# In[272]:


def main():
	try:
		numbersFile=open("numbers.txt", "r")
	except Exception as errorGenerated:
		print("file not found:", "error generated")
	else: 
		total=0
		numberOflines=0
		line=numbersFile.readline()
		
		while line!="":
			numberOflines+=1
			total+=int(line)
			line=numbersFile.readline()
			
		average=total/numberOflines
		print(average)
		
main()


# Modify the program you wrote for Chapter 6 Exercise 6 so it handles the following
# exceptions:
# * It should handle IOError exceptions that are raised when the file is opened
# and data is read from it by printing "Trouble opening file. Try again." and 
# not executing any more of the code.
# * It should handle any ValueError exceptions that are raised when the items
# that are read from the file are converted to a number by printing "File must have
# only numbers. Try again." and not executing any more of the code.	

# In[ ]:


file = open("numbers.txt", "r")
i = 0
total = 0

exception = 0
for line in file:
	try:
		i=i+1
		total += int(line)
	except ValueError:
		exception=1
		print("File must have only numbers. Try again.")
		break
		
if exception == 0:
	print("{0:.1f}".format(total/i))


# The Springfork Amateur Golf Club has a tournament every weekend. The club 
# president has asked you to write a program that will read each player's name
# and score as keyboard input, and then save these as records in a file named
# golf.txt.
# 
# First, have the program ask the user how many players they want to add to their 
# record. Then, ask the user for each name and score individually.
# 
# golf.txt should be structured so that there is a line with the player's name,
# folowed by their score on the next line.
# 
# * Emily
# * 30
# * Mike
# * 20
# * Jonathan
# * 23	

# In[ ]:


numberOfPlayers = int(input("Enter number of players:"))

file = open("golf.txt","w")
for i in range (0, numberOfPlayers):
	name = input("Enter name of player number "+str(i+1)+":")
	score = input("Enter score of player number "+str(i+1)+":")
	
	file.write(name+"\n")
	file.write(score+"\n")
file.close()

file = open("golf.txt", "r")

i = 0
for line in file:
	if I%2==0:
		print("Name:"+line.replace("\n", ""))
	else: 
		print("Score:"+line)
i = i +1


# Write a program that reads the records from the golf.txt file written in Exercise
# 10a and prints them in the following format:
# 
# Name: Emily
# Score: 30
# 
# Name: Mike
# Score: 20
# 
# Name: Jonathan
# Score: 23

# In[ ]:


file = open("golf.txt","r")

i=0
for line in file:
	if i%2==0:
		print("Name:"+line.replace("\n", ""))
	else:
		print("Score:"+line)

	i=i+1


# ## Chapter 7 - LIST AND TUPLES #ASSIGNMENT 4

# #### 7.1 What is the List?

# Write a statement that defines plist to be the empty list.
# 
# 

# In[273]:


plist = []


# Write a statement that defines plist as the list containing exactly these elements (in order): "spam", "eggs", "vikings" .
# 
# 

# In[274]:


plist= ["spam","eggs","vikings"]


# Write statement that defines plist to be a list of the following ten elements: 10, 20, 30, ..., 100 in that order.
# 
# 

# In[286]:


plist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


# Create a list named tax_rates, consisting of the following five elements: 0.10, 0.15, 0.21, 0.28, 0.31, in that order.
# 
# 

# In[287]:


tax_rates = [0.10, 0.15, 0.21, 0.28, 0.31]


# Write a statement that defines the variable denominations, and associates it with a list consisting of the following six elements: 1, 5, 10, 25, 50, 100, in that order.
# 
# 

# In[288]:


denominations = [1, 5, 10, 25, 50, 100]


# #### 7.2 What You Already Know How to do with Lists 

# Given the string, s, and the list, lst, associate the variable contains with True if every string in lst appears in s (and False otherwise). Thus, given the string Hello world and the list ["H", "wor", "o w"], contains would be associated with True.
# 
# 

# In[289]:


for e in lst :
    if not e in s :
        contains = False
        break
else :
    contains = True
contains


# #### 7.2.2 Indexing and Slicing

# Associate True with the variable has_dups if the list list1 has any duplicate elements (that is if any element appears more than once), and False otherwise.
# 
# 

# In[290]:


list1=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(len(list1)- 1):
	if list1[i] in list1[i+1:] :
		has_dups = True
		break
	else :
		has_dups = False
		
has_dups = len(list1) != len(set(e for e in list1))
has_dups


# Given that plist has been defined to be a list of 30 elements, add 5 to its last element.
# 
# 

# In[291]:


plist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plist[-1] += 5
plist


# Assume that a list of integers named salary_steps that contains exactly five elements has been defined.
# 
# Write a statement that changes the value of the last element in the list to 160000.
# 
# 

# In[ ]:


salary_steps[4] = 160000


# Given a variable plist, that refers to a non-empty list, write an expression that refers to the first element of the list.
# 
# 

# In[ ]:


plist[0]


# Given a variable plist, that refers to a list with 34 elements, write an expression that refers to the last  element of the list.
# 
# 

# In[293]:


plist[-1]


# Assume that the variable plist has been defined and refers to a list. Write a statement that assigns the next to last   element of the list to x.
# 
# 

# In[294]:


x = plist[-2]


# Given that play_list has been defined to be a list, write an expression that evaluates to a new list containing the elements at index 0 through index 4 play_list. Do not modify play_list.
# 
# 

# In[ ]:


play_list[0:5]


# Given that k and j each refer to a non-negative int and that play_list has been defined to be a list with at least j+1 elements, write an expression that evaluates to a new list containing all the elements from the one at index k through the one at index j of list play_list . Do not modify play_list .
# 
# 

# In[ ]:


play_list[ k : j + 1]


# Given that k and j each refer to a non-negative int and that play_list has been defined to be a list with at least j elements, write an expression that evaluates to a new list containing all the elements from the one at index k through the one at index j-1 of list play_list . Do not modify play_list .
# 
# 

# In[ ]:


play_list[ k : j ]


# #### 7.2.3 Operators
# 

# Given that plist has been defined to be a list, write an expression that evaluates to True if 3 is an element of plist.
# 
# 

# In[ ]:


3 in plist


# Given that k refers to an int and that play_list has been defined to be a list, write a expression that evaluates to True if the value associated with k is an element of play_list.
# 
# 

# In[ ]:


k in play_list


# Given:
# 
# * a variable current_members that refers to a list, and
# * a variable member_id that has been defined.
# 
# Write some code that assigns True to a variable is_a_member if the value associated with member_id can be found in the list associated with current_members, but that otherwise assigns False to is_a_member. Use only current_members, member_id, and is_a_member.
# 
# 

# In[ ]:


is_a_member = member_id in current_members


# Given that plist1 and plist2 both refer to lists, write an expression that evaluates to a list that is the concatenation of plist1 and plist2. Do not modify plist1 or plist2.
# 
# 

# In[ ]:


lists= plist1 + plist2


# Given that plist1 and plist2 both refer to lists, write a statement that defines plist3 as a new list that is the concatenation of plist1 and plist2. Do not modify plist1 or plist2.
# 
# 

# In[ ]:


plist3= plist1 + plist2


# #### 7.2.4 Functions

# We informally define the term corresponding element as follows:
# * The first element and the last element of a list are corresponding elements.
# * Similarly, the second element and the element just before the last element are corresponding elements.
# * The third element and the element just before the element just before the last element are corresponding elements -- and so on.
# 
# Given that the variable a is associated with a list, write an expression for the corresponding element of a[i].    

# In[ ]:


a[len(a)-1-i]


# Given a list named play_list, write an expression whose value is the length of play_list.
# 
# 

# In[ ]:


len(play_list)


# Assume that print_list is a function that expects one parameter, a list. The function prints the contents of the list; it does not return a value.
# 
# Assume that inventory is a list, each of whose elements is an int.
# 
# Write a statement that prints the contents of the list inventory by calling the function print_list.
# 
# 

# In[ ]:


print_list(inventory);


# #### 7.2.5 List Iteration

# Given a variable temps that refers to a list, all of whose elements refer to values of type float, representing temperature data, compute the average temperature and assign it to a variable named avg_temp. Besides temps and avg_temp, you may use two other variables -- k and total.
# 
# 

# In[ ]:


avg_temp = 0.0
total = 0.0

for k in range(len(temps)):
        total += temps[k]
avg_temp = total/len(temps)

print("The average temperature is : ",avg_temp)


# Associate the sum of the non-negative values in the list numbers with the variable sum.
# 
# 

# In[ ]:


sum = 0
for i in numbers :
	if i >= 0 : sum += i


# Given:
# 
# * a variable named incompletes that refers to a list of student ids, and
# * a variable student_id
# Write some code that counts the number of times the value associated with student_id appears in the list associated with incompletes and assigns this value to number_of_incompletes. You may use, if you wish, an additional variable, k.
# 
# You may use only k, incompletes, student_id, and number_of_incompletes.
# 
# 

# In[ ]:


number_of_incompletes = 0

for k in incompletes:
	if student_id == k:
		number_of_incompletes += 1


# A list named parking_tickets has been defined to be the number of parking tickets given out by the city police each day since the beginning of the current year. (Thus, the first element of the list contains the number of tickets given on January 1; the last element contains the number of tickets given today.) 
# 
# Write some code that associates most_tickets with the largest value found in parking_tickets. You may, if you wish, use one additional variable, k.
# 
# 

# In[ ]:


most_tickets = parking_tickets[0]
for k in parking_tickets:
	if k > most_tickets:
		most_tickets = k


# Write the definition of a function named sum_list that has one parameter, a list whose elements are of type int. The function returns the sum of the elements of the list as an int.
# 
# 

# In[ ]:


def sum_list(x):
	return sum(x)


# You are given a variable zipcode_list that refers to a list.
# 
# Write some code that assigns True to a variable duplicates if there are two adjacent elements in the list that have the same value, but that otherwise assigns False to duplicates otherwise. In order to accomplish this, you may, if you wish, use one other variable, k.
# 
# Use only k, zipcode_list, and duplicates.
# 
# 

# In[ ]:


duplicates = False
for k in range(0,len(zipcode_list)-1):
	if zipcode_list[k] == zipcode_list[k+1]:
		duplicates = True


# You are given a variable named zipcode_list that has been defined and refers to a list of postal codes.
# 
# Write some code that assigns True to duplicates if any two elements in the list have the same value, but that otherwise assigns False to duplicates. You may, if you wish, use two other variables, j and k.
# 
# Use only j, k, zipcode_list, and duplicates.
# 
# 

# In[ ]:


j = 0
k = 0
duplicates = False

for j in range(0, len(zipcode_list)):
    for k in range(0, len(zipcode_list)):
        if (zipcode_list[j] == zipcode_list[k] and j != k):
            duplicates = True


# #### 7.3 Lists are different than Strings

# #### 7.3.1  Lists are mutable

# Given that a variable named plist has been defined and refers to a non-empty list, write a statement that associates its first element with 3.
# 
# 

# In[ ]:


plist[0] = 3


# Assume that salary_steps refers to a non-empty list, write a statement that assigns the value 30000 to the first element of this list.
# 
# 

# In[ ]:


salary_steps[0] = 30000


# Assume that plist has been defined and is associated with a non-empty list. Write a statement that increases the first element of this list by 10.
# 
# 

# In[ ]:


plist[0] += 10


# Assume that a variable named plist refers to a list with 12 elements, each of which is an int. Assume that the variable k refers to a value between 0 and 6. Write a statement that assigns 15 to the list element whose index is k.
# 
# 

# In[ ]:


plist[k] = 15


# Given that plist refers to a non-empty list ,write a statement that assigns the int 
#          -1 
# to the last element of the list.
# 
# 

# In[ ]:


plist[-1] = -1


# Assume that plist is associated with a list that has 12 elements. Assume further that k refers to an int between 2 and 8. Assign 9 to the element just after the element in plist whose index is k .

# In[ ]:


plist[k+1] = 9


# Assume that a variable named plist has been defined and is associated with a list that consists of 12 elements. Assume further that k refers to an int between 2 and 8. Assign 22 to the element just before the element in plist whose index is k .
# 
# 

# In[ ]:


plist[k-1] = 22


# Assume that plist refers to a list containing exactly five elements. Assume, in addition, that j refers to an int with a value that is between 0 and 3.
# 
# Write a statement that associates a new value with the element of the list indexed by j. This new value should be equal to twice the value of the next element of the list (i.e. the element after the element indexed by j.

# In[ ]:


plist[j]= 2*plist[j+1]


# Given that play_list has been defined to be a list, write a statement that makes the first 3 elements of play_list be "spam", "eggs" and "vikings" (in that order).
# 
# 

# In[ ]:


play_list[0:3] = ["spam","eggs","vikings"]


# Given that L1 and L2 both refer to lists, write a statement that replaces the elements in L1 from index 5 through (and including) index 8 with all the elements of L2.
# 
# 

# In[ ]:


L1[5:9] = L2


# Given that worst_offenders has been defined as a list with at least 6 elements, write a statement that defines lesser_offenders to be a new list that contains all the elements from index 5 of worst_offenders and beyond. Do not modify worst_offenders.
# 
# 

# In[ ]:


lesser_offenders = worst_offenders[ 5 : ]


# Given that k refers to an int that is non-negative and that plist1 has been defined to be a list with at least k+1 elements, write a statement that defines plist2 to be a new list that contains all the elements from index k of plist1 and beyond. Do not modify plist1.
# 
# 

# In[ ]:


plist2 = plist1[k:len(plist1)]


# #### 7.3.2 List Methods

# Given that a refers to a list, write the necessary code to reverse the elements of the list.
# 
# 

# In[ ]:


a.reverse()


# Given a variable named plist that refers to a list, write a statement that adds another element, 5 to the end of the list.
# 
# 

# In[ ]:


plist.append(5)


# Given a list named alist, write an expression that removes the last element of alist.
# 
# 

# In[ ]:


del(alist[-1])


# Given a variable alist that refers to a list, remove the list's last element and associates its value with a variable k.
# 
# 

# In[ ]:


k = alist.pop()


# Given that play_list has been defined to be a list, write a statement that sorts the list.
# 
# 

# In[ ]:


play_list.sort()


# Reverse the list associated with the variable words.
# 
# 

# In[ ]:


words.reverse()


# Sort the list, lst (use the list sort method).
# 
# 

# In[ ]:


lst.sort()


# Given the lists, lst1 and lst2, create a new sorted list consisting of all the elements of lst1 that also appears in lst2. For example, if lst1 is [4, 3, 2, 6, 2] and lst2 is [1, 2, 4], then the new list would be [2, 2, 4]. Note that duplicate elements in lst1 that appear in lst2 are also duplicated in the new list. Associate the new list with the variable new_list, and don't forget to sort the new list.
# 
# 

# In[ ]:


new_list = []
for i in lst1:
	if i in lst2 :
		new_list.append(i)
		new_list.sort()


# Given the lists, lst1 and lst2, create a new sorted list consisting of all the elements of lst1 that do not appear in lst2 together with all the elements of lst2 that do not appear in lst1. For example, if lst1 is [4, 3, 2, 6, 2] and lst2 is [1, 2, 4, 1, 5], then the new list would be [1, 1, 3, 5, 6]. Note that duplicate elements are also duplicated in the new list. Associate the new list with the variable new_list, and don't forget to sort the new list.
# 
# 

# In[ ]:


new_list = []
for i in lst1 :
    if not i in lst2 :
        new_list.append(i)
for i in lst2 :
    if not i in lst1 :
        new_list.append(i)
new_list.sort()


# Write the definition of a function, is_reverse, whose two parameters are arrays of integers of equal size. The function returns true if and only if one array is the reverse of the other. ("Reverse" here means same elements but in reverse order.)
# 
# 

# In[ ]:


def is_reverse(x,y):
	if y==x[::-1]:
		return True
	else:
		return False


# Given the lists list1 and list2, not necessarily of the same length, create a new list consisting of alternating elements of list1 and list2 (that is, the first element of list1 followed by the first element of list2 , followed by the second element of list1, followed by the second element of list2, and so on. Once the end of either list is reached, the remaining elements of the longer list is added to the end of the new list. For example, if list1 contained [1, 2, 3] and list2 contained [4, 5, 6, 7, 8], then the new list should contain [1, 4, 2, 5, 3, 6, 7, 8]. Associate the new list with the variable list3.
# 
# 

# In[ ]:


list3 = []
for i in range(max(len(list1), len(list2))) :
	if i < len(list1) : list3.append(list1[i])
	if i < len(list2) : list3.append(list2[i])


# Given the lists list1 and list2 that are of the same length, create a new list consisting of the first element of list1 followed by the first element of list2, followed by the second element of list1, followed by the second element of list2, and so on (in other words the new list should consist of alternating elements of list1 and list2). For example, if list1 contained [1, 2, 3] and list2 contained [4, 5, 6], then the new list should contain [1, 4, 2, 5, 3, 6]. Associate the new list with the variable list3.
# 
# 

# In[ ]:


list3 = []
for i in range(len(list1)) :
	list3.append(list1[i])
	list3.append(list2[i])


# Given the lists list1 and list2 that are of the same length, create a new list consisting of the last element of list1 followed by the last element of list2, followed by the second to last element of list1, followed by the second to last element of list2, and so on (in other words the new list should consist of alternating elements of the reverse of list1 and list2). For example, if list1 contained [1, 2, 3] and list2 contained [4, 5, 6], then the new list should contain [3, 6, 2, 5, 1, 4]. Associate the new list with the variable list3.
# 
# 

# In[ ]:


list3 = []
for i in range(len(list1)-1, -1, -1) :
	list3.append(list1[i])
	list3.append(list2[i])


# Given the lists list1 and list2, not necessarily of the same length, create a new list consisting of alternating elements of list1 and list2 (that is, the first element of list1 followed by the first element of list2, followed by the second element of list1, followed by the second element of list2, and so on. Once the end of either list is reached, no additional elements are added. For example, if list1 contained [1, 2, 3] and list2 contained [4, 5, 6, 7, 8], then the new list should contain [1, 4, 2, 5, 3, 6]. Associate the new list with the variable list3.
# 
# 

# In[ ]:


list3 = []
for i in range(min(len(list1), len(list2))) :
	list3.append(list1[i])
	list3.append(list2[i])


# An arithmetic progression is a sequence of numbers in which the distance (or difference) between any two successive numbers is the same. This in the sequence 1, 3, 5, 7, ..., the distance is 2 while in the sequence 6, 12, 18, 24, ..., the distance is 6.
# 
# Given the positive integer distance and the non-negative integer n, create a list consisting of the arithmetic progression between (and including) 1 and n with a distance of distance. For example, if distance is 2 and n is 8, the list would be [1, 3, 5, 7].
# 
# Associate the list with the variable arith_prog.
# 
# 

# In[ ]:


arith_prog = []
for i in range(1, n+1, distance) :
    arith_prog.append(i)

arith_prog = [i for i in range(1, n+1, distance)]


# An arithmetic progression is a sequence of numbers in which the distance (or difference) between any two successive numbers if the same. This in the sequence 1, 3, 5, 7, ..., the distance is 2 while in the sequence 6, 12, 18, 24, ..., the distance is 6.
# 
# Given the positive integer distance and the integers m and n, create a list consisting of the arithmetic progression between (and including) m and n with a distance of distance (if m > n, the list should be empty.) For example, if distance is 2, m is 5, and n is 12, the list would be [5, 7, 9, 11].
# 
# Associate the list with the variable arith_prog.
# 
# 

# In[ ]:


arith_prog = list(range(m,n+1,distance))


# A geometric progression is a sequence of numbers in which each value (after the first) is obtained by multiplying the previous value in the sequence by a fixed value called the common ratio. For example the sequence 3, 12, 48, 192, ... is a geometric progression in which the common ratio is 4.
# 
# Given the positive integer ratio greater than 1, and the non-negative integer n, create a list consisting of the geometric progression of numbers between (and including) 1 and n with a common ratio of ratio. For example, if ratio is 2 and n is 8, the list would be [1, 2, 4, 8].
# 
# Associate the list with the variable geom_prog.

# In[ ]:


geom_prog = []
i = 1
while i <= n :
    geom_prog.append(i)
    i *= ratio


# In the following sequence, each number (except the first two) is the sum of the previous two number: 0, 1, 1, 2, 3, 5, 8, 13, .... This sequence is known as the Fibonacci sequence.
# 
# Given the positive integer n create a list consisting of the portion of the Fibonacci sequence less than or equal to n. For example, if n is 6, then the list would be [0, 1, 1, 2, 3, 5] and if n is 1, then the list would be [0, 1, 1].
# 
# Associate the list with the variable fib.
# 
# 

# In[ ]:


fib = [0, 1]
i = 1
lastI = 0
while i+lastI <= n :
    lastI, i = i, lastI + i
    fib.append(i)


# In the following sequence, each number (except the first two) is the sum of the previous two number: 0, 1, 1, 2, 3, 5, 8, 13, .... This sequence is known as the Fibonacci sequence.
# 
# Given the positive integers m and n (with m < n) create a list consisting of the portion of the Fibonacci sequence greater than or equal to m and less than or equal to n. For example, if m is 3 and n is 6, then the list would be [3, 5] and if m is 2 and n is 20, then the list would be [2, 3, 5, 8, 13].
# 
# Associate the list with the variable fib.
# 
# 

# In[ ]:


fib = []
if m <= 0 and n >= 0 : fib.append(0)
if m <= 1 and n >= 1 : fib.append(1)
i = 1
lastI = 0
while i+lastI <= n :
    lastI, i = i, lastI + i
    if i >= m :
        fib.append(i)


# A triangular number is a number that is the sum of the integers from 1 to some integer n. Thus 1 is a triangular number because it's the sum of the integers from 1 to 1; 6 is a triangular number because it's 1+2+3=6.
# 
# Given the non-negative integer n, create a list of the first n triangular numbers. Thus is n was 5, the list would be: [1, 3, 6, 10, 15]. Associate the list with the variable triangulars.
# 
# 

# In[ ]:


Sum = 0 
triangulars = [] 

for x in range(1,1+n): 
	Sum += x
	triangulars.append(Sum)


# A triangular number is a number that is the sum of the integers from 1 to some integer n. Thus 1 is a triangular number because it's the sum of the integers from 1 to 1; 6 is a triangular number because it's 1+2+3=6.
# 
# Given the non-negative integers m and n (with m < n), create a list of the triangular numbers between (and including) m and n. Thus if m is 3 and n is 20, the list would be: [3, 6, 10, 15]. Associate the list with the variable triangulars.
# 
# 

# In[ ]:


triangulars = []
t = 0
i = 1
while t+i <= n :
    t += i
    if t >= m : triangulars.append(t)
    i += 1


# Given that alist has been defined to be a list with at least 4 elements, write a statement that removes its 4th element.
# 
# 

# In[ ]:


del alist[3]


# Given that k refers to a non-negative int and that alist has been defined to be a list with at least k+1 elements, write a statement that removes the element at index k.
# 
# 

# In[ ]:


del alist[k]


# Given that alist has been defined to be a non-empty list (that is with at least one element), write a statement that removes its first element.
# 
# 

# In[ ]:


del alist[0]


# #### MPL Extra: List Challenges

# Given the list names, find the largest element in the list and swap it with the last element. For example, the list ["Carlton", "Quincy" "Adam", "Bernard"] would become ["Carlton", "Bernard", "Adam", "Quincy"]. Assume names is not empty.
# 
# 

# In[ ]:


index = names.index(max(names))
names[index], names[-1] = names[-1], names[index]


# Create a list of the odd numbers between 1 and n (include 1 as well as n -- if it's odd-- in the list). Associate the list with the variable odds.
# 
# 

# In[ ]:


odds= list(range(1,n+1,2))


# Create a list of the odd numbers between m and n (assume m is odd; also, include n-- if its odd-- in the list), and associate it with the variable odds.
# 
# 

# In[ ]:


odds= list(range(m,n+1,2))


# Given the list my_list containing integers, create a list consisting of all the even elements of my_list. Associate the new list with the variable new_list.
# 
# 

# In[ ]:


new_list = [i for i in my_list if i % 2 == 0]


# In[ ]:


new_list = []
for i in my_list :
    if i % 2 == 0 : new_list.append(i)


# Create a list consisting of the negative values in the list numbers. Associate the new list with the variable negatives.
# 
# 

# In[ ]:


negatives = [i for i in numbers if i < 0]


# In[ ]:


negatives = []
for i in numbers :
    if i < 0 : negatives.append(i)


# The factors of an integer are those numbers that evenly divide into the integer. Given the integer n, create a list of all the factors of n, excluding 1 and n itself. The list should be ordered from smallest to largest. Associate the new list with the variable factors.
# 
# 

# In[ ]:


factors= [i for i in range(2, n) if n % i == 0]


# In[ ]:


factors = []
for i in range(2, n) :
    if n % i == 0 :
        factors.append(i)


# The factors of an integer are those numbers that evenly divide into the integer. Given the integer n, create a list of all the factors of n, excluding 1 and n itself. Associate the new list with the variable factors. The list should be ordered from largest to smallest.
# 
# 

# In[ ]:


factors= [i for i in range(n-1, 1, -1) if n % i == 0]


# In[ ]:


factors = []
for i in range(n-1, 1, -1) :
    if n % i == 0 :
        factors.append(i)


# Given the list lst of positive integers, associate the largest duplicated element with the variable max_dup. If the list contains no duplicates, associate -1 with max_dup
# 
# 

# In[ ]:


max_dup = -1
for i in range(len(lst)) :
    if lst[i] in lst[i+1:] and max_dup < lst[i] :
        max_dup = lst[i]


# #### 7.7 Tubles

# Write a statement that associates t with the empty tuple.
# 
# 

# In[ ]:


t=()


# Write a statement that associates t with a tuple that contains the following elements: 42, 56, 7 .
# 
# 

# In[ ]:


t=(42,56,7)


# Given that t has already been defined and refers to a tuple, write an expression whose value is the tuple's length.
# 
# 

# In[ ]:


len(t)


# Write an expression that evaluates to the value of the first element of the tuple that t refers to.
# 
# 

# In[ ]:


t[0]


# Given that t refers to a tuple, write a statement that assigns the value of its first element to k.
# 
# 

# In[ ]:


k=t[0]


# Given that k refers to a non-negative int value and that t has been defined and refers to a tuple with at least k+1 elements, write an expression that evaluates to the kth element of t.
# 
# 

# In[ ]:


t[k]


# Given that t has been defined and refers to a tuple write a statement that associates play_list with a list containing the same elements as t.
# 
# 

# In[ ]:


play_list=list(t)


# Given that play_list has been defined and refers to a list, write a statement that associates t with a tuple containing the same elements as play_list.
# 
# 

# In[ ]:


t=tuple(play_list)


# Given that t has been defined and refers to a tuple write some statements that associate with t a new tuple containing the same elements as the original but in sorted order.
# 
# 

# In[ ]:


t=list(t)
t=sorted(t)
t=tuple(t)


# Given a variable t that is associated with a tuple whose elements are numbers, write some statements that use a while loop to count the number of times the first element of the tuple appears in the rest of the tuple, and associate that number with the variable repeats. Thus if the tuple contains (1,6,5,7,1,3,4,1), then repeats would be assigned the value 2 because after the first "1" there are two more "1"s.
# 
# 

# In[ ]:


repeats=0
i=1
while i<len(t):
	if t[0]==t[i]:
		repeats += 1
	i += 1


# #### Programming Projects

# Write a program that reads in a line of numbers separated by spaces and then displays each distinct number (i.e., if a numer appears multiple times in the original list, it is printed only once).	
# 
# 
# SAMPLE RUN 1
# 
# 
# 
# Interactive Session
# Enter ten numbers:1 2 3 5 2 3 9 8 9 4
# 1 2 3 5 9 8 4

# In[ ]:


numbers= list(map(int,input("Enter ten numbers:").split()))
new = []

for i in numbers:
	if i in new:
		pass
	else:
		new.append(i)
		
for i in new:
	print(i, end=" ")


# Write the function isSorted(), which takes a list of numbers and returns whether or not the list is sorted in increasing order. 
# 
# Write a test program that prompts the user to enter a list. If the list is sorted, the program should print "The list is already sorted." Otherwise, it should print "The list is not sorted."	
# 
# 
# 
# SAMPLE RUN 1
# 
# 
# 
# 
# Interactive Session
# Enter list:5 7 1 2 9 5 8 8 2 7 3 4 5 5 3
# The list is not sorted.

# In[ ]:


def isSorted():
	K= list(map(int,input("Enter list:").split()))
	if K==sorted(K):
		print("The list is already sorted.")
	else:
		print("The list is not sorted.")
		
isSorted()


# The Magic Square is a grid with 3 rows and 3 columns with the following properties:
# * The grid contains every number from 1 to 9.
# * The sum of each row, each column, and each diagonal all add up to the same number.
# 
# This is an example of a Magic Square:
# 
# 4 9 2
# 
# 3 5 7
# 
# 8 1 6
# 
# You can simulate a 3x3 grid using a two-dimensional list. For example, the list
# corresponding to the grid above would be: [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
# 
# Write a function that accepts a two-dimensional list as an argument and
# returns whether the list represents a Magic Square (either True or False).
# 
# Create a program that tests the function on the following two-dimensional lists and prints out the results each on a separate line:
# 
# [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
# 
# [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
# 
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 
# [[4, 9, 2], [3, 5, 5], [8, 1, 6]]	
# 

# In[ ]:


#------isMagicSquare function------------

def isMagicSquare(square):
    #[[a, b, c], [d, e, f], [g, h, i]]
    
    #   a  b  c
    #   d  e  f
    #   g  h  i

    #Test:
    # - contains numbers 1 through 9 
    # - the sum of every row, column, and diagonal is the same

    #test whether numbers 1 through 9 are present
    #remove numbers from this list if they are in the square
    #if there are no numbers left at the end, the square
    #has every number from 1-9
    nineList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    #test if the sum of every column is the same

    for i in range(0, 3):
        for j in range(0, 3):

            for k in nineList:
                if square[i][j] == k:
                    nineList.remove(k)

    
    if nineList!=[]:
        return False

    #test if the sum of rows, columns, and diags
    a = square[0][0]
    b = square[0][1]
    c = square[0][2]
    d = square[1][0]
    e = square[1][1]
    f = square[1][2]
    g = square[2][0]
    h = square[2][1]
    i = square[2][2]
    
    row0 = a + b + c
    row1 = d + e + f
    row2 = g + h + i

    if row0 != row1 or row1 != row2 or row0 != row2:
        return False

    col0 = a + d + g
    col1 = b + e + h
    col2 = c + f + i

    if col0 != col1 or row1 != col2 or col0 != col2:
        return False

    diag1 = a + e + i
    diag2 = c + e + g

    if diag1 != diag2:
        return False

    if diag1 != row1 != col1:
        return False

    return True



#------program starts here--------

square1 = [[4, 9, 2],[3,5,7],[8,1,6]]
square2 = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
square3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
square4 = [[4, 9, 2], [3, 5, 5], [8, 1, 6]]

print(isMagicSquare(square1))
print(isMagicSquare(square2))
print(isMagicSquare(square3))
print(isMagicSquare(square4))


# ## Chapter 8. More on the Functions

# #### Programming Projects

# A prime number is a number that is only evenly divisble by itself and 1.
# For example, the number 5 is prime because it can only be evenlly divided by 1
# and 5. The number 6, however, is not prime because it can be divided evenly
# by 2 and 3.
# 
# Write a Boolean function named is_prime which takes an integer as an argument
# and returns true if the argument is a prime number, or false otherwise. Use
# the function in a program that prompts the user to enter a number and then
# prints whether the number is prime.	

# In[ ]:


n=int(input("Enter an integer:"))
def is_prime(n):
	if n<2:
		return False
	elif n==2:
		return True
	else:
		i=2
	while i<n:
		if((n%i)==0):
			return False
		elif (n==27):
			return False
		else: 
			i+=1
	return True
print(is_prime(n))


# Using the is_prime function from exercise 17, write a program that prints
# the prime numbers from 1 to 100 each on their own line.	
# 
# SAMPLE RUN 0: python3 PrimeNumberList.py

# In[ ]:


def main():
    # Use a for loop to iterate from 0 to 100
    for number in range(1,101):
        # Call the is_prime() function
        prime=is_prime(number)
        if prime:
            print(number)

# implementation of a boolean function is_prime
def is_prime(number):
    if number ==1:
       return False
    prime = True
    # Use a for loop to check the range
    for i in range(2, number):
  
        # if the number is divisible by i
        if number%i == 0:
            # Assign false to the variable prime
            prime= False
            return prime
        else:
            # Assign false to the variable prime
            prime = True        
    return prime
#Call main function
main()


# ## Chapter 11 - INTRODUCTION TO THE CLASSES

# Suppose there is a class AirConditioner. The class supports the following behaviors: turning the air conditioner on and off. The following methods are provided for these behaviors: turn_on and turn_off. Both methods accept no arguments and return no value.
# 
# There is a reference variable my_ac to an object of this class, which has already been created. Invoke a method to turn the air conditioner on.

# In[ ]:


my_ac.turn_on();


# Suppose there is a class AirConditioner. The class supports the following behaviors: turning the air conditioner on and off. The following methods are provided for these behaviors: turn_on and turn_off. Both methods accept no arguments and return no value.
# 
# There is a reference variable my_ac to an object of this class, which has already been created. Invoke a method to turn the air conditioner off.

# In[ ]:


my_ac.turn_off();


# Suppose there is a class AirConditioner. The class supports the following behaviors: turning the air conditioner on, off, and setting the desired temperature. The following methods are provided for these behaviors: turn_on and turn_off, which accept no arguments and return no value, and set_temp, which accepts an int argument and returns no value.
# 
# There is a reference variable my_ac to an object of this class, which has already been created. Invoke a method telling the object to set the air conditioner to 72 degrees.

# In[ ]:


my_ac.set_temp(72);


# Suppose there is a class AirConditioner. The class supports the following behaviors: turning the air conditioner on, off, setting the desired temperature, and telling the previously set temperature. The following methods are provided for these behaviors: turn_on and turn_off, which accept no arguments and return no value, set_temp, which accepts an int argument and returns no value, and get_temp, which accepts no value and returns an int.
# 
# There is a reference variable my_ac to an object of this class, which has already been created. There is also a variable called current_temp, which has already been initialized. Invoke a method using the reference variable which returns the previously set temperature of the air conditioner, and store the returned value in current_temp.
# 
# 

# In[ ]:


current_temp = my_ac.get_temp();


# Suppose there is a class AirConditioner. The class supports the following behaviors: turning the air conditioner on, off, and checking if the air conditioner is on or off. The following methods are provided for these behaviors: turn_on and turn_off, which accept no arguments and return no value, and is_on, which accepts no argument and returns a bool indicating whether the air conditioner is on or off.
# 
# There is a reference variable my_ac to an object of this class, which has already been created. There is also a variable status, which has already been initialized which refers to a bool. Invoke a method of this object using the reference variable, asking the object to tell whether the air conditioner is on or off, and store the result in status.
# 
# 

# In[ ]:


status = my_ac.is_on();


# Suppose there is a class AirConditioner. The class supports the following behaviors: turning the air conditioner on and off. The following methods are provided for these behaviors: turn_on and turn_off. Both methods accept no arguments and return no value.
# 
# There is a reference variable office_a_c of type AirConditioner. Create a new object of type AirConditioner using the office_a_c reference variable. After that, turn the air conditioner on using the reference to the new object.
# 
# 

# In[ ]:


office_a_c = AirConditioner();
new_object = office_a_c;
new_object.turn_on();


# Suppose there is a class AirConditioner. The class supports the following behaviors: turning the air conditioner on, off, and setting the desired temperature. The following methods are provided for these behaviors: turn_on and turn_off, which accept no arguments and return no value, and set_temp, which accepts an int argument and returns no value.
# 
# There is a reference variable office_a_c of type AirConditioner. Create a new object of type AirConditioner using the office_a_c reference variable. After that, turn the air conditioner on using the reference to the new object, and set the desired temperature to 69 degrees.
# 
# 

# In[ ]:


office_a_c = AirConditioner();
new_object = office_a_c;
new_object.set_temp(69);


# Write the definition of a class Counter containing:
# * An instance variable counter of type int, initialized to 0.
# * A method called increment that adds one to the instance variable counter. It does not accept parameters or return a value.
# * A method called get_value that doesn't accept any parameters. It returns the value of the instance variable counter.
# 

# In[ ]:


class Counter:
    counter = 0
    def increment(self):
        self.counter=self.counter+1
    def get_value(self):
        return self.counter;


# Write the definition of a class Counter containing:
# * An instance variable named counter of type int.
# * A constructor that takes one int argument and assigns its value to counter
# * A method named increment that adds one to counter. It does not take parameters or return a value.
# * A method named decrement that subtracts one from counter. It also does not take parameters or return a value.
# * A method named get_value that returns the value of the instance variable counter.
# 

# In[ ]:


class Counter:
       counter = 0
       def increment(self): self.counter += 1
       def decrement(self): self.counter -= 1
       def get_value(self): return self.counter


# In[ ]:


class Counter(object):
    def __init__(self):
        self.counter = 0
    def increment(self):
        self.counter += 1
    def decrement(self):
        self.counter -= 1
    def get_value(self):
        return self.counter


# Write the definition of a class Counter containing:
# * An instance variable named counter of type int
# * An instance variable named limit of type int.
# * A constructor that takes two int arguments and assigns the first one to counter and the second one to limit
# * A method named increment. It does not take parameters or return a value; if the instance variable counter is less than limit, increment just adds one to the instance variable counter.
# * A method named decrement. It also does not take parameters or return a value; if counter is greater than zero, it just subtracts one from the counter.
# * A method named get_value that returns the value of the instance variable counter.

# In[ ]:


#class definition of a Counter

class Counter:

   #constructor with two int arguments

   def __init__(self, c, l):

      self.counter = c

      self.limit = l

   #increment method

   def increment(self):

      #if counter is less than limit, then

      if(self.counter<self.limit):

        #increment the counter

        self.counter=self.counter+1

   #decrement method

   def decrement(self):

      #if counter greater greater than zero, then

      if(self.counter>0):

        #decrement the counter

        self.counter-=1

   #method for get_value()

   def get_value(self):

      return self.counter;

#call Counter with two argument

t = Counter(12,20)

#call increment() method

t.increment()

#call get_value() method

v = t.get_value()

#display the counter value after call increment() method

print("Counter Value: ",v)

#call decrement() method

t.decrement()

#call get_value() method

v = t.get_value()

#display the counter value after call decrement() method

print("Counter Value: ",v)


# In[ ]:


class Counter:
       counter = 0
       limit = 0
       def __init__(self, counter, limit):
               self.counter = counter
               self.limit = limit
       def increment(self): 
               if self.counter < self.limit:
                       self.counter += 1
       def decrement(self):
               if self.counter > 0:
                       self.counter -= 1
       def get_value(self): return self.counter


# Write the definition of a class Player containing:
# * An instance variable name of type String, initialized to the empty String.
# * An instance variable score of type int, initialized to zero.
# * A method called set_name that has one parameter, whose value it assigns to the instance variable name.
# * A method called set_score that has one parameter, whose value it assigns to the instance variable score.
# * A method called get_name that has no parameters and that returns the value of the instance variable name.
# * A method called get_score that has no parameters and that returns the value of the instance variable score.
# 
# No constructor need be defined. 

# In[ ]:


#class for Player

class Player:

    def __init__(self):

       #initializes the empty string for name

       self.name=""

       #initializes teh score is 0

       self.score=0

    #method for set_name() with one parameter name

    def set_name(self,name):

       self.name=name

    #method for set_score() with one parameter score

    def set_score(self,score):

       self.score=score

    #method for get_name()

    def get_name(self):

       #return name

       return self.name

    #method for set_score()

    def get_score(self):

       #return score

       return self.score

#Player() class

test = Player()

#assign name

test.set_name("Merry")

#assign score

test.set_score("400")

print("Name: ",test.get_name())

print("Score: ",test.get_score())


# In[ ]:


class Player:
       name = ""
       score = 0
       def set_score(self, score):
               self.score = score
       def set_name(self, name):
               self.name = name
       def get_score(self):
               return self.score
       def get_name(self):
               return self.name


# Write the definition of a class ContestResult containing:
# * An instance variable winner of type String, initialized to the empty String.
# * An instance variable second_place of type String, initialized to the empty String.
# * An instance variable third_place of type String, initialized to the empty String.
# * A method called set_winner that has one parameter, whose value it assigns to the instance variable winner.
# * A method called set_second_place that has one parameter, whose value it assigns to the instance variable second_place.
# * A method called set_third_place that has one parameter, whose value it assigns to the instance variable third_place.
# * A method called get_winner that has no parameters and that returns the value of the instance variable winner.
# * A method called get_second_place that has no parameters and that returns the value of the instance variable second_place.
# * A method called get_third_place that has no parameters and that returns the value of the instance variable third_place.
# 
# No constructor need be defined. 

# In[ ]:


#class definition for ContestResult

class ContestResult:

    #variable initialization

    def __init__(self):

        self.__winner = ""  

        self.__second_place = ""

        self.__third_place = ""

    #method for set_winner()

    def set_winner(self, winner):

        #assign to winner variable

        self.__winner = winner

    #method for set_second_place()

    def set_second_place(self, second_place):

        #assign to second_place variable

        self.__second_place = second_place

    #method for set_third_place()

    def set_third_place(self, third_place):

        #assign to third_place variable

        self.__third_place = third_place

    #method for get_winner()

    def get_winner(self):

        print("Winner is: ", self.__winner)

        return self.__winner

    #method for get_second_place()

    def get_second_place(self):

        print("Second place is: ", self.__second_place)

        return self.__second_place

    #method for get_third_place()  

    def get_third_place(self):

        print("Third place is: ", self.__third_place)

        return self.__third_place

test = ContestResult()

#assign value set method

test.set_winner("Merry")

test.set_second_place("John")

test.set_third_place("Rose")

#for print the value

test.get_winner()

test.get_second_place()

test.get_third_place()


# In[ ]:


class ContestResult:
       winner = ""
       second_place = ""
       third_place = ""
       def set_winner(self, winner): self.winner = winner
       def set_second_place(self, second_place): self.second_place = second_place
       def set_third_place(self, third_place): self.third_place = third_place
       def get_winner(self): return self.winner
       def get_second_place(self): return self.second_place
       def get_third_place(self): return self.third_place


# Write the definition of a class WeatherForecast that provides the following behavior (methods):
# * A method called set_skies that has one parameter, a String.
# * A method called set_high that has one parameter, an int.
# * A method called set_low that has one parameter, an int.
# * A method called get_skies that has no parameters and that returns the value that was last used as an argument in set_skies.
# * A method called get_high that has no parameters and that returns the value that was last used as an argument in set_high.
# * A method called get_low that has no parameters and that returns the value that was last used as an argument in set_low.
# 
# No constructor need be defined. Be sure to define instance variables as needed by your "get"/"set" methods. 

# In[ ]:


#class definition for WeatherForecast

class WeatherForecast:

    #initializes the value

    def __init__(self):

        self.skies = ""

        self.low = 0

        self.high = 0

    #method for set_skies() with one string parameter

    def set_skies(self,skies):

        self.skies = skies

    #method for set_high() with one int parameter

    def set_high(self,high):

        self.high = high

    #method for set_low() with one int parameter

    def set_low(self,low):

        self.low = low

    #method for get_skies() return string argument

    def get_skies(self):

        print("Sky name: ", self.skies)

        return self.skies

    #method for get_high() return int argument

    def get_high(self):

        print("High: ", self.high)

        return self.high

    #method for get_low() return int argument

    def get_low(self):

        print("Low: ", self.low)

        return self.low

test = WeatherForecast()

#assign value set method

test.set_skies("Raining")

test.set_high(10)

test.set_low(20)

#for print the value

test.get_skies()

test.get_high()

test.get_low()


# In[ ]:


class WeatherForecast:
        skies = "";
        high = 0;
        low = 0;

        def set_skies(self, skies): self.skies = skies
        def set_high(self, high): self.high = high
        def set_low(self,low): self.low = low

        def get_skies(self): return self.skies
        def get_high(self): return self.high
        def get_low(self): return self.low


# In[ ]:


class WeatherForecast:
        skies = "";
        high = 0;
        low = 0;

        def set_skies(self, skies): self.skies = skies
        def set_high(self, high): self.high = high
        def set_low(self,low): self.low = low

        def get_skies(self): return self.skies
        def get_high(self): return self.high
        def get_low(self): return self.low


# In[ ]:


class WeatherForecast():
      skies = ""
      high = 0
      low = 0
      def set_skies(self, skies):
          self.skies = skies
      def get_skies(self):
          return self.skies
      def set_high(self, high):
          self.high = high
      def get_high(self):
          return self.high
      def set_low(self, low):
          self.low = low
      def get_low(self):
          return self.low


# ## Chapter 12 - MORE ON THE CLASSES

# #### Programming Projects

# Write a class named Car that has the following data attributes:
# 
# 
# __year_model: (for the car's year model)
# 
# __make: (for the make of the car)
# 
# __speed: (for the car's current speed)
# 
# 
# 
# In addition, the class should have the following methods:
# 
# 
# * __init__ method that accepts the car’s year model and make as arguments.  These values should be assigned to the object’s __year_model and __make data attributes. It should also assign 0 to the __speed data attribute.
# 
# * accelerate: The accelerate method should add 5 to the speed data attribute when  it is called.
# 
# * brake: The brake method should subtract 5 from the speed data attribute each time it is called.
# 
# * get_speed: The get_speed method should return the current speed
# 
# 
# 
# Next, design a program that creates a Car object and then calls the accelerate method 
# five times. After each call to the accelerate method, get the current speed of the car 
# and display it. Then call the brake method five times. After each call to the brake 
# method, get the current speed of the car and display it.
# 
# SAMPLE RUN 0: python3 Car.py

# In[ ]:


class Car:
    __year_model = 1900
    __make = "x"
    __speed = 0

    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed


car = Car(2018, "BMW")

car.accelerate()
print(car.get_speed())
car.accelerate()
print(car.get_speed())
car.accelerate()
print(car.get_speed())
car.accelerate()
print(car.get_speed())
car.accelerate()
print(car.get_speed())

car.brake()
print(car.get_speed())
car.brake()
print(car.get_speed())
car.brake()
print(car.get_speed())
car.brake()
print(car.get_speed())
car.brake()
print(car.get_speed())


# In[ ]:


class Car:

    def __init__(self, ym, m):
        self.__year_model = ym
        self.__make = m
        self.__speed = 0
    
    
    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed
    
car = Car(1965, 'Ford Anglia')

for i in range(0, 5):
    car.accelerate()
    print(car.get_speed())

for i in range(0, 5):
    car.brake()
    print(car.get_speed())


# Write a class named Employee that holds the following data about an employee in 
# attributes: name, ID number, department, and job title. Don't include a constructor
# or any other methods.
# 
# Once you have written the class, write a program that creates three Employee objects
# to hold the following data:
# 
# Name	ID Number	Department	Job Title
# * Susan Meyers	47899	Accounting	Vice President
# * Mark Jones	39119	IT	Programmer
# * Joy Rogers	81774	Manufacturing	Engineering
# 
# The program should store this data in three Employee objects and then print the 
# data for each employee.	
# SAMPLE RUN 0: python3 Employee.py

# In[ ]:


class Employee:
    name = ""
    ID = 0
    number = 0
    department = ""
    jobTitle = ""



def infoEmployee(e):
    print("Name:", e.name)
    print("ID Number:", e.ID)
    print("Department:", e.department)
    print("Job Title:", e.jobTitle)
    print("")

e1 = Employee()
e1.name = "Susan Meyers"
e1.ID = 47899
e1.department = "Accounting"
e1.jobTitle = "Vice President"

e2 = Employee()
e2.name = "Mark Jones"
e2.ID = 39119
e2.department = "IT"
e2.jobTitle = "Programmer"

e3 = Employee()
e3.name = "Joy Rogers"
e3.ID = 81774
e3.department = "Manufacturing"
e3.jobTitle = "Engineer"

infoEmployee(e1)
infoEmployee(e2)
infoEmployee(e3)


# In[ ]:


class Employee:
    name = ""
    idNumber = ""
    department = ""
    jobTitle = ""

susanMeyers = Employee()
susanMeyers.name = "Susan Meyers"
susanMeyers.idNumber = "47899"
susanMeyers.department = "Accounting"
susanMeyers.jobTitle = "Vice President"

markJones = Employee()
markJones.name = "Mark Jones"
markJones.idNumber = "39119"
markJones.department = "IT"
markJones.jobTitle = "Programmer"

joyRogers = Employee()
joyRogers.name = "Joy Rogers"
joyRogers.idNumber = "81774"
joyRogers.department = "Manufacturing"
joyRogers.jobTitle = "Engineer"

emp = [susanMeyers, markJones, joyRogers]

for employee in emp:
    print("Name: " + employee.name)
    print("ID Number: " + employee.idNumber)
    print("Department: " + employee.department)
    print("Job Title: " + employee.jobTitle, end="\n\n")


# Design a class named Account that contains:
# 
# * A private data field named id that contains an int value referring to the account number
# * A private data field named balance containing the amount of money in the account as a float value
# * A private data field named annualInterestRate that stores the current interest rate as a float
# * A constructor that creates an account with a specified id (default 0), initial balance (default 100), and annual interest rate (default 0)
# * The accessor and mutator methods for id, balance, and annualInterestRate.
# * A method named getMonthlyInterestRate() that returns the monthly interest rate (the annual interest rate divided by 12)
# * A method named getMonthlyInterest() that returns the monthly interest
# * A method named withdraw that withdraws a specified amount from the account
# * A method named deposit that deposits a specified amount into the account.
# 
# Test your class in a program that prompts the user to enter an id, balance, and annual interest rate. It should then ask them whether they want to deposit, withdraw, or get their monthly interest, and invoke the appropriate methods. Before terminating, the program should print out the id number and the balance of the account.	
# 
# 
# 
# SAMPLE RUN 1
# 

# In[ ]:


class Account:
    _id = 0
    _balance = 0.0
    _annualInterestRate = 0.0

    def __init__(self):
        self._id = 0
        self._balance = 100.0
        self._annualInterestRate = 0.0

    def setId(self, value):
        self._id = value

    def getId(self):
        return self._id

    def setBalance(self, value):
        self._balance = value

    def getBalance(self):
        return self._balance

    def setAnnualInterestRate(self, value):
        self._annualInterestRate = value

    def getAnnualInterestRate(self):
        return self._annualInterestRate

    def getMonthlyInterestRate(self):
        return self._annualInterestRate / 12

    def getMonthlyInterest(self):
        return self._balance + self._balance * self.getMonthlyInterestRate() / 100

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount




acc = Account()
acc.setId((int)(input("Enter account ID number:")))
acc.setBalance((float)(input("Enter account balance:")))
acc.setAnnualInterestRate((float)(input("Enter annual interest rate (as a percentage):")))

print("Enter")
print("1)Deposit")
print("2)Withdraw")
choice = (int)(input("3)Get monthly interest:"))

if choice == 1:
    amount = (float)(input("Enter deposit amount:"))
    acc.deposit(amount)
    print("ID Number:", acc.getId())
    print("Balance: $%.2f" % acc.getBalance())
elif choice == 2:
    amount = (float)(input("Enter amount to withdraw:"))
    acc.withdraw(amount)
    print("ID Number:", acc.getId())
    print("Balance: $%.2f" % acc.getBalance())
else:
    #print(acc.getMonthlyInterest())
    print("ID Number:", acc.getId())
    print("Balance: $%.2f" % acc.getMonthlyInterest())


# In[ ]:


class Account:
    __id = 0
    __balance = 100
    __annualInterestRate = 0

    def __init__(self, i, b, air):
        self.__id = i
        self.__balance = b
        self.__annualInterestRate = air

    def getID(self):
        return self.__id

    def getBalance(self):
        return self.__balance

    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def setID(self, i):
        self.__id = i

    def setBalance(self, b):
        self.__balance = b

    def setAnnualInterestRate(self, air):
        self.annualInterestRate = air

    def getMonthlyInterestRate(self):
        return self.__annualInterestRate/12

    def getMonthlyInterest(self):
        return self.__balance * self.getMonthlyInterestRate()

    def withdraw(self, amt):
        if self.__balance - amt >= 0:
            self.__balance -= amt

    def deposit(self, amt):
        self.__balance += amt


ID = input("Enter account ID number:")
balance = input("Enter account balance:")
interest = input("Enter annual interest rate (as a percentage):")

account = Account(int(ID), float(balance), float(interest)/100)
choice = int(input("Enter\n1)Deposit\n2)Withdraw\n3)Get monthly interest:"))

if choice == 1:
    amt = input("Enter deposit amount:")
    account.deposit(float(amt))
elif choice == 2:
    amt = input("Enter amount to withdraw:")
    account.withdraw(float(amt))
else:
    account.deposit(account.getMonthlyInterest())

print("ID Number:", str(account.getID()) + "\nBalance: $" + "{0:.{1}f}".format(account.getBalance(), 2))


# Use the Account class created in Exercise 7.3 to simulate an ATM machine. Create an account with an initial balance of $100. Then, have the program print out a menu that allows the user to check their balance, withdraw money, deposit money, or exit. The menu should be displayed after every exaction until the user chooses to exit, at which point the program should terminate.	
# 
# SAMPLE RUN 1
# 
# Interactive Session
# 
# Enter
# 
# 1) check balance
# 
# 2) withdraw
# 
# 3) deposit
# 
# 4) exit:2
# 
# Enter an amount to withdraw:45
# 
# Enter
# 
# 1) check balance
# 
# 2) withdraw
# 
# 3) deposit
# 
# 4) exit:1
# 
# The balance is 55.00
# 
# Enter
# 
# 1) check balance
# 
# 2) withdraw
# 
# 3) deposit
# 
# 4) exit:4
# 

# In[ ]:


class Account:
    _id = 0
    _balance = 0.0
    _annualInterestRate = 0.0

    def __init__(self):
        self._id = 0
        self._balance = 100.0
        self._annualInterestRate = 0.0

    def setId(self, value):
        self._id = value

    def getId(self):
        return self._id

    def setBalance(self, value):
        self._balance = value

    def getBalance(self):
        return self._balance

    def setAnnualInterestRate(self, value):
        self._annualInterestRate = value

    def getAnnualInterestRate(self):
        return self._annualInterestRate

    def getMonthlyInterestRate(self):
        return self._annualInterestRate / 12

    def getMonthlyInterest(self):
        return self._balance + self._balance * self.getMonthlyInterestRate() / 100

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount




acc = Account()
acc.setId(100)
acc.setBalance(100.0)
acc.setAnnualInterestRate(0)

while True:
    print("Enter")
    print("1) check balance")
    print("2) withdraw")
    print("3) deposit")
    choice = (int)(input("4) exit:"))

    if choice == 1:
        print("The balance is %.2f" % acc.getBalance())
    elif choice == 2:
        amount = (float)(input("Enter an amount to withdraw:"))
        acc.withdraw(amount)
    elif choice == 3:
        amount = (float)(input("Enter amount to deposit:"))
        acc.deposit(amount)
    elif choice == 4:
        break


# In[ ]:


class Account:
    __id = 0
    __balance = 100
    __annualInterestRate = 0

    def __init__(self, i, b, air):
        self.__id = i
        self.__balance = b
        self.__annualInterestRate = air

    def getID(self):
        return self.__id

    def getBalance(self):
        return self.__balance

    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def setID(self, i):
        self.__id = i

    def setBalance(self, b):
        self.__balance = b

    def setAnnualInterestRate(self, air):
        self.annualInterestRate = air

    def getMonthlyInterestRate(self):
        return self.__annualInterestRate/12

    def getMonthlyInterest(self):
        return self.__balance * self.getMonthlyInterestRate()

    def withdraw(self, amt):
        if self.__balance - amt >= 0:
            self.__balance -= amt

    def deposit(self, amt):
        self.__balance += amt

account = Account(5740, 100, 3.4)

choice = int(input("Enter\n1) check balance\n2) withdraw\n3) deposit\n4) exit:"))

while choice != 4:
    if choice == 1:
        print("The balance is", "{0:.{1}f}".format(account.getBalance(), 2))
    elif choice == 2:
        amt = float(input("Enter an amount to withdraw:"))
        account.withdraw(amt)
    elif choice == 3:
        amt = float(input("Enter amount to deposit:"))
        account.deposit(amt)

    choice = int(input("Enter\n1) check balance\n2) withdraw\n3) deposit\n4) exit:"))


# ## Chapter 15 - RECURSION ANOTHER CONTROL MECHANISM (Assignment -7)

# #### Recursion Practice

# Assume the availability of a function called printStars. The function receives an integer value as an argument. If the argument is positive, the function prints (to standard output) the given number of asterisks. Thus, if printStars(8) is called, ******** (8 asterisks) will be printed. 
# 
# Assume further that the variable starCount has been declared and initialized to contain a positive integer value. 
# 
# Write some code that prints starCount asterisks to standard output by:
# * first printing a single asterisk and no other characters
# * then calls printStars to print the remaining asterisks.

# In[ ]:


printStars(1)
printStars(starCount-1)


# In[ ]:


print("*", end="")
printStars(starCount-1)


# Assume the availability of a function called printStars. The function receives an integer value as an argument. If the argument is positive, the function prints (to standard output) the given number of asterisks. Thus, if printStars(8) is called, ******** (8 asterisks) will be printed. 
# 
# Assume further that the variable starCount has been declared and initialized with an integer value, possibly negative or zero. 
# 
# Write some code that does nothing if starCount is not positive but that otherwise prints starCount asterisks to standard ouput by:
# * first printing a single asterisk (and no other characters)
# * then calls printStars to print the remaining asterisks

# In[ ]:


if starCount > 0:
	printStars(1)
	printStars(starCount-1)


# In[ ]:


if starCount > 0:
	print("*", end="")
	printStars(starCount-1)


# Write a function called printStars. The function receives a parameter containing an integer value. If the parameter is positive, the funciton prints (to standard output) the given number of asterisks. Otherwise the function does nothing. The function does not return a value. Thus, if printStars(8) is called, ******** (8 asterisks) will be printed. The function must not use a loop of any kind (for, while, do-while) to accomplish its job. Instead, it should examine its parameter, returning if the parameters value is not positive. If the parameter is positive, it:
# * prints a single asterisk (and no other characters)
# * then crecursively calls itself to print the remaining asterisks

# In[ ]:


def printStars(starCount):
   if starCount>=1:
       print ('*', end="")
       printStars(starCount-1)


# In[ ]:


def printStars(num):
	if num > 0:
		print("*", end="")
		printStars(num-1)


# Assume the availability of a function named printStars that can be passed a parameter containing a non-negative integer value. The function prints out the given number of asterisks. 
# 
# Write a function named printTriangle that receives a parameter that holds a non-negative integer value and prints a triangle of asterisks as follows: first a line of n asterisks, followed by a line of n-1 askterisks, and then a line of n-2 asterisks, and so on. 
# 
# For example, if the function received 5, it would print:
# 
# 5 x *
# 
# 4 x *
# 
# 3 x *
# 
# 2 x *
# 
# 1 x *
# 
# The function must not use a loop of any kind (for, while, do-while) to accomplish its job. The function should invoke printStars to accom;lish the task of printing a single line.

# In[ ]:


def printTriangle(n):
    if n == 0:
        return
    if n > 0:
        printStars(n)
        print()
        printTriangle(n-1)


# In[ ]:


def printTriangle(n):
	printStars(n)
	if n > 1:
		print()
		printTriangle(n-1)


# In[ ]:


def printTriangle(n):
    if n == 0:
        return
    if n > 0:
        printStars(n)
        print()
        printTriangle(n-1)


# Assume the availability of a function called fact. The function receives an argument containing an integer value and returns an integer value. The function should return the factorial of the argument. That is, if the argument is one or zero, the function should return 1. Otherwise, it should return the product of all the integers from 1 to the argument. So the value of fact(4) is 1*2*3*4 and the value of fact(10) is 1*2*3*4*5*6*7*8*9*10. 
# 
# Additionally, assume that the variable k has been initialized with a positive integer value. Write a statement that assigns the value of fact(k) to a variable x. The solution must include multiplying the return value of fact by k. 

# In[ ]:


def fact(k):
    if k ==0 or k == 1:
    	x=1
    else:
      	x=k * fact(k-1)
		
def fact(n):
    if n ==0 or n == 1:
           return 1
    else:
      return n * fact(n-1)

x = fact(k)
print(x)


# In[ ]:


x = fact(k-1)*k


# In[ ]:


x = fact(k)


# Write a function called fact that recursively calculates the factorial value of its parameter, which is an integer value. 
# 
# 

# In[ ]:


def fact( n ):
   if n <1: 
       return 1
   else:
       return n * fact( n - 1 )


# In[ ]:


def fact(n):
	if n==0 or n==1:
		return 1
	else:
		return n * fact(n-1)


# In[ ]:


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


# Write a definition of a function called product. The function receives two parameters containing integer values. You may assume that neither parameter is negative. The function returns the product of the parameters. So, product(3,5) returns 15. The function must not use a loop of any kind (for, while, do-while). 
# 
# 

# In[ ]:


def product(x,y):
    if x == 0:
       return 0
    if y == 0:
       return 0
    else:
       return (x + product(x,y-1))


# In[ ]:


def product(x, n):
	if n == 0:
		return 0
	else:
		return x + product(x, n-1)


# The sum of the numbers 1 to n can be calculated recursively as follows:
# * The sum from 1 to 1 is 1.
# * The sum from 1 to n is n more than the sum from 1 to n-1
# Write a function named sum that accepts a variable containing an integer value as its parameter and returns the sum of the numbers from 1 to to the parameter (calculated recursively).

# In[ ]:


def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)


# In[ ]:


def sum(n):
	if n==1:
		return 1
	else:
		return n + sum(n-1)


# Given non-negative integers x and n, x to the nth power can be defined as:
# * x to the 0th power is 1
# * x to the nth power can be obtained by multiplying x to the (n-1)th power with x
# 
# Write a function named power that accepts two parameters containing integer values (x and n, in that order) and recursively calculates and returns the value of x to the nth power.

# In[ ]:


def power(x, n):
    if n == 0:
        return 1
    else:
        return x* power(x,n - 1)


# The nth harmonic number is defined non-recursively as: 1+1/2+1/3+1/4+...+1/n. Come up with a recursive definition and use it to write a function called harmonic that accepts a parameter n that contains an integer value and returns the nth harmonic number.
# 
# 

# In[ ]:


def harmonic(N):
     if (N == 1):
          return 1.0
     else:
          return (1.0/N + harmonic(N-1))


# The "odd/even factorial" of a positive integer n is represented as n and is defined non-recursively as: (n)(n-2)(n-4)...(4)(2) if n is even and (n)(n-2)(n-4)...(5)(3)(1) if n is odd. For example, the odd factorial of 7 equals 7*5*3*1 or 105, and the even factorial of 6 equals 6*4*2 or 48.
# 
# Come up with a recursive definition for the odd/even factorials and use it to write a function called oddevenfact that recursively calcules that odd/even factorial value of its single parameter, which contains an integer value.
# 
# 

# In[ ]:


def oddevenfact(n):
	fact = 1 
	if n > 1:
		fact = n * oddevenfact (n-2)   
	return fact


# In[ ]:


def oddevenfact(n):
	if n==1 or n==2:
		return n
	else:
		return n * oddevenfact(n-2)


# The Fibonacci series (0, 1, 1, 2, 3, 5, 8, 13, 21) has as its first two values 0 and 1; each successive value is then calculated as the sum of the previous two values. The first element in the series is considered the 0th element. 
# 
# The nth element in the series, written as fib(n), is thus defined as:
# * n if n=0 or n=1
# * fib(n-1)+fib(n-2) otherwise
# 
# Write a function fib, that takes a single parameter, n, which contains an integer value, and recursively calculates and returns the nth element of the Fibonacci series.

# In[ ]:


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1)+fib(n-2)
 

print(fib(7))


# In[ ]:


def fib(n):
	if n==0 or n==1:
		return n
	else:
		return fib(n-1)+fib(n-2)


# Write a recursive function, len, that accepts a parameter that holds a string value, and returns the number of characters in the string. 
# The length of the string is:
# * 0 if the string is empy ("")
# * 1 more than the length of the string beyond the first character
# 

# In[ ]:


def len(str):
    if(str==""):
        return 0
    else:
        return 1+len(str[1:])


# Write a recursive function, containsVowel, which accepts one parameter containing a string value and returns True if the string contains a vowel. 
# 
# A string contains a vowel if:
# * The first character of the string is a vowel or
# * The rest of the string (beyond the first character) contains a vowel
# 

# In[ ]:


def containsVowel(s):
	if len(s) != 0:
		vowel_set = s[0]
		if vowel_set in 'aeiouAEIOU':
			return True
		else:
			return containsVowel(s[1:])
	else:
		return False


# Write a recursive function, replace, that accepts a parameter containing a string value and returns another string value, the same as the original string except with each blank replaced by an asterisk "*". 
# 
# Replacing the blanks in a string involves:
# Nothing if the string is empty
# Otherwise
# * If the first character is not a blank, simply concatenate it with the result of replacing the rest of the string.
# * If the first character IS a blank, concatenate an asterisk with the result of replacing the rest of the string.
# 

# In[ ]:


def replace(string):
	if string=="":
		return ""
	elif string[0]==" ":
		return "*" + replace(string[1:])
	else:
		return string[0] + replace(string[1:])


# Write a recursive function, reverse, that accepts a parameter containing a string value and returns the original string in reverse. For example, calling reverse('goodbye') would return 'eybdoog'. 
# 
# Reversing a string involves:
# * No action if the string is empty or only has 1 character
# * Concatenating the last character with the result of reversing the string consisting of the second through next-to-last character, followed by the first character
# 

# In[ ]:


def reverse(s):
    if s == "":
        return s
    else:
        return reverse(s[1:]) + s[0]


# In[ ]:


def reverse(string):
	if len(string) == 0 or len(string) == 1:
		return string
	else:
		return string[len(string)-1] + reverse(string[:-1])


# A palindrome is a word or phrase that reads the same forwards or backwards (e.g. "dad", "mom", "deed"). 
# Write a recrusive function, isPalindrome that accepts a string and returns whether the string is a palindrome. A string is a palindrome if:
# * it is an empty string or consists of a single letter, or
# * if the first and last characters are the same, and the rest of the string forms a palindrome
# 
# Your function should ignore spaces and only compare letters.

# In[ ]:


def isPalindrome(string):
	if len(string) == 0 or len(string) == 1:
		return True
	else:
		if string[0] == string[-1]:
			return isPalindrome(string[1:-1])
		elif string[0] == " ":
			return isPalindrome(string[1:])
		elif string[-1] == " ":
			return isPalindrome(string[:-1])
		else:
			return False


# In[ ]:


def isPalindrome(string):
	if len(string) == 0 or len(string) == 1:
		return True
	else:
		if string[0] == string[-1]:
			return isPalindrome(string[1:-1])
		elif string[0] == " ":
			return isPalindrome(string[1:])
		elif string[-1] == " ":
			return isPalindrome(string[:-1])
		else:
			return False


# The elements of a tuple can be set to 0 recursively as follows:
# * If the tuple has a length of zero, nothing should be done to it.
# * Otherwise, set the first element of the tuple to 0, and then append it to the rest of the tuple.
# 
# Write a function named clearthat accepts one argument, a tuple of any length, and returns a tuple of the same length with every element set to 0.
# 
# 

# In[ ]:


def clear(tup):
    if not tup:
        return ()
    return( (0,) + clear(tup[1:]) )


# In[ ]:


def clear(tup):
	if len(tup) == 0:
		return ()
	else:
		return (0,) + clear(tup[1:])


# The sum of the elements in a tuple can be recusively calculated as follows:
# * The sum of the elements in a tuple of size 0 is 0
# * Otherwise, the sum is the value of the first element added to the sum of the rest of the elements
# 
# Write a function named sum that accepts a tuple as an argument and returns the sum of the elements in the tuple.

# In[ ]:


def sum(tup):
    if(len(tup)==0):
        return 0
    else:
        return tup[0]+sum(tup[1:])


# An 'array palindrome' is an array, which, when its elements are reversed, remains the same.
# Write a recursive function, isPalindrome, that accepts a tuple and returns whether the tuple is a palindrome.
# A tuple is a palindrome if:
# * the tuple is empty or contains one element
# * the first and last elements of the tuple are the same, and the rest of the tuple is a palindrome

# In[ ]:


def isPalindrome(tup):
    if(len(tup)==0 or len(tup)==1):
        return True
    else:
        length=len(tup)
        if (tup[0]==tup[length-1] and isPalindrome(tup[1:length-1])):
            return True
        else:
            return False


# In[ ]:


def isPalindrome(tup):
	if len(tup) == 0 or len(tup) == 1:
		return True
	else:
		if tup[0] == tup[-1]:
			return isPalindrome(tup[1:-1])
		else:
			return False


# The maximum-valued element in a tuple can be recursively calculated as follows:
# * If the tuple has a single element, that is its maximum (tuples of size zero have no maxiumum)
# * Otherwise, compare the first element with the maximum of the rest of the tuple
# 
# Write a function named max that accepts a tuple and returns the largest value in the tuple. Assume the tuple has at least one element.

# In[ ]:


def Max(list):
    if len(list) == 1:
        return list[0]
    else:
        m = Max(list[1:])
        return m if m > list[0] else list[0]


# In[ ]:


def max(tup):
	if len(tup) == 1:
		return tup[0]
	else:
		if tup[0] > max(tup[1:]):
			return tup[0]
		else:
			return max(tup[1:])


# The elements of tuple can be initialized so that tup[i] == i in a recursive fashion as follows:
# A tuple of size 0 is already initialized
# Otherwise:
# * set the last element of the tuple to n-1 (where n is the number of elements in the tuple)
# * initialize the portion of the tuple consisting of the first n-1 elements
# 
# Write a function named init that takes one argument, a tuple of the proper length, and returns an tuple initialized as described above.

# In[ ]:


def init(tup):
	if len(tup) == 0:
		return ()
	else:
		return init(tup[:-1]) + (len(tup)-1,)


# Write a recursive function named productOfOdds that accepts a tuple containing integer values and returns the product of the odd-valued elements in the tuple. You may assume the tuple has at least one odd-valued element. 
# The product of the odd-valued elements may be calculated as follows:
# * If the tuple has a single element and it is odd, return the value of that element; otherwise return 1
# * Otherwise, if the first element of the tuple is odd, return the product of that element and the result of finding the product of hte odd elements of the rest of the tuple. If the first element is not odd, simply return the result of of finding the product of the odd elements of the rest of the tuple.
# 

# In[ ]:


def productOfOdds(tup):
	if len(tup) == 1:
		if tup[0]%2 == 1:
			return tup[0]
		else:
			return 1
	else:
		if tup[0]%2 == 1:
			return tup[0]*productOfOdds(tup[1:])
		else:
			return productOfOdds(tup[1:])


# Two non-negative integers x and y are equal if either:
# * Both are 0, or
# * x-1 and y-1 are equal
# 
# Write a function named equals that recursively determines whether two parameters (both containing integer values) are equal and returns True or False.

# In[ ]:


def equals(x, y):
	if x ==0 and y==0:
		return True
	elif x ==0 or y ==0:
		return False
	else:
		return equals(x-1, y-1)


# Write a definition of a function named copy that reads all of the lines that remain in standard input and displays them in standard output, one on a line with no other spacing. 
# 
# The function must not use a loop of any kind.

# In[ ]:


def copy():	
	try:		
		stdin = input()		
		print(stdin)
		copy()	
	except EOFError:		
		pass


# In[ ]:


#Finally! No more code lab to deal with!!! Book rarely helped with these exercises!!!!!

def copy():
	
	try:
		print(input())
		copy()
	
	except EOFError:
		return


# Write the definition of a function named countPosthat reads integer values from standard input until there are none left and returns the number that are positive. 
# The function must not use a loop of any kind.

# In[ ]:


def countPos():
	try:
		if int(input()) < 0:
			return 1 + countPos()
		else:
			return countPos()
	except EOFError:
		return 0


# Assume the availability of a function named printStars that can be passed one argument, an integer value n, which prints n asterisks. Write a function named printTriangle that receives an integer value as an argument and prints a triangle of asterisks as follows: first a line with 1 asterisk, then a line with 2 asterisks, then a line with 3 asterisks, and so on until it prints a line of n asterisks, at which point it stops. 
# 
# For example, if the function received 5, it would print: 
# 
# 1 x*
# 
# 2 x*
# 
# 3 x*
# 
# 4 x*
# 
# 5 x* 
# 
# The function must not use a loop of any kind. The function should invoke printStarsto accomplish the task of printing a single line.

# In[ ]:


def printTriangle(n):	
	if n > 0:		
		printTriangle(n-1)
		if n > 1:
			print()
	printStars(n)


# In[ ]:


def printTriangle(n):
	if n == 0:
		return
	printTriangle(n-1)
	printStars(n)
	print()


# Write the definition of a function named printStarBucks that receives one parameter containing a non-negative integer value, n, and prints a line consisting of n asterisks followed by n dollar signs. 
# 
# So if the function received 5, it would print: *****$$$$$ 
# 
# And if it received 3, it would print: ***$$$ 
# 
# The function must not use a loop of any kind.

# In[ ]:


def printStarBucks(n):
	if n > 0:
		print("*", end="")
		printStarBucks(n-1)
		print("$", end="")


# In[ ]:


def printStarBucks(n):
	if n == 0:
		return
	print('*', end='')
	printStarBucks(n-1)
	print('$', end='')


# ### ASSIGNMENT 8 - SOME EXAMPLES

# Write a loop that reads strings from standard input where the string is either "land", "air", or "water". The loop terminates when "xxxxx" (five x characters) is read in. Other strings are ignored. After the loop, your code should print out 3 lines: the first consisting of the string "land:" followed by the number of "land" strings read in, the second consisting of the string "air:" followed by the number of "air" strings read in, and the third consisting of the string "water:" followed by the number of "water" strings read in. Each of these should be printed on a separate line.
# 
# ASSUME the availability of a variable, stdin, that references a Scanner object associated with standard input.
# 
# 

# In[ ]:


landCount = 0
airCount = 0
waterCount = 0
word = input()
while word != "xxxxx" :
	if word == "land" :
		landCount += 1
	elif  word == "air" :
		airCount += 1
	elif  word == "water" :
		waterCount += 1
	word = input()
print("land:"+str(landCount))
print("air:"+str(airCount))
print("water:"+str(waterCount))


# Consider this data sequence: "3 11 5 5 5 2 4 6 6 7 3 -8". Any value that is the same as the immediately preceding value is considered a CONSECUTIVE DUPLICATE. In this example, there are three such consecutive duplicates: the 2nd and 3rd 5s and the second 6. Note that the last 3 is not a consecutive duplicate because it was preceded by a 7. Write some code that uses a loop to read such a sequence of non-negative integers, terminated by a negative number. When the code finishes executing, the number of consecutive duplicates encountered is printed. In this case,3 would be printed.
# 
# ASSUME the availability of a variable, stdin, that references a Scanner object associated with standard input.
# 
# 

# In[ ]:


consecdups = 0
prev = eval(input())
n = eval(input())
while n>=0 :
	if n == prev :
		consecdups += 1
	prev = n
	n = eval(input())
print(consecdups)


# Write a loop that displays all possible combinations of two letters where the letters are 'a', or 'b', or 'c', or 'd', or 'e'. The combinations should be displayed in ascending alphabetical order:
# 
# aa
# 
# ab
# 
# ac
# 
# ad
# 
# ae
# 
# ba
# 
# bb
# 
# ...
# 
# ee
# 

# In[ ]:


for i in range(ord('a'), ord('e')+1) :
	for j in range(ord('a'), ord('e')+1) :
		print(chr(i)+chr(j))


# In[ ]:


import itertools
for x in itertools.product('abcde',repeat=2):
	print(x[0]+x[1])


# Assume the input data is structured as follows: first there is a non-negative integer specifying the number of employee timesheets to be read in. This is followed by data for each of the employees. The first number for each employee is an integer that specifies their pay per hour in cents. Following this are 5 integers, the number of hours they worked on each of the days of the workweek. Given this data, write a loop and any necessary code that reads the data and stores the total payroll of all employees into the variable total. Note that you will have to add up the numbers worked by each employee and multiply that by that particular employee's pay rate to get the employee's pay for the week-- and sum those values into total.

# In[ ]:


total = 0
nEmployees = eval(input())
for i in range(nEmployees)  : 
		weekhours = 0
		wagerate = eval(input())
		for j in range(5) :
			hours = eval(input())
			weekhours += hours
		total += wagerate * weekhours


# In[ ]:


total = 0
emp_numbs = input("Amount of employee's")
for i in range(int(emp_numbs)):
	emp_pay = input("Pay per hour in cents")
	emp_mon = input("Pay on Monday")
	emp_tues = input("Pay on Tuesday")
	emp_wed = input("Pay on Wednesday")
	emp_thurs = input("Pay on Thursday")
	emp_fri = input("Pay on Friday")
	hours = int(emp_mon) + int(emp_tues) + int(emp_wed) + int(emp_thurs) + int(emp_fri)
	pay = hours*int(emp_pay)
	total += pay


# ### THE END
