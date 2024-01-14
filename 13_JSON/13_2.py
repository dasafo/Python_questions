# Access the value of key2 from the following JSON

import json
dat = """{"key1" : "value1", "key2" : "value2", "key3" : "value3"}"""

dat2 = json.loads(dat) #converto to dict
print(type(dat2))
print(dat2['key2'])
