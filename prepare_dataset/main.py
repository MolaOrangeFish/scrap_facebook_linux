from function import join_csv,join_json,add_data_to_csv_with_deepcut
import pandas as pd
from storage import data1,data2

# df = pd.read_csv('data.csv')
# print(df.shape)
# df.drop_duplicates(keep='last',ignore_index=False,inplace=True)

# print(df.shape)

# df.to_csv("sample.csv")

join_json()



####################
### Import data by hand##
"""
data = data2
size = len(data)
# print(size)
for i in range (0,size,2):
    print(f"{data[i]} , {data[i+1]}")
    add_data_to_csv_with_deepcut(data[i],data[i+1])
    """
### Import data by hand##
####################
            
    
    

           
