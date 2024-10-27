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


# --------------List---------------[]
# Lists in python are similar to array, they are mutable
my_list=[1,10,"abc",[15]]
my_list.insert(1,"abc")
print(my_list)



# ------------Tuple-------------------()
# Tuple-simialr to list but they are immutable
my_tuple=(1,10,"sangyog")
my_tuple[0]="new-data" #it will throw error
print(my_tuple[0])

my_tuple=(1,10) #creating new tuple with same name will change the address of it as my_tuple will point towards new location

t=(1,(1,2),"san",[1,2,3]) 
t[3].append(4) #even thought the tuple is immutable, the list inside tuple is mutable, so we can change it
print(t)



# ----------------Set------------------------------{value}
# it doesnot contain duplicate and has only unique value and order doesnot matter
print(type({}))  
print(type({2}))
s={1,2,3,1,2,3,3,3}
s.add((2,3))
print(s)


# -----------------------Dictionaries---------------------------{}
# we have key vlaue pair in dictionary
#we cannot use unhashable function like list in the key beacuse it will hash all the keys before saving it
d={"name":"sangyog","age":22,(1,2):"my tuple"}
print(type(d))
print(d.keys())
print(d.values())
print(d.items()[1]) #does not suport index
del d["age"]
print(d.get("name"))

d={
    "name":"sangyog",
    (1,2):"my tuple",
    10:100
    # [1,2]:"my list"  #cannot store list as key as it is not hashable
}
for i in d.keys():
 print(i)


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
