# Create a function add_to_json that takes a filename and a dictionary as input. The function should read the JSON data from the file, add the new dictionary to it, 
# and write the updated data back to the same file.
import json
import logging
logging.basicConfig(filename="file_handling_jon.log",level=logging.INFO,encoding="utf-8")
def add_to_json(filename,dict):
    try:
        with open(filename,"r") as f:
            data=json.load(f)
        data.append(dict)
        logging.info("File opened")
        logging.debug(data)
        with open(filename,"w") as f:
            json.dump(data,f,indent=3)
        logging.info("Data dumped")
        logging.debug(data)
    except FileNotFoundError:
        logging.error("File not found")
    except Exception as e:
        logging.error(f"{e}")
    
add_to_json("json_data.jon",{"name":"Sachin","age":15})
    