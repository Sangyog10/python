# ----------------Python-----------------

print(bin(111)) #prints the binary of the given number

# To print the complex number
c= complex(3,4)
print(c)

# String
hello = "hello"
repeat_hello = "Hello " * 3 
print(repeat_hello)
print(hello[-1]) #negative -1 gives the value at last index


# Formatted printing
name = "sangyog"
age = 23
formatted_text =f"My name is {name} and my age is {age}"
print(formatted_text)


#Slicing
name = "sangyog"
print(name[2:5]) #print from 2th index to 4th index
print(name[:5])  #prints from 0th index to 4th index(n-1)
print(name[2:])  #prints from 2th index to last index

print(name[::2]) #steps of 2(i.e prints character every 2 step)

# "is Vs =="
# The == operator checks if two values are equal, 
#  is checks if two variables refer to the same object in memory.
a = [1,2,3]
b = [1,2,3]
c = a
print(a==b)
print(a is b)
print(a is c)




# built-in function
s = "  Hello World  "
print(s.lower())     # Output: hello world
print(s.upper())     # Output: HELLO WORLD
print(s.strip())     # Output: Hello World
print(s.replace("World", "Python"))  # Output: Hello Python
print(s.find("World"))  # Output: 7 (index of the first occurrence)