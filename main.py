#making a Dictionary
#dictionary is a collection of items in a key value pair similar to list but without index numbers

person={"name":"Krishiv","age":"15","hobbies":"going to the gym"}
print(person)

#access the values using keys
print(person["name"])

print(person["hobbies"])

#adding new item to the dictionary


person["country"]= "england" #counrty is a key and england is a value for it

print(person)

person={"name":"johnny","age":"15","hobbies":"swimming"}
print(person)

#access the values using keys 
print(person["name"])

print(person["hobbies"])

person["country"]="croatia"

#getting keys from dictionary 
print(person.keys())

print(person.values())

#size/length of dictionary -how many items in the dictionary 

print(len(person))
#check whether key exists in the dictionary 
print("Hobby"in person)#this will give true if hobby is there otherewise false

#deleting key-value pair (item) from the dictionary

del person["hobbies"]
print(person)

#modifying values of the dictionary 
person["age"]=20
print(person)

#ierating (going to each item)in the dictionary 
list=[]#empty list to store the values 
for i in person:
    list.append(i)#appendis used to add an item to the list 

print(list)

#sorting items in the list 
list.sort()
print(list)

game={"name1":"roblox","name2":"fortnite,","name 3":"fifa"}
print(game)

game["sport"]="volleyball"

print(game)
#adding new items to the dictionary

#asking input from the user of the key and value
game={"name1":"volleyball"}

key_name= input("enter the value for it:")
value = input("enter the value for it:")
game[key_name]=value
print(game)