# The enumerate() function is useful when you need to access both the index and the value in a sequence while iterating.

fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index,fruit)



student = {"name": "Alice", "age": 25, "city": "New York"}


for key,value in enumerate(student):
    print(key,value)  #gives the index of key



