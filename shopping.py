import json
shopitems = {"shopping_list":
        { 
            "choco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
 }
item = input("enter a item :")
quantity = int(input("enter the quantity :"))
for i in shopitems :
    for j in shopitems[i]:
        if item in shopitems[i] :
            if j == item and int(shopitems[i][j])>=quantity:
                print(shopitems[i][j])
                deducted_amount = int(shopitems[i][j]) - quantity
                shopitems[i][j] = str(deducted_amount)
                break
        elif j != item:
          print("Not available")
          break

with open("data1.json","w") as write_file:  
    json.dump( shopitems, write_file , indent=4)  
with open("data1.json", "r") as read_file:  
    c =  read_file.read() 
print(c)





