
#List operations
l=int(input("No. of ele in list:"))
mylist=[]
for i in range(l):
	mylist.append(int(input()))
print(mylist)
print("2nd element:",mylist[2])
print("Insert 9 at 3 index")
mylist.insert(3,9)
print(mylist)
print("Delete at index 3")
mylist.pop(3)
print(mylist)

#Tuple operations
print("\nTUPLE")
mytuple=('abc','def','efg','hij','klm')
print(mytuple)
print("ele at 4:",mytuple[4])
print("2 and 3 ele:",mytuple[2:4])

#Dictionary operations
print("\nDictionary:")
my_dict={}
l=int(input("No. of ele in dict:"))
i=0
while(i<l):
	user=input("Enter key:value -->")
	key,value=user.split(":")
	my_dict[key]=value
	i+=1
print(my_dict)
del my_dict['H']
print("Dict after deletion:",my_dict)
my_dict['J']='12'
print("Add J:12 in dict:",my_dict)



