#even numbers with list coprehension
list = [1,2,3,4,5]
res = [i+1 for i in list if i < 4]
print(res)
res = [i for i in list if i % 2 == 0]
print(res)


#creating a dictionary comprehension from two list
keys = ["name","age","city"]
values = ["Esha",18,"hyd"]
dictionary = {k:v for k,v in zip(keys,values)}
print(dictionary)