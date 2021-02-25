import pandas as pd
import numpy as np

# ----------------------------------------------------------------------------------------------------

# Convert numeric playoffs to text by applying text_playoffs()

rays_df = pd.DataFrame([[2012, 697, 577, 90, 0], [2011, 707, 614, 91, 1], [2010, 802, 649, 96, 1], [2009, 803, 754, 84, 0], [2008, 774, 671, 97, 1]])

rays_df.columns = ['YR' ,'RS' ,  'RA'  , 'W' , 'Playoffs']


def text_playoffs(num_playoffs):
  if num_playoffs == 1:
    return 'Yes'
  else:
    return 'No'

# Use .apply() and a lambda function to apply text_playoffs() to each row's 'Playoffs' value of the rays_df DataFrame.

textual_playoffs = rays_df.apply(lambda row: text_playoffs(row['Playoffs']), axis = 1 )
print(textual_playoffs)

# ----------------------------------------------------------------------------------------------------
print("="*25)
# Let's use the below function and the .apply() method to see which manager is correct.

dbacks = [['ARI', 'NL', 2012, 734, 688, 81, 162, 0], ['ARI', 'NL', 2011, 731, 662, 94, 162, 1], ['ARI', 'NL', 2010, 713, 836, 65, 162, 0], ['ARI', 'NL', 2009, 720, 782, 70, 162, 0], ['ARI', 'NL', 2008, 720, 706, 82, 162, 0], ['ARI', 'NL', 2007, 712, 732, 90, 162, 1], ['ARI', 'NL', 2006, 773, 788, 76, 162, 0], ['ARI', 'NL', 2005, 696, 856, 77, 162, 0], ['ARI', 'NL', 2004, 615, 899, 51, 162, 0], ['ARI', 'NL', 2003, 717, 685, 84, 162, 0], ['ARI', 'NL', 2002, 819, 674, 98, 162, 1], ['ARI', 'NL', 2001, 818, 677, 92, 162, 1], ['ARI', 'NL', 2000, 792, 754, 85, 162, 0], ['ARI', 'NL', 1999, 908, 676, 100, 162, 1], ['ARI', 'NL', 1998, 665, 812, 65, 162, 0]]

columns = ['Team', 'League', 'Year', 'RS', 'RA', 'W', 'G', 'Playoffs']

dbacks_df = pd.DataFrame(dbacks)
dbacks_df.columns = columns
print(dbacks_df)

# funciton to calculate win percentage
def calc_win_perc(wins, games_played):
  win_perc = wins / games_played
  return np.round(win_perc, 2)

  # Create a win percentage Series 
win_percs = dbacks_df.apply(lambda row: calc_win_perc(row['W'], row['G']), axis=1)
print(win_percs, '\n')

# Append a new column to dbacks_df
dbacks_df['WP'] = win_percs
print(dbacks_df)

# Display dbacks_df where WP is greater than 0.50
print(dbacks_df [ dbacks_df['WP'] > 0.5 ] )
