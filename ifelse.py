'''
Equal : a==b
not equal: a!=b
less than: a<b
greater than :b>a
greater than or equal to :a>=b
less than equal to: a<=b

 
'''
# if statement

a=33
b=200
if b>a:
  print("b is geater than a")


# # elif
a = 33
b = 33
if b>a:
    print("b is greater than a")
elif a==b:
        print("a and b  are equal")

# # ELSE
a = 200
b = 33
if b>a:
    print("b is greater than a")
elif a==b:
    print("a is greater than b")
else:
    print("a is greater than b")
    
# # SHORT HAND IF 
a=300
b=30
if a>b: print("a is greater than b ")

# # SHORT HAND IF ELSE 
a = 2
b = 330
print("A") if a > b else print("B")

# # AND operator 
a =200
b =33
c =500
if a>b and c<a:
 print("both conditions are true")

# #OR OPERATOR
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# # Nested If
# Example
x = 41

if x > 10:
  print("Above ten,")
  if x >20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# #The PASS Statement
# '''
# if statements cannot be empty,
# but if you for some reason have an if statement with no content,
# put in the pass statement to avoid getting an error.
# '''
a = 33
b = 200

if b > a:
 pass
