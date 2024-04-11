# Create a function search_log that takes a log file and a search keyword as input. The function should find and display all 
# lines containing the search keyword.
import logging
logging.basicConfig(filename="file_handling_logging.log",level=logging.DEBUG,encoding="utf-8")
def search_log(file,key_word):
    result=[]
    try:
        with open(file,mode='r',encoding='utf-8') as f:
            data=f.readlines()
            for i in data:
                j=i.split(" ")
                if(key_word in j):
                    result.append(i)
            f.close()
        logging.debug(result)
    except Exception as e:
        logging.error("Error occured {e}")
search_log("example.log","should")