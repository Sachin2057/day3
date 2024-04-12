# Write a Python program that takes user input for age. Create a custom exception InvalidAgeError 
# to handle cases where the age is below 0 or above 120.
import argparse
import logging
logging.basicConfig(filename="error_handling.log",level=logging.DEBUG,encoding="utf-8")
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
        if(age>120 or age<0):
            raise InvalidAgeError
        else:
            logging.debug(f"Age={age}")
    except InvalidAgeError as e:
        logging.error(f"An error occured:{e}")
        