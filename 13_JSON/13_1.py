# Convert the following dictionary into JSON format

dat = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3'}

import json

dat_json = json.dumps(dat)
print(dat_json)
