# Access the nested key 'salary' from the following JSON

import json

data_json ="""{
    "company":{
        "employee":{
            "name":"david",
            "payble":{
                "salary":8500,
                "bonus":400
            }
        }
    }
}"""
dat = json.loads(data_json)

print(dat['company']['employee']['payble']['salary'])
