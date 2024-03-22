import pandas as pd

# SELECTING Specific ROW in a Dataframe 'df'

"""
1. Using .loc[]:

    The .loc[] attribute allows you to select rows based on their labels (index values). It's generally preferred when you know the actual values of the index (e.g., row names or integer positions).
"""

df_1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['apple', 'banana', 'cherry'])

# Select the row with index 'banana'
specific_row_1 = df_1.loc['banana']

# Select multiple rows (using a list or boolean mask)
specific_rows_1 = df_1.loc[['apple', 'cherry']]  # By index labels
all_rows_with_A_gt_2 = df_1.loc[df_1['A'] > 2]  # By boolean condition



"""
2. Using .iloc[]:

    The .iloc[] attribute selects rows based on their integer positions within the DataFrame. It's useful when you know the order of the rows (starting from 0 for the first row).
"""

df_2 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['apple', 'banana', 'cherry'])

# Select the second row (index 1)
specific_row = df_2.iloc[1]

# Select multiple rows (using integer positions)
specific_rows = df_2.iloc[[0, 2]]  # Select rows at positions 0 and 2


"""
Summary
    Choosing the Right Method:

    Use .loc[] when you want to select rows based on their index labels (more readable for named indexes).

    Use .iloc[] when you need to select rows based on their position (faster for large DataFrames).

Remember that both methods return a new DataFrame containing only the selected rows. They don't modify the original DataFrame in place.

"""
