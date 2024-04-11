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
        print(result)
    except Exception as e:
        print("Error occured {e}")
search_log("example.log","should")