import pandas as pd
try:
    data=pd.read_csv("sachin.csv")
    above_18=data[data["Age"]>=18]
    above_18.to_csv("output.csv",index=False)
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"Found exception {e}")
    