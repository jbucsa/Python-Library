# First IMPORT pandas as pd to create a dataframe
import pandas as pd
# Second IMPORT numpy as np to do math operations
import numpy as np


# Use this to add modified data to a Dataframe.

df = pd.DataFrame({'X': [1, 2, 3, 4, 5, 6, 7, 8, 9], 'Y': [4, 5, 6, 6, 7, 11, 12, 14, 15], 'Z': [2, 7, 8, 11, 12, 15, 17, 3, 4]})


# This is just creates a copy of the df dataframe and renames it to df_squared. This step is SKIP ABLE but allows use to safe guard the original dataframe from future changes. 
df_squared = df.copy()

# Create a new column with the same index as df with the values in the respective indexis
square_r = (df_squared["X"] ** 2) + (df_squared["Y"] ** 2) + (df_squared["Z"] ** 2)


# Adds a row to the df_squared dataframe name New_Squared_Values that is the values found in the pervious step. 
df_squared["New_Squared_Values"] = np.sqrt(square_r)



