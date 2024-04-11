# Implement a program that reads a CSV file named "data.csv," containing columns "Name" and "Age."
# Create a new CSV file called "adults.csv" with only the rows of 
# individuals who are 18 years or older.
import pandas as pd
import logging
try:
    data=pd.read_csv("sachin.csv")
    logging.info("file opened sucessfully")
    above_18=data[data["Age"]>=18]
    above_18.to_csv("output.csv",index=False)
except FileNotFoundError:
    logging.error("File not found")
except Exception as e:
    logging.error(f"Found exception {e}")
    