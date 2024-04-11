import pandas as pd
data = [['Sachin', 20], ['Sanskar', 15], ['June', 15]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
df.to_csv("sachin.csv",index=False)