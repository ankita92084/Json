import json
a={"Name": "Abhishek",
    "Designation": "CEO of navgurukul",
    "Gender":" male",
    "Age": "29"
 }
mydata=open("mydatafile.json","w")
json.dump(a,mydata,indent=4)
mydata.close()
