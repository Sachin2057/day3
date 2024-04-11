# Create a function add_to_json that takes a filename and a dictionary as input. The function should read the JSON data from the file, add the new dictionary to it, 
# and write the updated data back to the same file.
import json
import logging
logging.basicConfig(filename="file_handling_json.log",level=logging.DEBUG,encoding="utf-8")
def add_to_json(filename,dict):
    try:
        with open(filename,"r") as f:
            data=json.load(f)
    except FileNotFoundError:
        logging.error("File not found")
    data.append(dict)
    try:
        with open(filename,"w") as f:
            json.dump(data,f,indent=3)
    except FileNotFoundError:
        logging.error("File not found")
    
add_to_json("json_data.json",{"name":"Sachin","age":15})
    