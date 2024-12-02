from tensorflow.python.ops.gen_data_flow_ops import priority_queue

fruits = ["apple","mango","cherry"]
print(fruits) # before adding a new fruit

fruits.append("orange")
print(fruits)

fruits.insert(0,"banana")
print(fruits)
sample = ["grape","kiwi"]
fruits.extend(sample)
print(fruits)
#-----------------------------------------------------------------------------
fruits.append("banana")
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.pop()
print(fruits)

fruits.pop(1)
print(fruits)

fruits.clear()
print(fruits)