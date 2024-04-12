# Write a Python program that takes two integers as input and performs division (num1 / num2). Handle the ZeroDivisionError and 
# display a custom error message when the second number is zero.
import logging
logging.basicConfig(filename="error_handling_1.log",level=logging.DEBUG,encoding="utf-8")
def division(num1,num2):
    try:
        result=num1/num2
        return result
    except ZeroDivisionError:
        logging.critical("Second number cannot be zero")
    except Exception as e:
        logging.error("{e}")
result=division(1,3)
logging.debug(result)
result=division(2,0)
logging.debug(result)        