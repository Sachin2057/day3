# Write a Python program that takes a user input and converts it to an integer. Handle the ValueError and display a custom error message when 
# the input cannot be converted to an integer.
import argparse
if __name__ =="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--value",required=True)
    agr=parser.parse_args()
    try:
        a=int(agr.value)
        print(a)
    except ValueError:
        print("Value cannot be converted into integer")