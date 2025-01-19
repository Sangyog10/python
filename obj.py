# everything is object in python 

obj="string"
print(type(obj))
print(dir(obj)) #it will give all the methods that are availble for that obj
print(id(obj)) #it wil give memory address


# in python, if x=5 and a=x, both will point to the same loaction which store 5
str="sangyog"
x=str
if id(str)==id(x):
    print("Both are stored in same location")
else:
    print("both are in differnet memroy location")


# mutable-we can change its data ->lists, dictionary, sets
# immutable-we cannot change its data->tuple,string, integer,float

#hashable->if input remians same , output will be same, eg hash(123) and its value will always be the same, cannot hash mutable object


# -----------------Iterable-------------------------
# if object is iterable we can use for loop in it
print(iter([1,2]))
print(iter((1,2)))


for i in 34: #not iterable
    print(i)

for i in range(34):
    print(i)

d={"name":"sangyog","age":22,(1,2):"my tuple"}

for key in d.keys():
    print(f"my d has key {key} and value {d.get(key)}")

for el in d.items():
    print(f"my d has key {el[0]} and value {el[1]}")

for a,b in d.items():
    print(f"my d has key {a} and value {b}")



# -----------------Destucturing---------------------
t=("name","age")
a,b=t
print(a)

d={"name":"sangyog","age":22,(1,2):"my tuple"}
for a,b in d.items():
    print(f"my d has key {a} and value {b}")
