
# Program to create series
  
# Import Panda Library
import pandas as pd  
  
# Create series with Data, and Index
a = pd.Series(Data, index = Index)

# Program to Create series with scalar values 
  
# Numeric data
Data =[1, 3, 4, 5, 6, 2, 9]  
  
# Creating series with default index values
s = pd.Series(Data)    
  
# predefined index values
Index =['a', 'b', 'c', 'd', 'e', 'f', 'g'] 
  
# Creating series with predefined index values
si = pd.Series(Data, Index) 
