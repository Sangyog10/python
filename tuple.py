# ------------Tuple-------------------()
# Tuple-simialr to list but they are immutable
my_tuple=(1,10,"sangyog")
my_tuple[0]="new-data" #it will throw error
print(my_tuple[0])

my_tuple=(1,10) #creating new tuple with same name will change the address of it as my_tuple will point towards new location

t=(1,(1,2),"san",[1,2,3]) 
t[3].append(4) #even thought the tuple is immutable, the list inside tuple is mutable, so we can change it
print(t)
