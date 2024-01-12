# Check if all items in the tuple are the same

def check_items(tup):
    return all(i == tup[0] for i in tup)

tuple1= (56, 56, 56, 56, 56)
tuple2 = (45, 87, 23, 12)

print(check_items(tuple1))

print(check_items(tuple2))
