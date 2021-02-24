import pandas as pd

# Convert numeric playoffs to text by applying text_playoffs()

rays_df = pd.DataFrame([[2012, 697, 577, 90, 0], [2011, 707, 614, 91, 1], [2010, 802, 649, 96, 1], [2009, 803, 754, 84, 0], [2008, 774, 671, 97, 1]])

rays_df.columns = ['YR' ,'RS' ,  'RA'  , 'W' , 'Playoffs']


def text_playoffs(num_playoffs):
  if num_playoffs == 1:
    return 'Yes'
  else:
    return 'No'

# Use .apply() and a lambda function to apply text_playoffs() to each row's 'Playoffs' value of the rays_df DataFrame.

# textual_playoffs = rays_df.apply(lambda row: text_playoffs(row['Playoffs']), axis = 1 )
# print(textual_playoffs)

# The .apply() method let's you apply functions to all rows or columns of a DataFrame by specifying an axis.

# If you've been using pandas for some time, you may have noticed that a better way to find these stats would use the pandas built-in .sum() method.

# You could have used rays_df.sum(axis=0) to get columnar sums and rays_df[['RS', 'RA']].sum(axis=1) to get row sums.

# You could have also used .apply() directly on a Series (or column) of the DataFrame. For example, you could use rays_df['Playoffs'].apply(text_playoffs) to convert the 'Playoffs' column to text.

