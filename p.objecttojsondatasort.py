import json
input={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
mydata=json.dumps(input,sort_keys=True)
print(mydata)
