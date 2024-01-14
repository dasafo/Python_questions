# PrettyPrint following JSON data
# PrettyPRint following JON data with indent level 2
# and key-value separators should be ("," ," = ")


import json
dat = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3'}

dat_json = json.dumps(dat, indent= 2, separators= (",", " = "))
print(dat_json)

