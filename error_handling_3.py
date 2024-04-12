# Write a Python program that takes a user input and converts it to an integer. Handle the ValueError and display a custom error message when 
# the input cannot be converted to an integer.
import argparse
import logging
logging.basicConfig(filename="error_handling_3.log",level=logging.INFO,encoding="utf-8")
if __name__ =="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--value",required=True)
    agr=parser.parse_args()
    try:
        a=int(agr.value)
        logging.info("Conversion sucessful")
    except ValueError:
        logging.error("Value cannot be converted into integer")