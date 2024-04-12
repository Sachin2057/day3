# Implement a program that takes user input for a filename, opens the file in read mode, and displays its contents. Handle the 
# FileNotFoundError and display an error message if the file is not found.
import argparse
import logging
logging.basicConfig(filename="error_handling_2.log",level=logging.DEBUG,encoding="utf-8")
if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--filename', required=True)
    args = parser.parse_args()
    filename=args.filename
    try:
        with open(file=filename,mode="r",encoding="utf-8") as f:
            text=f.read()
            logging.debug(text)
            f.close()
    except FileNotFoundError:
        logging.error("File not found")
    except Exception as e:
        logging.error(f"{e}")