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
