my_dict={"name":"adzo","age":16,"tribe":"dutch"}
print(my_dict)

# my_dict.clear()
# print(my_dict)

backup=my_dict.copy()
print(backup)

keys=["name","age","City"]
values="unknown"
default=dict.fromkeys(keys,values)
print(default)

getting =backup.get("age")
print(getting)

key1=backup.keys()
print(key1)

values1=my_dict.values()
print(values1)

all_item=backup.items()
print(all_item)

popping=backup.pop("name")
print(popping)
print(backup)

popitem=my_dict.popitem()
print(popitem)
print(my_dict)

new_dict={"name":"amber","Country":"newsland"}
setdefaulting=new_dict.setdefault("Country","kikuyu")
print(setdefaulting)

updating=my_dict.update(new_dict)
print(my_dict)

new_keys=["school","gender","Class"]
new_values=["NewStar","Male",9]
complete_dict=dict(zip(new_keys,new_values))
print(complete_dict)