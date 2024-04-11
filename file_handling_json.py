import json
def add_to_json(filename,dict):
    try:
        with open(filename,"r") as f:
            data=json.load(f)
    except FileNotFoundError:
        print("File not found")
    data.append(dict)
    try:
        with open(filename,"w") as f:
            json.dump(data,f,indent=3)
    except FileNotFoundError:
        print("File not found")
    
add_to_json("json_data.json",{"name":"Sachin","age":15})
    