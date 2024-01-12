# Sort a tuple of tuples by 2nd item

tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))

# Method 1
tuple1 = tuple(sorted(list(tuple1), key = lambda x : x[1]))
print("Method 1: ", tuple1)

# Method 2
def order(elem):
    return elem[1]

tuple2 = tuple(sorted(tuple1, key = order))
print("Method 2: ", tuple2)
