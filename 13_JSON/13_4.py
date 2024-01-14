# Sort JSON keys in and write them into a file
# Sort folowing JSON data alphabetical order of keys
import json
dat_JSON = {"id" : 1, "name" : "value2", "age" : 29}

with open('dat_JSON.json', 'w') as dat_write:
    json.dump(dat_JSON, dat_write, indent = 4, sort_keys = True)
print("Print file DONE")
