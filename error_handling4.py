import argparse
class InvalidAgeError(Exception):
    def __init__(self):
        self.message="Invalid Age"
        super().__init__(self.message)
if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--age",required=True)
    arg=parser.parse_args()
    age=int(arg.age)
    try:
        if(age>120 or age>0):
            raise InvalidAgeError
        else:
            print(f"Age={age}")
    except InvalidAgeError as e:
        print(f"An error occured:{e}")
        